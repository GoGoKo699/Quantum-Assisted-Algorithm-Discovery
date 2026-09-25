#!/usr/bin/env python3
"""Exact reference checks for guided search and directed-edge reversible addressing.
All numerics are classical tests; no hardware, novel identity, or advantage claim.
"""
from __future__ import annotations
import itertools,json,collections
from pathlib import Path
Term=tuple[int,int,int]; Scheme=tuple[Term,...]
def tensor(s:Scheme,m:int)->int:
 out=0
 for a,b,c in s:
  for i in range(m):
   if a>>i&1:
    for j in range(m):
     if b>>j&1:
      for k in range(m):
       if c>>k&1:out^=1<<((i*m+j)*m+k)
 return out

def school(n:int)->Scheme:
 return tuple((1<<(i*n+j),1<<(j*n+k),1<<(i*n+k)) for i in range(n) for j in range(n) for k in range(n))
def flip(s:Scheme,label:tuple[int,int,int])->Scheme:
 a,i,j=label
 if a not in range(3) or i not in range(len(s)) or j not in range(len(s)) or i==j or s[i][a]!=s[j][a]:return s
 out=[list(t) for t in s];b,c=(a+1)%3,(a+2)%3
 out[i][b]^=out[j][b];out[j][c]^=out[i][c]
 return tuple(map(tuple,out))
def moves(s:Scheme,rank_preserving:bool=True):
 result=[]
 for a in range(3):
  for i in range(len(s)):
   for j in range(len(s)):
    if i==j or not all(s[i]) or not all(s[j]) or s[i][a]!=s[j][a]:continue
    t=flip(s,(a,i,j))
    if t==s or (rank_preserving and not all(all(u) for u in t)):continue
    result.append((a,i,j))
 return tuple(result)
def edge_shift(s:Scheme,k:int):
 """Involution on state plus outgoing-edge ordinal. Invalid ordinals fixed."""
 labels=moves(s)
 if k<0 or k>=len(labels):return s,k
 label=labels[k];t=flip(s,label);reverse=moves(t).index(label)
 return t,reverse

def dependency(vectors:list[int]):
 basis={}
 for j,v in enumerate(vectors):
  mask=1<<j
  while v:
   b=v.bit_length()-1
   if b in basis:v^=basis[b][0];mask^=basis[b][1]
   else:basis[b]=(v,mask);break
  if not v:return mask
 return None

def reducible(s:Scheme)->bool:
 for a in range(3):
  groups=collections.defaultdict(list)
  for t in s:
   if all(t):groups[t[a]].append(t)
  for g in groups.values():
   for b in range(3):
    if b!=a and dependency([t[b] for t in g]) is not None:return True
 return False

