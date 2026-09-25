#!/usr/bin/env python3
"""Reproduce without overwriting archived results. Python stdlib + C++17."""
from __future__ import annotations
import argparse,json,subprocess,tempfile,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
RUNS={
'school_raw.json':('school',0,64,4096,23),
'school_legal.json':('school',1,64,4096,23),
'school_dependency.json':('school',2,64,4096,23),
'school_adaptive.json':('school',3,64,4096,23),
'excursion_raw.json':('excursion',0,64,4096,23),
'excursion_legal.json':('excursion',1,64,4096,23),
'excursion_dependency.json':('excursion',2,64,4096,23),
'school_raw_long.json':('school',0,64,65536,23),
'school_legal_long.json':('school',1,64,65536,23),
'school_dependency_long.json':('school',2,64,65536,23),
}
def main():
 p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group();g.add_argument('--full',action='store_true');g.add_argument('--quick',action='store_true');a=p.parse_args()
 subprocess.run([sys.executable,str(ROOT/'guided_core.py'),'--check'],check=True,timeout=90)
 with tempfile.TemporaryDirectory() as temp:
  exe=Path(temp)/'survey'
  subprocess.run(['g++','-std=c++17','-O3','-Wall','-Wextra',str(ROOT/'guided_survey.cpp'),'-o',str(exe)],check=True,timeout=90)
  selected=RUNS if a.full else {'school_legal.json':RUNS['school_legal.json']}
  for name,args in selected.items():
   cmd=[str(exe),str(ROOT/'reference23.txt')]+list(map(str,args))
   completed=subprocess.run(cmd,check=True,capture_output=True,text=True,timeout=180)
   actual=json.loads(completed.stdout);expected=json.loads((ROOT/name).read_text())
   if actual!=expected:raise RuntimeError(f'{name}: deterministic result mismatch')
   print(name+': exact match',flush=True)
 print('Selected reproduction checks passed.')
if __name__=='__main__':main()
