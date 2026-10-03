#!/usr/bin/env python3
"""Exact rational certificates and independent high-precision checks.
No finite spin scan is used as an all-spin proof. See level3_theorem.md.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s
import mpmath as mp
mp.mp.dps=90

def moment(j,d):
    z=Q(1)
    for k in range(j): z*=Q(2*k+1)/(d+2*k-1)
    return z

def coef(m):
    return (Q(-1) if m==0 else 0)+Q(24,5)*Q(3,5)**m-Q(120,7)*Q(3,7)**m+Q(40,3)*Q(1,3)**m

def scalar_interval(d,J=100):
    # All omitted a_(2j) are strictly positive by the analytic lemma.
    low=sum(coef(2*j)*moment(j,d) for j in range(J+1))
    # Drop the negative partial-fraction contribution and use 0<M_j<=1.
    tail=Q(24,5)*Q(9,25)**(J+1)/(1-Q(9,25))+Q(40,3)*Q(1,9)**(J+1)/(1-Q(1,9))
    return low,low+tail

def dec(q): return mp.nstr(mp.mpf(q.numerator)/q.denominator,55)

def f(d):
    return -1+mp.mpf(24)/5*mp.hyp2f1(1,mp.mpf('.5'),(d-1)/2,mp.mpf(9)/25)-mp.mpf(120)/7*mp.hyp2f1(1,mp.mpf('.5'),(d-1)/2,mp.mpf(9)/49)+mp.mpf(40)/3*mp.hyp2f1(1,mp.mpf('.5'),(d-1)/2,mp.mpf(1)/9)
root=mp.findroot(f,(13,14))
lo=Q(str(mp.floor(root*10**35)/10**35)); hi=lo+Q(1,10**35)
L=scalar_interval(lo);H=scalar_interval(hi)
assert L[0]>0 and H[1]<0
F10=scalar_interval(Q(10));F14=scalar_interval(Q(14));assert F10[0]>0 and F14[1]<0
x,ss,tt=s.symbols('x ss tt')
A=-(ss+tt)/(ss*tt)*s.prod(i*(i-ss-tt)/((i-ss)*(i-tt)) for i in range(1,4))
for k in range(1,4):
    direct=s.cancel(s.limit(-(ss-k)*A,ss,k)).subs(tt,s.Rational(k,2)*(x-1))
    t=s.Rational(k,2)*(x-1)
    formula=s.prod(t+j for j in range(1,k+1))/s.factorial(k)*s.prod(s.Rational(3-j)/(3-j-t) for j in range(k))
    assert s.cancel(direct-formula)==0
R3=-(9*x*x-1)*(x+1)/((x-3)*(3*x-7)*(3*x-5))
assert s.cancel(R3-(-1+24/(5-3*x)-120/(7-3*x)+40/(3-x)))==0
S=Q(143,105)
assert S*S<4 and S*S+S<9
# Independent beta-weight quadrature. The normalized scalar is the expectation.
checks=[]
for d in [mp.mpf(4),mp.mpf(10),root,mp.mpf(14),mp.mpf(20)]:
    def r(y):return -(9*y*y-1)*(y+1)/((y-3)*(3*y-7)*(3*y-5))
    v=mp.quad(lambda y:(1-y*y)**((d-4)/2)*r(y),[-1,0,1])/mp.beta(mp.mpf('.5'),(d-2)/2)
    assert abs(v-f(d))<mp.mpf('1e-75')
    checks.append({'D':mp.nstr(d,45),'scalar':mp.nstr(v,45)})
out={'status':'analytic all-spin theorem at n=3; all-n level-three theorem; not an all-n full-amplitude proof',
'critical_dimension_n3':mp.nstr(root,70),'certified_bracket': [str(lo),str(hi)],
'bracket_decimal':[dec(lo),dec(hi)],'lower_endpoint_scalar_interval':[dec(z) for z in L],
'upper_endpoint_scalar_interval':[dec(z) for z in H],
'D10_scalar_interval':[dec(z) for z in F10],'D14_scalar_interval':[dec(z) for z in F14],
'certificate_arithmetic':'Python fractions.Fraction, exact rationals; tail bound geometric',
'certificate_terms_even':101,'independent_quadrature':checks,
'level3_root_asymptotic':['10','72/(11*n)','13032/(1331*n^2)','O(n^-3)']}
Path(__file__).with_name('level3_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
