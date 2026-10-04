from fractions import Fraction as Q
N=2_000_000;m=N//6
assert 1415**2>N
assert Q(9*1415+12,N-5)<Q(65,10000)
assert Q(12*1415+6,N-5)<Q(86,10000)
assert 3+Q(5,2*m)<Q(3000008,1000000)
assert 22*(3+Q(3,m))<Q(66001,1000)
assert Q(66001,1000)/Q(27,10)**6<Q(171,1000)
for y in [Q(1,50),Q(1)]:assert Q(342,1000)*y**6-y+Q(151,10000)<0
assert Q(6500,1000000)+Q(4300,1000000)+Q(8,1000000)<Q(249,10000)
assert Q(66001,1000)*Q(105,300)**3<Q(284,100)
assert Q(568,100)*Q(12,100)**2<1
assert Q(4544,100)*Q(2,100)**2<1
assert Q(8,3)**15>N
assert Q(N-1,21000)>Q(63,2)
for n in range(6,10000):
 q,r=divmod(n,6);f=n//2+n//3-n//6
 assert n-f+q==3*q+[0,1,1,1,1,2][r]
 assert (n+1)//2-(n//3-n//6+1)==2*q+[-1,0,0,0,0,1][r]
 assert n//3-n//6+1>=q+1
print('PASS: exact rational analytic guards; floor identities independently checked for n=6..9999, and algebraically by six residue classes in the audit.')
