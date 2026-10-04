#!/usr/bin/env python3
"""Exact rational certificate for a limiting totient-Hall envelope.
This proves guarded uniform finite-prefix bounds for n >= 10^6.
It does not prove a finite-n or all-n graph result.
The conditioning argument adapts Della Pietra's prior totient-distribution method.
"""
from fractions import Fraction as Q
from math import isqrt, factorial
from time import process_time
start = process_time()

def primes_to(n):
    return [p for p in range(3,n+1,2)
            if all(p%d for d in range(3,isqrt(p)+1,2))]

def lambda_lower(p):
    return sum((Q(1,h*p**h) for h in range(1,13)), Q(0))

def lambda_upper(p):
    return lambda_lower(p)+Q(1,13*p**12*(p-1))

# The omitted prime tail is bounded by the sum over all integers > 2000:
# lambda_p/p <= 1/[p(p-1)], whose sum is 1/2000.
C1 = sum((lambda_upper(p)/p for p in primes_to(2000)), Q(1,2000))
assert C1 < Q(117,500)
small = [3,5,7,11]
delta = C1 - sum((lambda_lower(p)/p for p in small), Q(0))
assert delta < Q(47,2000)

# c_p=(p/(p-1))^6-1 <= 7/(p-1) for p>200, by the binomial theorem.
# Product tail <= exp(7/200) <= 1/(1-7/200).
C6 = Q(1)
for p in primes_to(200):
    C6 *= 1 + (Q(p,p-1)**6-1)/p
C6 *= Q(200,193)
assert C6 < 11

# Each state is (small-prime ratio a, limiting signature probability q).
states = [(Q(1),Q(1))]
for p in small:
    states = [(a,q*Q(p-1,p)) for a,q in states] + \
             [(a*Q(p-1,p),q/p) for a,q in states]
assert sum(q for a,q in states) == 1

def upper(t):
    # log(a/t)>=2(a-t)/(a+t), for a>t.
    first = sum((q if a<=t else q*min(Q(1),Q(47,2000)*(a+t)/(2*(a-t)))
                 for a,q in states), Q(0))
    return min(22*t**6,first)

# Guarded high branch: [1/3,3/4] includes both the needed endpoints
# and a common-neighbor-error guard beyond 20/27.
high_slacks=[]
for i in range(1000):
    left=Q(1,3)+Q(i,2400)
    right=left+Q(1,2400)
    slack=Q(9,10)*left-Q(1,6)-upper(right)
    assert slack>Q(29,1000), (i,float(slack))
    high_slacks.append(slack)

def sqrt_upper(x,scale=10**9):
    z=isqrt(x.numerator*scale**2//x.denominator)
    if z*z*x.denominator < x.numerator*scale**2:
        z+=1
    result=Q(z,scale)
    assert result**2>=x
    return result

low_slacks=[]
for i in range(100,2010):
    left,right=Q(i,1000),Q(i+1,1000)
    threshold=sqrt_upper((right+Q(3,100))/3)
    slack=left/3-upper(threshold)
    assert slack>Q(119,5000), (i,float(slack)) # .0238
    low_slacks.append(slack)

# Elementary exponential comparisons, with positive rational Taylor sums.
assert sum((Q(12**k,factorial(k)) for k in range(21)),Q(0)) > 10**5
assert sum((Q(49,4)**k/factorial(k) for k in range(21)),Q(0)) > 2*10**5
# E(n) <= (81000/47) log(n/10)/n, decreasing for these n.
E_1million=Q(81000,47)*12/10**6
E_2million=Q(81000,47)*Q(49,4)/(2*10**6)
assert Q(29,1000)-E_1million>Q(83,10000) # .0083
assert Q(119,5000)-E_2million>Q(33,2500) # .0132
# Small-t branch of the full original limiting envelope.
for c in [Q(87,100),Q(9,10)]:
    assert 44*(1/(3*c))**5<c

print('C1 upper bound:',float(C1))
print('Tail first moment upper bound:',float(delta),' < .0235')
print('C6 upper bound:',float(C6),' < 11')
print('All 1000 guarded high-branch cells pass; minimum slack:',float(min(high_slacks)))
print('All 1910 low-rank beta cells pass; minimum slack:',float(min(low_slacks)))
print('Uniform CDF error for every n >= 10^6:',float(E_1million))
print('Uniform CDF error for every n >= 2*10^6:',float(E_2million))
print('G_n(t) < .9*t - 1/6 - .0083 for n >= 10^6 and 1/3 <= t <= 3/4')
print('G_n(sqrt((beta+.03)/3)) < beta/3 - .0132 for n >= 2*10^6 and .1 <= beta <= 2.01')
print('Here G_n(t)=(2/n)*#{odd v<=n: phi(v)/v<t}')
print('No finite-n or all-n graph assertion is made')
print('CPU seconds:',process_time()-start)
