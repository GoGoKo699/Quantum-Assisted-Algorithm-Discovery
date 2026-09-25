"""Classical eager target closure for the explicit bounded shifted-add model."""
from mcm_smt import odd

def options(a,b,B):
    for s in range(B+1):
        for sign in (1,-1):
            n=abs((a<<s)+sign*b)
            if n<=0:continue
            t=(n&-n).bit_length()-1;c=n>>t
            if c<(1<<B):yield c,s,t,sign

def close(targets,B):
    targets=set(map(odd,targets))-{0,1};values=[1];steps=[]
    while True:
        found=None
        for i,a in enumerate(values):
            for j,b in enumerate(values):
                for c,s,t,sign in options(a,b,B):
                    if c in targets-set(values):found=(c,i,j,s,t,sign);break
                if found:break
            if found:break
        if found is None:break
        c,i,j,s,t,sign=found;values.append(c);steps.append({'value':c,'left':i,'right':j,'left_shift':s,'right_shift':t,'sign':sign,'output_sign':1 if (values[i]<<s)+sign*values[j]>0 else -1})
    return steps,sorted(targets-set(values))

