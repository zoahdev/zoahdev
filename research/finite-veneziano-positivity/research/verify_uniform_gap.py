#!/usr/bin/env python3
"""Exact fixed-polynomial certificate for the D=51/5 central-factorial gap.
Uses the established central-factorial/Bessel reduction, with kappa=c.
No mass-level or spin positivity scan is used as a proof.
"""
from pathlib import Path
import sympy as s,json,hashlib
j,l,p,r,R=s.symbols('j l p r R');X,Y,Q=s.symbols('X Y Q')
d=s.Rational(51,5);c=j+2*l+1;b=j+(d-1)/2;q=p+1-r
M=s.expand(c*((4*l+4-d)*r+j-2*l+d-4)-2*q*(2*q-1+2*c*r+d-4-4*l))
bulk=s.Poly(s.expand(M.subs({l:Y+Q+2+X,p:Y+Q+1,r:Y+2})),j,X,Y,Q)
assert all(v>0 for _,v in bulk.terms())
def MM(pp,rr):return M.subs({p:pp,r:rr})
def den(pp):return 2*pp*(2*j+2*pp+d-3)
def alpha(rr):return s.Rational(2**(2*rr-1),s.factorial(2*rr))
W=3;F=[s.Integer(1)]
for h in range(1,W):
 F.append(s.expand(sum(F[u]*alpha(h-u+1)*MM(l-u,h-u+1)*s.prod(den(l-v) for v in range(u+1,h)) for u in range(h))))
P=sum(F[u]*s.Rational(1,4**u)*s.prod(2*R+2-v for v in range(2*u))*MM(l-u,R-u+1)*s.prod(den(l-v) for v in range(u+1,W)) for u in range(W))
poly=s.Poly(s.expand(P.subs({R:X+W,l:X+Y+W})),j,X,Y)
scale,integerpoly=poly.clear_denoms()
content,primitive=integerpoly.primitive()
assert all(v>0 for _,v in primitive.terms())
assert primitive.eval({j:0,X:0,Y:0})>0
# Shallow trajectory identities, obtained by independent formal-series expansion.
z=s.symbols('z');shallow=[]
for ell in range(3):
 cc=j+2*ell+1;bb=j+(d-1)/2
 logseries=s.series(s.log(z/s.sinh(z)),z,0,2*ell+2).removeO()
 base=s.series(s.exp(cc*logseries),z,0,2*ell+2).removeO()
 phi=sum((cc*cc*z*z/4)**a/(s.rf(bb,a)*s.factorial(a)) for a in range(ell+1))
 h=s.factor(s.expand(base*phi).coeff(z,2*ell));shallow.append(str(h))
expected=[s.Integer(1),(j+3)*(5*j-1)/(12*(5*j+23)),(j+5)*(125*j**3+1275*j**2+3295*j+177)/(1440*(5*j+23)*(5*j+28))]
assert all(s.cancel(s.sympify(h)-e)==0 for h,e in zip(shallow,expected))
# Exact checks of the GF normalization against direct Gegenbauer decomposition.
# These are identity sanity checks; the proof uses the general coefficient identity.
x=s.symbols('x');identity_cases=[]
lam=(d-3)/2
for m in range(0,9):
 Wm=s.prod(s.Rational(m+1,2)*x-(a-s.Rational(m-1,2)) for a in range(m))/s.factorial(m)
 rem=s.expand(Wm)
 for spin in range(m,-1,-1):
  C=s.gegenbauer(spin,lam,x);coef=s.expand(rem).coeff(x,spin)/s.expand(C).coeff(x,spin);rem=s.expand(rem-coef*C)
  if (m-spin)%2:assert coef==0;continue
  ell=(m-spin)//2;cc=m+1;bb=spin+(d-1)/2
  logseries=s.series(s.log(z/s.sinh(z)),z,0,2*ell+2).removeO()
  base=s.series(s.exp(cc*logseries),z,0,2*ell+2).removeO()
  phi=sum((cc*cc*z*z/4)**a/(s.rf(bb,a)*s.factorial(a)) for a in range(ell+1))
  hh=s.expand(base*phi).coeff(z,2*ell)
  pref=s.Rational(1,2**(m+spin))*s.Rational(cc**spin,1)/s.rf(lam,spin)
  assert s.cancel(coef-pref*hh)==0,(m,spin,coef,pref*hh)
  identity_cases.append([m,spin])
terms=[{'powers':list(mon),'coefficient':str(co)} for mon,co in primitive.terms()]
out={'status':'PASS fixed polynomial and exact generating-function checks','dimension':'51/5','first_exit_width':3,
'bulk_terms':len(bulk.terms()),'exit_terms':len(terms),'exit_scaling':{'clear_denominators_multiplier':str(scale),'removed_integer_content':str(content)},
'exit_polynomial_variables':['j','R-3','ell-R'],'exit_total_degree':primitive.total_degree(),'exit_multidegree':list(primitive.degree_list()),
'exit_minimum_coefficient':str(min(primitive.coeffs())),'exit_constant':str(primitive.eval({j:0,X:0,Y:0})),
'shallow_h':shallow,'exception':'m=2,spin=0 only at dimension51/5','identity_cases':identity_cases,'exit_integer_polynomial_terms':terms,
'bulk_expression':str(bulk.as_expr())}
path=Path(__file__).with_name('uniform_gap_certificate.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['exit_integer_polynomial_terms','identity_cases']},indent=2))
print('identity checks',len(identity_cases),'SHA256',hashlib.sha256(path.read_bytes()).hexdigest())
