from fractions import Fraction as F
from math import prod,isqrt,factorial,gcd
from pathlib import Path
import time
start=time.process_time()
# Trial division for all candidates, rather than the producer's odd-only sieve.
def prime(p):return p>1 and all(p%d for d in range(2,isqrt(p)+1))
ps=[p for p in range(3,10000) if prime(p)]
# Independently strengthen the tail constants using larger truncation points.
k=10
lam=lambda p: sum((F(1,h*p**h) for h in range(1,k+1)),F())
upper=lambda p: lam(p)+F(1,(k+1)*p**k*(p-1))
delta=sum((upper(p)/p for p in ps if 11<p<=3000),F(1,3000))
assert delta<F(47,2000)
c6=prod(1+(F(p,p-1)**6-1)/p for p in ps if p<=500)*F(500,493)
assert c6<11
assert (F(201,200)**6-1)*200<7
# Enumerate residue classes modulo 1155 to recover the signature masses.
small=[3,5,7,11];P=prod(small);mass={}
for v in range(P):
 a=prod(F(p-1,p) for p in small if v%p==0)
 mass[a]=mass.get(a,0)+1
states=[(a,F(c,P)) for a,c in mass.items()]
assert len(states)==16 and sum(q for a,q in states)==1
D=F(47,2000)
def envelope(t):
 return min(22*t**6,sum((q if a<=t else q*min(F(1),D*(a+t)/(2*(a-t))) for a,q in states)))
# Twice as many cells as the producer, to audit the continuum bounds independently.
high=[]
for i in range(2000):
 l=F(1,3)+F(i,4800);r=l+F(1,4800)
 high.append(F(9,10)*l-F(1,6)-envelope(r))
assert min(high)>F(29,1000)
low=[]
for i in range(200,4020):
 l=F(i,2000);r=l+F(1,2000);x=(r+F(3,100))/3
 a=isqrt((x.numerator*10**20)//x.denominator)
 while F(a*a,10**20)<x:a+=1
 assert F(a*a,10**20)>=x
 low.append(l/3-envelope(F(a,10**10)))
assert min(low)>F(119,5000)
for x,y in [(F(12),10**5),(F(49,4),2*10**5)]:
 assert sum(x**i/factorial(i) for i in range(25))>y
assert F(29,1000)-F(81000,47)*12/10**6>F(83,10000)
assert F(119,5000)-F(81000,47)*F(49,4)/(2*10**6)>F(33,2500)
# Adaptive tail check with independent generated primes and exact prime product.
best=F(1)
for s in range(6,511):
 x=1;y=F(1);i=s
 while x*ps[i]<=4**s:
  x*=ps[i];y*=F(ps[i]-1,ps[i]);i+=1
 assert y>=F(9,10)
 best=min(best,y)
assert best==F(396,437)
assert 16**5<81*prod([3,5,7,11,13])
print('Independent PASS: delta <',float(delta),'; C6 <',float(c6))
print('Independent PASS: 2000 high cells, minimum slack',float(min(high)))
print('Independent PASS: 3820 low cells, minimum slack',float(min(low)))
print('Independent PASS: tail factors s=6..510, minimum',best)
print('CPU',time.process_time()-start)