def check_reference(root:Path):
 d=json.loads((root/'reference23.json').read_text());s=tuple(map(tuple,d['terms_gf2']))
 if tensor(s,9)!=tensor(school(3),9):raise RuntimeError('binary reference failed')
 checks=0
 for i,j,k in itertools.product(range(9),repeat=3):
  v=sum(a[i]*b[j]*c[k] for a,b,c in zip(d['U'],d['V'],d['W_row_major']))
  want=int(i%3==j//3 and i//3==k//3 and j%3==k%3)
  if v!=want:raise RuntimeError('integer reference failed')
  checks+=1
 return checks

def main():
 root=Path(__file__).parent;ref_checks=check_reference(root)
 witness_checks=[]
 for path in sorted(root.glob('*_*.json')):
  d=json.loads(path.read_text())
  if 'best_witness' not in d:continue
  s=tuple(map(tuple,d['best_witness']))
  if tensor(s,9)!=tensor(school(3),9):raise RuntimeError(f'witness {path.name} failed')
  if sum(all(t) for t in s)!=d['best_active']:raise RuntimeError('active count mismatch')
  witness_checks.append(path.name)
 collision=json.loads((root/'selector_collision.json').read_text());sx=tuple(map(tuple,collision['x']));sy=tuple(map(tuple,collision['y']));image=tuple(map(tuple,collision['image']))
 if sx==sy or flip(sx,moves(sx)[0])!=image or flip(sy,moves(sy)[0])!=image:raise RuntimeError('collision failed')
 # Exhaust all nonzero-factor triples. Address capacity 32 includes invalid labels.
 pool=tuple(itertools.product(range(1,4),repeat=3));states=tuple(itertools.product(pool,repeat=3))
 labels={s:moves(s) for s in states};edge_checks=0;invalid_checks=0;invalid_executed=0;reverse_indices=[]
 for s in states:
  old=tensor(s,2)
  for k,label in enumerate(labels[s]):
   t=flip(s,label)
   if tensor(t,2)!=old:raise RuntimeError('tensor mismatch')
   j=labels[t].index(label)
   if flip(t,labels[t][j])!=s or labels[s].index(labels[t][j])!=k:raise RuntimeError('shift involution failed')
   edge_checks+=1
  invalid_checks+=32-len(labels[s])
  for bad in sorted({len(labels[s]),31}):
   if edge_shift(s,bad)!=(s,bad):raise RuntimeError('invalid-label rule failed')
   invalid_executed+=1
 for s in (sx,sy):reverse_indices.append(edge_shift(s,0)[1])
 if reverse_indices[0]==reverse_indices[1]:raise RuntimeError('which-edge information lost')
 # Small connected labelled plateau; explicit coined-walk norm/inverse check.
 todo=[sx];seen={sx}
 for s in todo:
  for label in labels[s]:
   t=flip(s,label)
   if t not in seen:seen.add(t);todo.append(t)
 ids={s:i for i,s in enumerate(todo)};basis=[(s,k) for s in todo for k in range(len(labels[s]))];index={e:i for i,e in enumerate(basis)}
 import math,cmath
 vals=[complex((i*17+3)%37-18,(i*29+5)%41-20) for i in range(len(basis))]
 norm=math.sqrt(sum(abs(x)**2 for x in vals));vals=[x/norm for x in vals]
 def coin(v):
  out=v.copy()
  for s in todo:
   indices=[index[s,k] for k in range(len(labels[s]))]
   if not indices:continue
   avg=sum(v[i] for i in indices)/len(indices)
   for i in indices:out[i]=2*avg-v[i]
  return out
 def shift(v):
  out=[0j]*len(v)
  for i,(s,k) in enumerate(basis):
   label=labels[s][k];t=flip(s,label);j=labels[t].index(label);out[index[t,j]]=v[i]
  return out
 walked=shift(coin(vals));back=coin(shift(walked))
 discrepancy=max(abs(a-b) for a,b in zip(back,vals))
 normerr=abs(sum(abs(a)**2 for a in walked)-1)
 if discrepancy>1e-12 or normerr>1e-12:raise RuntimeError('walk unitarity numerical check failed')
 result={'integer_reference_coefficients_checked':ref_checks,'verified_survey_witnesses':witness_checks,'exhaustive_small_states':len(states),'directed_legal_edges_checked':edge_checks,'invalid_ordinals_counted_from_rule':invalid_checks,'invalid_ordinal_calls_executed':invalid_executed,'selector_collision_confirmed':True,'collision_reverse_ordinals':reverse_indices,'small_component_vertices':len(todo),'small_component_directed_edges':len(basis),'small_component_marked_vertices':sum(reducible(s) for s in todo),'coin_shift_inverse_max_error':discrepancy,'coin_shift_norm_error':normerr,'scope':'Exact algebra/edge-permutation tests and one small classical coined-walk simulation, not gate synthesis of guided selector, not useful advantage.'}
 import sys
 if '--check' in sys.argv:
  expected=json.loads((root/'validation.json').read_text())
  for k,v in result.items():
   if isinstance(v,float):
    if abs(v-expected[k])>1e-12:raise RuntimeError(f'validation mismatch: {k}')
   elif v!=expected[k]:raise RuntimeError(f'validation mismatch: {k}')
 else:(root/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
