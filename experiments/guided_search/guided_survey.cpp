// Independent, paper-inspired benchmark. NOT the authors' GPU/CPU implementation.
// Modes: raw reversible labels; legal active moves; legal+dependency closure;
// legal+closure+bounded stagnation-triggered expansions. No quantum speedup claimed.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using Term=std::array<unsigned,3>; using Scheme=std::vector<Term>;
struct Move{int i,j,a;};
uint64_t rnd(uint64_t &x){x^=x<<7;x^=x>>9;x^=x<<8;return x;}
bool active(const Term&t){return t[0]&&t[1]&&t[2];}
unsigned count(const Scheme&s){unsigned n=0;for(auto&t:s)n+=active(t);return n;}
void compact(Scheme&s){s.erase(std::remove_if(s.begin(),s.end(),[](const Term&t){return !active(t);}),s.end());}
Scheme school(int n){Scheme s;for(int i=0;i<n;i++)for(int j=0;j<n;j++)for(int k=0;k<n;k++)s.push_back({1u<<(i*n+j),1u<<(j*n+k),1u<<(i*n+k)});return s;}
void flip(Scheme&s,int i,int j,int a){if(i<0||j<0||i>=int(s.size())||j>=int(s.size())||i==j||a>=3||s[i][a]!=s[j][a])return;int b=(a+1)%3,c=(a+2)%3;s[i][b]^=s[j][b];s[j][c]^=s[i][c];}
std::vector<Move> legal(const Scheme&s){std::vector<Move> v;for(int a=0;a<3;a++)for(int i=0;i<int(s.size());i++)for(int j=0;j<int(s.size());j++)if(i!=j&&active(s[i])&&active(s[j])&&s[i][a]==s[j][a])v.push_back({i,j,a});return v;}
bool reduce_one(Scheme&s,int m){
 for(int a=0;a<3;a++)for(int head=0;head<int(s.size());head++){
  bool earlier=false;for(int j=0;j<head;j++)if(s[j][a]==s[head][a])earlier=true;if(earlier)continue;
  for(int off=1;off<=2;off++){
   int b=(a+off)%3,c=3-a-b;unsigned basis[16]={};uint64_t masks[16]={};
   for(int j=head;j<int(s.size());j++)if(s[j][a]==s[head][a]){
    unsigned val=s[j][b];uint64_t dep=uint64_t(1)<<j;
    for(int bit=m-1;bit>=0;bit--)if(val&(1u<<bit)){if(basis[bit]){val^=basis[bit];dep^=masks[bit];}else{basis[bit]=val;masks[bit]=dep;break;}}
    if(val==0){int p=__builtin_ctzll(dep);for(int h=0;h<int(s.size());h++)if(h!=p&&(dep&(uint64_t(1)<<h)))s[h][c]^=s[p][c];s[p][b]=0;compact(s);return true;}
   }
  }
 }
 return false;
}
unsigned closure(Scheme&s,int m){unsigned old=s.size();while(reduce_one(s,m)){}return old-s.size();}
bool plus(Scheme&s,uint64_t&x,int cap){if(int(s.size())>=cap)return false;std::vector<Move> v;for(int a=0;a<3;a++)for(int i=0;i<int(s.size());i++)for(int j=0;j<int(s.size());j++)if(i!=j&&s[i][a]!=s[j][a])v.push_back({i,j,a});if(v.empty())return false;auto z=v[rnd(x)%v.size()];auto t=s[z.j];s[z.j][z.a]^=s[z.i][z.a];t[z.a]=s[z.i][z.a];s.push_back(t);return true;}
void emit_scheme(const Scheme&s){std::cout<<'[';for(size_t i=0;i<s.size();i++){if(i)std::cout<<',';std::cout<<'['<<s[i][0]<<','<<s[i][1]<<','<<s[i][2]<<']';}std::cout<<']';}
int main(int argc,char**argv){try{
 if(argc!=7)throw std::runtime_error("usage: survey reference23.txt task mode seeds horizon target; task=school|excursion");
 std::ifstream f(argv[1]);int nr;f>>nr;Scheme ref(nr);for(auto&t:ref)f>>t[0]>>t[1]>>t[2];if(!f||nr!=23)throw std::runtime_error("reference read failed");
 std::string task=argv[2];int mode=std::stoi(argv[3]),N=std::stoi(argv[4]),L=std::stoi(argv[5]),target=std::stoi(argv[6]);if(mode<0||mode>3||N<1||L<1||(task!="school"&&task!="excursion"))throw std::runtime_error("bad args");
 std::vector<unsigned> hits;uint64_t total_steps=0,legal_scans=0,reductions=0,expansions=0;unsigned global_best=100;Scheme witness;int witness_seed=-1;
 std::cout<<"{\"task\":\""<<task<<"\",\"mode\":"<<mode<<",\"seed_count\":"<<N<<",\"seed_bits\":64,\"horizon\":"<<L<<",\"target\":"<<target<<",\"trials\":[";
 for(int seed=1;seed<=N;seed++){
  uint64_t x=seed;Scheme s=school(3);if(task=="excursion"){s=ref;uint64_t init=uint64_t(seed)^0x9e3779b97f4a7c15ULL;plus(s,init,32);plus(s,init,32);}
  unsigned best=count(s),hit=best<=unsigned(target)?0:L+1,plateau=0;uint64_t steps=0;Scheme bests=s;
  for(int t=1;t<=L&&hit>unsigned(L);t++){
   unsigned old=count(s);uint64_t y=rnd(x);
   if(mode==0){int k=0;while((1u<<k)<s.size())k++;unsigned mask=(1u<<k)-1;flip(s,y&mask,(y>>k)&mask,(y>>(2*k))&3);}
   else{
    compact(s);auto v=legal(s);legal_scans+=uint64_t(3)*s.size()*(s.size()-1);
    if(!v.empty()){auto z=v[y%v.size()];flip(s,z.i,z.j,z.a);compact(s);}
    if(mode>=2)reductions+=closure(s,9);
    if(mode==3){if(count(s)<old)plateau=0;else plateau++;if((plateau>=128||v.empty())&&s.size()<30){if(plus(s,x,30))expansions++;plateau=0;}}
   }
   steps++;unsigned now=count(s);if(now<best){best=now;bests=s;}if(best<=unsigned(target))hit=t;
  }
  if(best<global_best){global_best=best;witness=bests;witness_seed=seed;}total_steps+=steps;if(hit<=unsigned(L))hits.push_back(hit);
  if(seed>1){std::cout<<',';}std::cout<<"["<<seed<<','<<best<<','<<(hit<=unsigned(L)?hit:0)<<','<<steps<<"]";
 }
 std::cout<<"],\"hits\":"<<hits.size()<<",\"total_steps\":"<<total_steps<<",\"ordered_pair_predicate_checks\":"<<legal_scans<<",\"dependency_reductions\":"<<reductions<<",\"expansions\":"<<expansions<<",\"best_active\":"<<global_best<<",\"best_witness_seed\":"<<witness_seed<<",\"best_witness\":";emit_scheme(witness);std::cout<<"}\n";
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}}
