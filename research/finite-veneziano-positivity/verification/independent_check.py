from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s
import mpmath as mp
mp.mp.dps=75
x,z,D=s.symbols('x z D')
V=(9*x*x-1)*(x+1)/16
# Independent logarithmic expansion of finite truncation correction.
t=s.Rational(3,2)*(x-1)
L1=sum(t for i in range(3))
L2=sum(((i+t)**2-i*i)/2 for i in range(3))
C1=L1; C2=s.expand(L2+L1*L1/2)
def avg(p):
 return s.factor(sum(c*s.rf(s.Rational(1,2),m[0]//2)/s.rf((D-1)/2,m[0]//2) for m,c in s.Poly(s.expand(p),x).terms() if m[0]%2==0))
F0,F1,F2=[avg(V*c) for c in [1,C1,C2]]
c1=s.simplify(-F1.subs(D,10)/s.diff(F0,D).subs(D,10))
c2=s.simplify(-(F2.subs(D,10)+c1*s.diff(F1,D).subs(D,10)+c1*c1*s.diff(F0,D,2).subs(D,10)/2)/s.diff(F0,D).subs(D,10))
assert c1==s.Rational(72,11) and c2==s.Rational(13032,1331)
# Root interval independently checked by exact rational moment series,
# with a different global tail bound on Taylor coefficients.
S=F(143,105)
q=[F(1,3),F(3,7),F(3,5)]
K=F(1,105)
J=120
h=[F(0)]*(2*J+3);h[0]=1
for qi in q:
 for m in range(1,len(h)):h[m]+=qi*h[m-1]
b=[h[m]+(h[m-1] if m else 0) for m in range(len(h))]
a=[K*((9*b[m-2] if m>=2 else 0)-b[m]) for m in range(len(h))]
assert a[0]<0 and a[1]<0 and all(c>0 for c in a[2:])
# For m>=2, a_m <=9 K b_(m-2); b_m is bounded by
# binom(m+2,2)(3/5)^m + binom(m+1,2)(3/5)^(m-1).
# Instead obtain exact total even tail at x=1 from rational evaluations.
def moments(d):
 ms=[F(1)]
 for r in range(J): ms.append(ms[-1]*F(2*r+1)/(d+2*r-1))
 return ms
R=lambda xx: -(9*xx*xx-1)*(xx+1)/((xx-3)*(3*xx-7)*(3*xx-5))
total_even=(R(F(1))+R(F(-1)))/2
tail=total_even-sum(a[2*r] for r in range(J+1))
assert tail>0
lo=F('13.15983426171950364948847935837366808'); hi=F('13.15983426171950364948847935837366809')
def interval(d):
 ms=moments(d); subtotal=sum(a[2*r]*ms[r] for r in range(J+1))
 return subtotal,subtotal+tail*ms[-1]
loi,hii=interval(lo),interval(hi)
assert loi[0]>0 and hii[1]<0
# Independent integral calculations for multiple finite truncations and spin projections.
def residue(n,k,xx):
 tt=mp.mpf(k)/2*(xx-1)
 return mp.fprod(tt+i for i in range(1,k+1))/mp.factorial(k)*mp.fprod(mp.mpf(n-i)/(n-i-tt) for i in range(k))
def scalar(n,d):
 return mp.quad(lambda xx:(1-xx*xx)**((d-4)/2)*residue(n,3,xx),[-1,0,1])/mp.beta(mp.mpf('.5'),(d-2)/2)
roots=[]
for n in [3,4,8,16,32,100,1000]:
 root=mp.findroot(lambda d:scalar(n,d),(10,14))
 approx=10+mp.mpf(72)/(11*n)+mp.mpf(13032)/(1331*n*n)
 roots.append({'n':n,'root':str(root),'scaled_remainder_n3':str((root-approx)*n**3)})
assert all(mp.mpf(roots[i]['root'])>mp.mpf(roots[i+1]['root']) for i in range(len(roots)-1))
projections=[]
for n,d in [(3,mp.mpf(13)),(3,mp.mpf(14)),(8,mp.mpf(10))]:
 for k in ([1,2,3] if n==3 else [3]):
  for j in [0,1,2,3,4,8,16,32]:
   lam=(d-3)/2
   val=mp.quad(lambda xx:(1-xx*xx)**((d-4)/2)*mp.gegenbauer(j,lam,xx)*residue(n,k,xx),[-1,0,1])/mp.beta(mp.mpf('.5'),(d-2)/2)
   assert val>0 or (n==3 and d==14 and k==3 and j==0)
   projections.append({'n':n,'D':str(d),'k':k,'spin':j,'projection':str(val)})
out={'symbolic_asymptotic_terms':list(map(str,[F0,F1,F2,c1,c2])),
'root_bracket':[str(lo),str(hi)],'root_bracket_signs':[str(float(loi[0])),str(float(hii[1]))],
'independent_roots':roots,'independent_spin_projections':projections}
Path(__file__).with_name('independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='independent_spin_projections'},indent=2))
print('PASSED',len(projections),'independent Gegenbauer projections; proof is analytic, not this finite scan')
