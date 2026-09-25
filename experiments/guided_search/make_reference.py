#!/usr/bin/env python3
"""Mathematical coefficients transcribed from a pinned public reference.
Not a newly discovered scheme. w_source is in transposed-output convention.
"""
import json
from pathlib import Path
U='''0 -1 -1 0 0 0 0 0 0
0 0 0 -1 1 0 0 -1 0
0 1 0 -1 0 0 0 0 0
-1 0 0 1 0 0 0 0 0
0 0 0 0 0 -1 0 0 0
0 0 0 0 -1 -1 0 1 1
0 0 0 0 0 0 0 0 -1
0 0 0 0 -1 -1 0 1 0
0 0 0 0 0 0 0 -1 0
0 1 0 0 0 1 0 0 0
-1 0 0 1 0 0 -1 0 -1
0 0 0 0 0 0 -1 0 0
1 0 1 -1 0 -1 1 0 1
-1 1 0 0 0 0 0 0 0
0 0 0 -1 0 0 0 0 0
1 0 0 -1 0 0 1 0 0
0 0 0 0 0 0 0 1 0
0 1 1 0 0 0 0 0 0
0 0 0 0 0 0 -1 0 -1
0 -1 0 0 0 0 0 0 0
0 -1 0 0 1 0 0 0 0
0 0 0 0 -1 -1 0 0 0
0 0 0 1 0 0 0 0 0'''
V='''0 0 0 0 0 0 0 -1 0
0 0 0 0 -1 0 0 1 0
1 1 -1 0 1 0 0 -1 0
-1 0 1 0 0 0 0 0 0
0 0 0 0 0 1 0 0 -1
0 0 0 0 0 0 0 1 0
0 0 -1 0 0 0 0 1 1
0 0 0 0 0 1 0 1 0
0 0 0 -1 0 0 0 0 0
0 0 0 0 0 -1 -1 0 1
0 0 1 0 0 0 -1 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 -1 0 0
1 1 -1 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0
1 0 0 0 0 0 -1 0 0
0 0 0 0 1 1 0 0 0
0 0 0 0 0 0 -1 0 1
0 0 1 0 0 0 0 0 0
-1 -1 1 -1 -1 1 1 1 -1
0 0 0 1 0 0 0 0 0
0 0 0 0 0 -1 0 0 0
0 1 0 0 1 0 0 -1 0'''
W='''0 0 0 1 0 0 0 0 0
0 0 0 0 -1 0 0 0 0
-1 -1 0 1 0 0 0 0 0
1 0 -1 -1 0 0 0 0 0
1 1 0 0 0 0 1 1 0
0 0 0 0 0 1 0 0 -1
0 0 0 0 0 0 0 0 -1
0 0 0 0 -1 -1 0 0 1
0 0 1 0 0 0 0 0 0
-1 -1 0 0 0 0 -1 0 0
-1 0 1 0 0 0 -1 0 0
0 0 0 0 0 -1 0 0 0
-1 0 0 0 0 0 -1 0 0
0 0 0 -1 0 0 0 0 0
-1 -1 0 0 0 0 -1 -1 0
0 0 1 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0
0 0 0 0 0 0 1 0 0
1 0 -1 0 0 0 1 0 -1
1 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 -1 -1 0 1 1
-1 -1 0 1 1 0 0 0 0'''
def data():
    u,v,w=([list(map(int,row.split())) for row in s.splitlines()] for s in (U,V,W))
    wout=[[row[3*j+i] for i in range(3) for j in range(3)] for row in w]
    terms=[tuple(sum((x%2)<<j for j,x in enumerate(row)) for row in rows) for rows in zip(u,v,wout)]
    return {'source_repository':'dronperminov/FastMatrixMultiplication','source_ref':'b28490ca14c884c339a9fc69a3bdcba1f6e2c5da','source_path':'schemes/known/a_60_addition/3x3x3_m23_additions60_ZT.json','source_blob_sha':'482609bcebe1fba1bec7e28e8158d9d7ff4312ff','note':'Coefficient transcription, not a byte-for-byte copy. Output factors transposed for row-major output. Known scheme; no new identity.','n':3,'U':u,'V':v,'W_row_major':wout,'terms_gf2':terms}
if __name__=='__main__':
 d=data()
 for i in range(9):
  for j in range(9):
   for k in range(9):
    x=sum(a[i]*b[j]*c[k] for a,b,c in zip(d['U'],d['V'],d['W_row_major']))
    want=int(i%3==j//3 and i//3==k//3 and j%3==k%3)
    if x!=want: raise RuntimeError((i,j,k,x,want))
 p=Path(__file__).parent
 (p/'reference23.json').write_text(json.dumps(d,indent=2)+'\n')
 (p/'reference23.txt').write_text('23\n'+'\n'.join(' '.join(map(str,t)) for t in d['terms_gf2'])+'\n')
 print('729 integer identities checked; binary scheme generated.')
