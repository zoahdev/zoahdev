import sympy as s
x,z,d=s.symbols('x z d'); t=s.Rational(3,2)*(x-1)
V=(9*x*x-1)*(x+1)/16
C=s.prod((1-i*z)/(1-(i+t)*z) for i in range(3))
C=s.series(C,z,0,5).removeO().expand()

def avg(poly):
 return s.factor(sum(c*s.rf(s.Rational(1,2),m//2)/s.rf((d-1)/2,m//2) for (m,),c in s.Poly(s.expand(poly),x).terms() if m%2==0))
f=[avg(V*C.coeff(z,j)) for j in range(5)]
for j,q in enumerate(f): print('F',j,s.factor(q))
a=s.symbols('a1:5');D=10+sum(a[j-1]*z**j for j in range(1,5))
expr=s.series(sum(z**j*f[j].subs(d,D) for j in range(5)),z,0,5).removeO(); sol={}
for j in range(1,5):sol[a[j-1]]=s.solve(expr.coeff(z,j).subs(sol),a[j-1])[0]
print('d_n expansion coefficients:',sol)
