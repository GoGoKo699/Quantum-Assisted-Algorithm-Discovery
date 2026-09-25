"""Minimal typed access to the installed native Z3 C API (no Python binding needed)."""
import ctypes as C
import ctypes.util
import json,time,re
from pathlib import Path
library_path=ctypes.util.find_library('z3')
if not library_path:
    raise RuntimeError('The optional SMT checks require the native Z3 shared library.')
lib=C.CDLL(library_path)
def api(name,args,rest):
    f=getattr(lib,name);f.argtypes=args;f.restype=rest;return f
P=C.c_void_p; S=C.c_char_p
mk_config=api('Z3_mk_config',[],P);del_config=api('Z3_del_config',[P],None)
mk_context=api('Z3_mk_context_rc',[P],P);del_context=api('Z3_del_context',[P],None)
mk_solver=api('Z3_mk_solver',[P],P)
inc_solver=api('Z3_solver_inc_ref',[P,P],None);dec_solver=api('Z3_solver_dec_ref',[P,P],None)
from_string=api('Z3_solver_from_string',[P,P,S],None)
check=api('Z3_solver_check',[P,P],C.c_int)
get_model=api('Z3_solver_get_model',[P,P],P);model_string=api('Z3_model_to_string',[P,P],S)
get_reason=api('Z3_solver_get_reason_unknown',[P,P],S)
mk_params=api('Z3_mk_params',[P],P);inc_params=api('Z3_params_inc_ref',[P,P],None);dec_params=api('Z3_params_dec_ref',[P,P],None)
mk_symbol=api('Z3_mk_string_symbol',[P,S],P)
set_uint=api('Z3_params_set_uint',[P,P,P,C.c_uint],None);set_params=api('Z3_solver_set_params',[P,P,P],None)
version=api('Z3_get_full_version',[],S)

def solve(text:str,timeout_ms:int=5000):
    if timeout_ms <= 0 or not isinstance(text, str):
        raise ValueError('Expected SMT-LIB text and a positive timeout.')
    cfg=mk_config();ctx=mk_context(cfg);del_config(cfg);slv=mk_solver(ctx);inc_solver(ctx,slv)
    prm=mk_params(ctx);inc_params(ctx,prm)
    set_uint(ctx,prm,mk_symbol(ctx,b'timeout'),timeout_ms);set_uint(ctx,prm,mk_symbol(ctx,b'random_seed'),0)
    set_params(ctx,slv,prm);dec_params(ctx,prm)
    t=time.perf_counter()
    try:
        from_string(ctx,slv,text.encode());status=check(ctx,slv)
        out={'status':{1:'sat',0:'unknown',-1:'unsat'}[status],'seconds':time.perf_counter()-t,'version':version().decode()}
        if status==1:out['model']=model_string(ctx,get_model(ctx,slv)).decode()
        if status==0:out['reason']=get_reason(ctx,slv).decode()
        return out
    finally:dec_solver(ctx,slv);del_context(ctx)

if __name__=='__main__':
    print(solve('(declare-const x Int)(assert (= x 3))'))
