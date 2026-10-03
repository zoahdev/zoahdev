from fractions import Fraction as Q
import sys,json
from pathlib import Path
sys.dont_write_bytecode=True
# Exact coefficient formulas; no frozen deliverable is modified.
from certify_uniform_base import partialfractions,coefficients,moments
out=[]
for n,d in [(3,13),(3,14),(4,12),(4,13),(5,12),(7,11),(8,11)]:
 d=Q(d);J=100;_,pf=partialfractions(n,3);a=coefficients(n,3,2*J);ms=moments(d,J)
 lo=sum(a[2*j]*ms[j] for j in range(J+1))
 tail=sum(A*q*(q*q)**(J+1)/(1-q*q) for A,q in pf if A>0)
 hi=lo+tail
 assert lo>0 or hi<0
 out.append({'n':n,'D':str(d),'sign':1 if lo>0 else -1,'lower':float(lo),'upper':float(hi)})
Path(__file__).with_name('integer_dimension_corollary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
