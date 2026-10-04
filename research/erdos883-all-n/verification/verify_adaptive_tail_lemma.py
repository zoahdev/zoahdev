"""Exact finite parameter check used in ADAPTIVE_SIGNATURE_REPAIR_LEMMA.txt."""
from fractions import Fraction
from math import isqrt
import time
start=time.process_time()
primes=[]
p=3
while len(primes)<900:
    if all(p%d for d in range(3,isqrt(p)+1,2)):
        primes.append(p)
    p+=2
best=(Fraction(1),None,None)
for s in range(6,511):
    cap=4**s
    product=1
    factor=Fraction(1)
    count=0
    stopped=False
    for p in primes[s:]:
        if product*p>cap:
            stopped=True
            break
        product*=p
        factor*=Fraction(p-1,p)
        count+=1
    assert stopped, 'Prime list insufficient for an exact maximal count'
    assert factor>=Fraction(9,10),(s,factor)
    if factor<best[0]:
        best=(factor,s,count)
assert best==(Fraction(396,437),6,2)
assert 16**5<81*(3*5*7*11*13)
print('PASS: every s=6..510 has worst permitted tail factor >=9/10')
print('Minimum exact factor:',best)
print('PASS: exact fourth-power inequality for common-neighbor discrepancy')
print('CPU seconds:',time.process_time()-start)
