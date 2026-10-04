#include <bits/stdc++.h>
using namespace std;
vector<int> factors(int x) {vector<int>p;for(int d=2;d*d<=x;d++)if(x%d==0){p.push_back(d);while(x%d==0)x/=d;}if(x>1)p.push_back(x);return p;}
int main(int argc,char**argv) {
 ifstream in(argv[1]);int L,U,last=5,intervals=0;long long pairs=0,tests=0;
 while(in>>L>>U) {
  assert(L==last+1);last=U;intervals++;
  vector<int> o,phi(U+1);vector<vector<int>>pf(U+1);
  for(int v=1;v<=U;v+=2){o.push_back(v);pf[v]=factors(v);phi[v]=v;for(int p:pf[v])phi[v]=phi[v]/p*(p-1);}
  sort(o.begin(),o.end(),[&](int x,int y){int d=phi[x]*y-phi[y]*x;return d?d>0:x<y;});
  int H=o.size(),m=U/6, F=U/2+U/3-U/6,B=H-(U/3-U/6+1),D=U-F+m;
  vector<vector<int>> e(5,vector<int>(H+1,INT_MAX)),r=e;
  vector<int>sm={3,5,7,11};
  for(int k=2;k<=H;k++) {
   for(int s=0;s<=4;s++){e[s][k]=e[s][k-1];r[s][k]=r[s][k-1];}
   int v=o[k-1];
   for(int i=0;i<k-1;i++) {
    int u=o[i];vector<int>ps=pf[u];for(int p:pf[v])if(find(ps.begin(),ps.end(),p)==ps.end())ps.push_back(p);
    vector<pair<long long,int>>ds={{1,1}};for(int p:ps){int sz=ds.size();for(int z=0;z<sz;z++)ds.push_back({ds[z].first*p,-ds[z].second});}
    int ce=0,cr=0;for(auto [d,mu]:ds){ce+=mu*((L/2)/d);cr+=mu*(L/d);}
    for(int s=0;s<=4;s++){if(s && ((u%sm[s-1]==0)!=(v%sm[s-1]==0)))break;e[s][k]=min(e[s][k],ce);r[s][k]=min(r[s][k],cr);}
    pairs++;
   }
  }
  for(int b=0;b<=B;b++)for(int j=1;j<=m;j++) {
   bool pass=false;for(int s=0;s<=4;s++){int h=s?(1<<s)+1:0;if(j<=h)continue;int k=H-b-(j-h-1)/2;assert(k>=2&&k<=H);if(e[s][k]>=b+j || r[s][k]>=D+j)pass=true;}
   if(!pass){cerr<<"FAIL "<<L<<" "<<U<<" "<<b<<" "<<j<<"\n";return 1;}tests++;
  }
  cout<<"INDEPENDENT_PASS "<<L<<" "<<U<<"\n";
 }
 assert(intervals==71 && last==2300);cout<<"PASS 71 small intervals; inclusion-exclusion pair counts="<<pairs<<" b,j tests="<<tests<<"\n";
}
