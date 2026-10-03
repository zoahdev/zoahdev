from pathlib import Path
from fractions import Fraction
import sympy as s
import json,time
start=time.time()
j,l,p,r,q,D,c,b,R,X,Y,Q=s.symbols('j l p r q D c b R X Y Q')
# Derive the kernel from G''+(2b-1)G'/z-c^2G=0 after G=(sinh(z)/z)^c H.
# Off-diagonal coefficient of z^(2p+2) in the conjugated ODE,
# divided by alpha_r, with q=p+1-r.
M_ode=-(2*q*(2*q-1)+4*c*q*r+2*q*(2*b-1-2*c)+c*(2*b-1-2*c)*r+c*(c+2-2*b))
M=s.expand(M_ode.subs({c:j+2*l+1,b:j+(D-1)/2,q:p+1-r}))
claimed=(j+2*l+1)*((4*l+4-D)*r+j-2*l+D-4)-2*(p+1-r)*(2*(p+1-r)-1+2*(j+2*l+1)*r+D-4-4*l)
assert s.expand(M-claimed)==0
# Leading coefficient from the ODE must equal the claimed positive denominator.
lead=s.expand(2*p*(2*p-1)+2*p*(2*b-1)+c*(c-1)+c*(2*b-1-2*c)+c*(c+2-2*b))
assert s.expand(lead-2*p*(2*p+2*b-2))==0
D0=s.Rational(51,5)
M=M.subs(D,D0)
# Bulk: p>=1, 2<=r<=p+1, p<=ell-1.
bulk=s.Poly(s.expand(M.subs({l:2+X+Y+Q,p:1+Y+Q,r:2+Y})),j,X,Y,Q)
assert all(v>0 for v in bulk.coeffs())
# First exit from the depths 0,1,2, explicitly enumerating four possible path types.
def mm(pp,rr):return M.subs({p:pp,r:rr})
def dd(pp):return 2*pp*(2*j+2*pp+D0-3)
a2=s.Rational(1,3);a3=s.Rational(2,45)
ratio1=(2*R+2)*(2*R+1)/4
ratio2=(2*R+2)*(2*R+1)*(2*R)*(2*R-1)/16
P0=mm(l,R+1)*dd(l-1)*dd(l-2)
P1=a2*mm(l,2)*ratio1*mm(l-1,R)*dd(l-2)
P02=a3*mm(l,3)*dd(l-1)*ratio2*mm(l-2,R-1)
P012=a2*a2*mm(l,2)*mm(l-1,2)*ratio2*mm(l-2,R-1)
poly=s.Poly(s.expand((P0+P1+P02+P012).subs({R:X+3,l:X+Y+3})),j,X,Y)
assert len(poly.terms())==182 and all(v>0 for v in poly.coeffs())
source=s.sympify((Path(__file__).resolve().parent.parent/'research'/'positive_exit_polynomial.txt').read_text(),locals={'j':j,'X':X,'Y':Y})
assert s.expand(source-poly.as_expr())==0
# The first-exit identity is also checked using generic numerical integer indices
# and direct path recursion, independent of the symbolic common-denominator layout.
def aa(rr):return s.Rational(2**(2*rr-1),s.factorial(2*rr))
for jj,ll in [(0,3),(1,3),(0,4),(3,7),(0,12),(10,20)]:
 def C(depth,step):
  pp=ll-depth
  return aa(step+1)*mm(pp,step+1).subs({j:jj,l:ll})/dd(pp).subs(j,jj)
 paths={0:s.Integer(1)}
 for depth in [1,2]: paths[depth]=sum(paths[u]*C(u,depth-u) for u in range(depth))
 for RR in range(3,ll+1):
  E=sum(paths[u]*C(u,RR-u) for u in range(3))
  rhs=aa(RR+1)*poly.as_expr().subs({j:jj,X:RR-3,Y:ll-RR})
  rhs/=s.prod(dd(ll-u).subs(j,jj) for u in range(3))
  assert s.factor(E-rhs)==0 and E>0
