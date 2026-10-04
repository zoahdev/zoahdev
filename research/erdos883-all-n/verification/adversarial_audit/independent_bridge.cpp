#include <bits/stdc++.h>
using namespace std;
using I=__int128_t;
struct MaxTree {
 int n; vector<int> t;
 MaxTree(const vector<int>& a):n(a.size()),t(2*n) { copy(a.begin(),a.end(),t.begin()+n); for(int i=n-1;i;i--)t[i]=max(t[i*2],t[i*2+1]); }
 int get(int l,int r) { int v=INT_MIN; for(l+=n,r+=n;l<=r;l/=2,r/=2) { if(l&1)v=max(v,t[l++]); if(!(r&1))v=max(v,t[r--]); } return v; }
};
int main(int argc,char**argv) {
 ifstream in(argv[1]); string word; int L,U,claim; vector<array<int,3>> intervals;
 while(in>>word>>L>>U>>claim) { assert(word=="PASS"); intervals.push_back({L,U,claim}); }
 assert(intervals.size()==84 && intervals.front()[0]==2301 && intervals.back()[1]==2000000);
 int N=2000000; vector<int> spf(N+1),phi(N+1); vector<int> primes;
 phi[1]=1;
 for(int v=2;v<=N;v++) { if(!spf[v]) {spf[v]=v;primes.push_back(v);} int p=spf[v],u=v/p;phi[v]=(u%p==0)?phi[u]*p:phi[u]*(p-1); for(int q:primes) {if(q>spf[v] || (long long)v*q>N)break; spf[v*q]=q;} }
 vector<int> oddprimes(primes.begin()+1,primes.end()); long long ranks=0,queries=0;
 for(int t=0;t<int(intervals.size());t++) {
  auto [L,U,claim]=intervals[t]; if(t)assert(L==intervals[t-1][1]+1);
  const int J=U/6, F=U/2+U/3-U/6, B=(U+1)/2-(U/3-U/6+1), D=U-F+J;
  I prod=1;int omega=0;for(int p:oddprimes) {if(prod*p>I(U)*U)break;prod*=p;omega++;}
  int loss=(1<<(omega-1))-1;vector<bool> passed(J+1,false);
  for(int s=0;s<=claim;s++) {
   int h=s?(1<<s)+1:0; if(h>=J)continue;
   I num=1,den=1;for(int idx=s;;idx++){int p=oddprimes.at(idx);if(den*p>U)break;num*=p-1;den*=p;}
   // Compute both integer bounds independently, then take the maximum.
   vector<int> ec(B+J+1),rc(D+J+1);
   for(int v=1;v<=U;v+=2) {
    int pe=max(int(I(L/2)*phi[v]*phi[v]/(I(v)*v)),int(I(L/2)*num*phi[v]/(den*v)))-loss;
    int pr=max(int(I(L)*phi[v]*phi[v]/(I(v)*v)),int(I(L)*num*phi[v]/(den*v)))-loss;
    if(pe<B+J)ec[max(0,pe+1)]++;
    if(pr<D+J)rc[max(0,pr+1)]++;
   }
   partial_sum(ec.begin(),ec.end(),ec.begin());partial_sum(rc.begin(),rc.end(),rc.begin());
   vector<int> adjusted(ec.size());for(int z=0;z<int(ec.size());z++)adjusted[z]=ec[z]-z;
   MaxTree tree(adjusted);
   for(int j=h+1;j<=J;j++) {
    if(passed[j])continue;
    int a=(j-h-1)/2, largest_bad_whole=min(B,rc[D+j]-a-1);
    bool success=largest_bad_whole<0 || tree.get(j,j+largest_bad_whole)<=a-j;
    queries++;if(success)passed[j]=true;
   }
  }
  for(int j=1;j<=J;j++)if(!passed[j]) {cerr<<"FAIL "<<L<<" "<<U<<" "<<j<<"\n";return 1;}
  ranks+=J;cout<<"INDEPENDENT_PASS "<<L<<" "<<U<<"\n";
 }
 cout<<"PASS 84 intervals; every Hall rank verified, with one prefix covering all b per rank. ranks="<<ranks<<" RMQ_queries="<<queries<<"\n";
}
