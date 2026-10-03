"""Cold adversarial exact checks. No sympy or candidate/auditor module imports."""
from fractions import Fraction as F
from collections import defaultdict
from math import factorial, comb
from pathlib import Path
import json, time
T=time.time();N=4;Z=(0,)*N
class Poly:
 def __init__(self,x=0):
  self.d=x if isinstance(x,dict) else ({Z:F(x)} if x else {})
 def __add__(self,x):
  x=P(x); d=self.d.copy()
  for e,c in x.d.items():d[e]=d.get(e,F(0))+c
  return Poly({e:c for e,c in d.items() if c})
 __radd__=__add__
 def __neg__(self):return Poly({e:-c for e,c in self.d.items()})
 def __sub__(self,x):return self+-P(x)
 def __rsub__(self,x):return P(x)+-self
 def __mul__(self,x):
  x=P(x); d=defaultdict(F)
  for e,c in self.d.items():
   for f,b in x.d.items():d[tuple(a+z for a,z in zip(e,f))]+=c*b
  return Poly({e:c for e,c in d.items() if c})
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0;r=Poly(1)
  for _ in range(n):r=r*self
  return r
 def __truediv__(self,n):return self*F(1,n)
def P(x):return x if isinstance(x,Poly) else Poly(x)
def var(i):return Poly({tuple(int(i==k) for k in range(N)):F(1)})
j,X,Y,Q=map(var,range(N)); D=F(51,5)
# Conjugated hypergeometric ODE: H'' + [2c coth(z)+(2b-1-2c)/z] H'
# + [c(c-1)csch(z)^2 + c(2b-1-2c)coth(z)/z + c(c+2-2b)/z^2]H=0.
# Multiply by z^2 sinh(z)^2 and obtain off-diagonal coefficients directly.
def kernel(l,p,r):
 c=j+2*l+1;b=j+(D-1)/2;q=p+1-r;B=2*b-1-2*c
 return -(2*q*(2*q-1)+4*c*q*r+2*q*B+c*B*r+c*(c+2-2*b))
def delta(p):return 2*p*(2*j+2*p+D-3)
bulk=kernel(X+Y+Q+2,Y+Q+1,Y+2)
assert len(bulk.d)==20 and all(v>0 for v in bulk.d.values())
l=X+Y+3;R=X+3
# Four paths: (0,R), (0,1,R), (0,2,R), (0,1,2,R).
ratio1=(2*R+2)*(2*R+1)/4
ratio2=ratio1*(2*R)*(2*R-1)/4
m=lambda u,step:kernel(l,l-u,step+1)
a=F(1,3);bb=F(2,45)
e=(m(0,R)*delta(l-1)*delta(l-2)
 +a*m(0,1)*ratio1*m(1,R-1)*delta(l-2)
 +bb*m(0,2)*delta(l-1)*ratio2*m(2,R-2)
 +a*a*m(0,1)*m(1,1)*ratio2*m(2,R-2))*22500
assert len(e.d)==182 and all(v.denominator==1 and v>0 for v in e.d.values())
source=json.load(open(Path(__file__).resolve().parent.parent/'research'/'uniform_gap_certificate.json'))
reported={tuple(row['powers'])+(0,):F(row['coefficient']) for row in source['exit_integer_polynomial_terms']}
assert reported==e.d
print('No-CAS exact dictionary reconstruction: 20 positive bulk terms and 182 positive exit terms match.',flush=True)
# Independent direct W_m -> Gegenbauer triangular decomposition.
# No use of Bessel transform, recurrence h_p, or certificate polynomial.
def mul_linear(cs,a,b):
 out=[F(0)]*(len(cs)+1)
 for i,c in enumerate(cs):out[i]+=b*c;out[i+1]+=a*c
 return out
def add(cs,ds):
 out=[F(0)]*max(len(cs),len(ds))
 for i,c in enumerate(cs):out[i]+=c
 for i,c in enumerate(ds):out[i]+=c
 return out
lam=F(18,5);G=[[F(1)],[F(0),2*lam]]
for n in range(1,100):
 x=mul_linear(G[-1],2*(n+lam)/(n+1),0)
 y=[-F(n+2*lam-1,n+1)*c for c in G[-2]]
 G.append(add(x,y))
rows=[]
for m in (0,1,2,3,4,31,32,49,64,80,100):
 poly=[F(1)]
 for aidx in range(m):poly=mul_linear(poly,F(m+1,2),F(m-1,2)-aidx)
 poly=[c/factorial(m) for c in poly]
 coeff=[]
 for spin in range(m,-1,-2):
  a=poly[spin]/G[spin][spin];coeff.append((spin,a))
  for k,c in enumerate(G[spin]):poly[k]-=a*c
  assert a>0 or (m==2 and spin==0 and a<0),(m,spin,a)
 assert all(c==0 for c in poly)
 rows.append({'m':m,'coefficients_checked':len(coeff),'minimum':str(min(a for _,a in coeff))})
 print('Direct polynomial checked',m,len(coeff),flush=True)
output={'status':'NO_COUNTEREXAMPLE_IN_CHECKED_DOMAINS','sympy_used':False,'bulk_terms':len(bulk.d),'exit_terms':len(e.d),'all_182_coefficients_match':True,'minimum_exit_integer':str(min(e.d.values())),'constant_exit_integer':str(e.d[Z]),'direct_polynomial_checks':rows,'elapsed_seconds':time.time()-T}
Path(__file__).with_name('cold_check.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2),flush=True)
