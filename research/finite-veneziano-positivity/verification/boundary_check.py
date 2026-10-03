from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json,time
import sys
sys.set_int_max_str_digits(0)
T=time.time()
S=json.load(open(Path(__file__).resolve().parent.parent/'research'/'uniform_base_certificates.json'))
def linear(cs,a,b):
 out=[F(0)]*(len(cs)+1)
 for i,c in enumerate(cs):out[i]+=b*c;out[i+1]+=a*c
 return out
def rational_residue(n,k):
 N=[F(1)];P=[F(1)]
 for i in range(1,k+1):N=linear(N,F(k,2),F(2*i-k,2))
 for r in range(n-k+1,n+1):P=linear(P,F(-k,2),F(2*r+k,2))
 N=[v*F(factorial(n),factorial(k)*factorial(n-k)) for v in N]
 return N,P
def series(n,k,M):
 N,P=rational_residue(n,k);a=[]
 for r in range(M+1):
  v=N[r] if r<len(N) else F(0)
  for q in range(1,min(r,len(P)-1)+1):v-=P[q]*a[r-q]
  a.append(v/P[0])
 return a
def moment(D,r):
 v=F(1)
 for h in range(r):v*=F(2*h+1)/(D+2*h-1)
 return v
def bounds(n,k,M,D,js):
 a=series(n,k,M);vals=[]
 for j in js:
  v=sum(a[j+2*r]*comb(j+2*r,j)*moment(D+2*j,r) for r in range((M-j)//2+1));assert v>0
  vals.append({'j':j,'lower':str(v)})
 return vals
rows=[]
for row in S['rows']:
 if (row['n'],row['k']) not in {(3,2),(30,30),(34,34),(34,5)}:continue
 n,k=row['n'],row['k'];M=row['certificate_degree'];L=row['last_negative_Taylor_degree'];D=F(row['D_cap'])
 vals=bounds(n,k,M,D,range(max(L,0)+1));rows.append({'n':n,'k':k,'M':M,'D':str(D),'checked_spins':len(vals),'minimum':str(min(F(v['lower']) for v in vals))})
 print('Pass adversarial base edge',n,k,flush=True)
# Obtain scalar cutoff from direct polynomial division, then rigorous tail majorant
# via rational pole evaluation rather than binomial partial-fraction formula.
N,P=rational_residue(35,3);a=series(35,3,160);D=F(51,5)
lo=sum(a[2*r]*moment(D,r) for r in range(81));tail=F(0)
for r in (33,34,35):
 z=1+F(2*r,3);deriv=sum(i*c*z**(i-1) for i,c in enumerate(P) if i);num=sum(c*z**i for i,c in enumerate(N));A=-num/deriv
 if A>0:tail+=A/z*z**(-162)/(1-z**(-2))
assert lo+tail<F(-3,100000)
# Scalar sign at D=14, n=3, independently using same pole evaluation tail bound.
N,P=rational_residue(3,3);a=series(3,3,160);hi14=sum(a[2*r]*moment(F(14),r) for r in range(81))
for r in (1,2,3):
 z=1+F(2*r,3);deriv=sum(i*c*z**(i-1) for i,c in enumerate(P) if i);num=sum(c*z**i for i,c in enumerate(N));A=-num/deriv
 if A>0:hi14+=A/z*z**(-162)/(1-z**(-2))
assert hi14<0
out={'selected_exact_base_checks':rows,'cutoff35_upper':str(lo+tail),'cutoff35_upper_float':float(lo+tail),'n3_D14_upper_float':float(hi14),'elapsed_seconds':time.time()-T}
Path(__file__).with_name('boundary_check.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS cutoff 35:',float(lo+tail),'and n3 D14:',float(hi14),flush=True)
