#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using i64=int64_t;using i128=__int128_t;
struct Result{int failures,first,last,max_s;};
vector<int> primes(){vector<bool>a(1001,true);a[0]=a[1]=false;for(int p=2;p*p<=1000;p++)if(a[p])for(int j=p*p;j<=1000;j+=p)a[j]=false;vector<int>p;for(int i=3;i<=1000;i+=2)if(a[i])p.push_back(i);return p;}
vector<int> phi_sieve(int N){vector<int>a(N+1);iota(a.begin(),a.end(),0);for(int p=2;p<=N;p++)if(a[p]==p)for(int j=p;j<=N;j+=p)a[j]-=a[j]/p;return a;}
Result certify(int L,int U,const vector<int>&ph,const vector<int>&ps){
 assert(6<=L&&L<=U&&int(ph.size())>U);
 int m=U/6,H=(U+1)/2,f=U/2+U/3-U/6,M=f-U/2+1,bmax=H-M,D=U-f+m;
 i64 pp=1;int r=0;bool terminated=false;
 for(int p:ps){if(p>i64(U)*U/pp){terminated=true;break;}pp*=p;r++;}assert(terminated&&r>0&&r<31);
 int loss=(1<<(r-1))-1;vector<unsigned char>covered(m+1,0);int remaining=m,max_s=-1;
 for(int s=0;s<20;s++){
  int h=s?((1<<s)+1):0;if(h>=m)break;
  i64 tq=1,en=1,ed=1;terminated=false;
  for(int idx=s;idx<int(ps.size());idx++){int p=ps[idx];if(p>U/tq){terminated=true;break;}tq*=p;en*=p-1;ed*=p;}assert(terminated);
  int ze=bmax+m,zr=D+m;vector<int>E(ze+1,0),R(zr+1,0);
  for(int v=1;v<=U;v+=2){
   i128 nv=i128(en)*ph[v],dv=i128(ed)*v;
   if(i128(ph[v])*ed>=i128(en)*v){nv=i128(ph[v])*ph[v];dv=i128(v)*v;}
   int de=max(-1,int((L/2)*nv/dv)-loss),dr=max(-1,int(L*nv/dv)-loss);
   if(de<ze) E[de+1]++;
   if(dr<zr) R[dr+1]++;
  }
  for(int z=1;z<=ze;z++) E[z]+=E[z-1];
  for(int z=1;z<=zr;z++) R[z]+=R[z-1];
  vector<int>Z(ze+1);for(int z=0;z<=ze;z++)Z[z]=E[z]-z;
  deque<int>dq;int pushed=-1;
  for(int j=h+1;j<=m;j++){
   int a=(j-h-1)/2,end=min(j+bmax,j+R[D+j]-a-1);bool ok;
   if(end<j)ok=true;
   else{
    assert(end<=ze);
    while(pushed<end){++pushed;while(!dq.empty()&&Z[dq.back()]<=Z[pushed])dq.pop_back();dq.push_back(pushed);}
    while(!dq.empty()&&dq.front()<j) dq.pop_front();
    assert(!dq.empty());
    ok=Z[dq.front()]<=a-j;
   }
   if(ok&&!covered[j]){covered[j]=1;remaining--;max_s=s;}
  }
  if(remaining==0)break;
 }
 int first=0,last=0;for(int j=1;j<=m;j++)if(!covered[j]){if(!first)first=j;last=j;}
 return {remaining,first,last,max_s};
}
int main(int argc,char**argv){
 auto start=chrono::steady_clock::now();int N=2000000;if(argc>=2)N=atoi(argv[1]);assert(N>=6&&N<=2000000);
 auto ph=phi_sieve(N);auto ps=primes();
 if(argc==4){int L=atoi(argv[2]),U=atoi(argv[3]);auto r=certify(L,U,ph,ps);cout<<L<<" "<<U<<" "<<r.failures<<" "<<r.first<<" "<<r.last<<" "<<r.max_s<<"\n";return 0;}
 int L=2301,intervals=0,rejected=0;
 while(L<=N){int U=min(N,L+max(1,L/10));Result r;
  while(true){r=certify(L,U,ph,ps);if(!r.failures)break;cerr<<"REJECT "<<L<<" "<<U<<" "<<r.failures<<" "<<r.first<<"\n";rejected++;if(U==L){cerr<<"UNRESOLVED "<<L<<"\n";return 2;}U=L+(U-L)/2;}
  cout<<"PASS "<<L<<" "<<U<<" "<<r.max_s<<"\n";cout.flush();intervals++;L=U+1;
 }
 cerr<<"SUMMARY intervals="<<intervals<<" rejected="<<rejected<<" wall_seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