# Shallow values independently obtained through recurrence, not copied from source.
h1=s.factor(mm(1,2).subs(l,1)/(3*dd(1)))
h2=s.factor((aa(2)*mm(2,2).subs(l,2)*(aa(2)*mm(1,2).subs(l,2)/dd(1))+aa(3)*mm(2,3).subs(l,2))/dd(2))
assert s.factor(h1-(j+3)*(5*j-1)/(12*(5*j+23)))==0
assert s.factor(h2-(j+5)*(125*j**3+1275*j**2+3295*j+177)/(1440*(5*j+23)*(5*j+28)))==0
# Direct finite central-factorial polynomials versus coefficient reconstruction.
x,z=s.symbols('x z');lam=(D0-3)/2
checks=[]
for m in range(31):
 cp=s.prod(s.Rational(m+1,2)*x+s.Rational(2*i-m-1,2) for i in range(1,m+1))/s.factorial(m)
 rem=s.Poly(cp,x)
 for jj in range(m,-1,-2):
  cg=s.Poly(s.gegenbauer(jj,lam,x),x)
  direct=s.factor(rem.coeff_monomial(x**jj)/cg.coeff_monomial(x**jj))
  rem=s.Poly(rem.as_expr()-direct*cg.as_expr(),x)
  ll=(m-jj)//2;hs=[s.Integer(1)]
  for pp in range(1,ll+1):
   h=sum(aa(rr)*mm(pp,rr).subs({j:jj,l:ll})*hs[pp+1-rr] for rr in range(2,pp+2))/dd(pp).subs(j,jj)
   hs.append(s.factor(h))
  pref=s.Rational((m+1)**jj,2**(m+jj))/s.rf(lam,jj)
  assert s.factor(direct-pref*hs[ll])==0,(m,jj)
  assert direct>0 or (m==2 and jj==0)
  checks.append([m,jj,str(direct)])
 assert rem.is_zero
 print('direct central polynomial checked m',m,flush=True)
# Independent direct formal generating-series check at selected pairs.
for jj,ll in [(0,0),(0,1),(1,1),(0,2),(0,3),(1,3),(0,4),(2,4),(0,6)]:
 cc=jj+2*ll+1;bb=jj+(D0-1)/2
 base=s.series((z/s.sinh(z))**cc,z,0,2*ll+1).removeO()
 phi=sum((cc*cc*z*z/4)**u/(s.factorial(u)*s.rf(bb,u)) for u in range(ll+1))
 direct=s.expand(base*phi).coeff(z,2*ll)
 hs=[s.Integer(1)]
 for pp in range(1,ll+1):
  hs.append(s.factor(sum(aa(rr)*mm(pp,rr).subs({j:jj,l:ll})*hs[pp+1-rr] for rr in range(2,pp+2))/dd(pp).subs(j,jj)))
 assert s.factor(direct-hs[ll])==0
lcm=s.ilcm(*[v.q for v in poly.coeffs()])
out={'status':'PASS recurrence, bulk, first-exit identity, shallow exceptions and independent direct central-factorial projections',
'D':'51/5','bulk_terms':len(bulk.terms()),'bulk_polynomial':str(bulk.as_expr()),'exit_terms':len(poly.terms()),'exit_denominator_lcm':int(lcm),'exit_min_integer_coefficient':str(min(v*lcm for v in poly.coeffs())),
'exit_polynomial':str(poly.as_expr()),'h1':str(h1),'h2':str(h2),'direct_projection_checks':checks,'num_direct_projections':len(checks),'elapsed_seconds':time.time()-start}
Path(__file__).with_name('independent_uniform_check.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(checks),'direct Gegenbauer projections;182 strictly positive exit polynomial terms;20 positive bulk terms; elapsed',time.time()-start)
