// Independent exact integer +/- implementation of the four-input census.
// No coefficient cutoff; enumeration includes descendants of successful states.
#include <array>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstdint>
#include <stdexcept>
using V=std::array<int,4>; using S=std::vector<V>;
V norm(V v){for(int x:v)if(x){if(x<0)for(int& y:v)y=-y;break;}return v;}
V sum(V a,V b,int s){for(int i=0;i<4;i++)a[i]+=s*b[i];return norm(a);}
const V zero={0,0,0,0};
const std::set<V> targets={{1,1,1,1},{1,-1,1,-1},{1,1,-1,-1},{1,-1,-1,1}};
struct Counts{uint64_t closures=0,tests=0,parent_tests=0,proposals=0;};
Counts c;
std::set<V> closure(const S& h){
 c.closures++;
 std::set<V>a={{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1}};
 std::set<V>missing=targets;missing.insert(h.begin(),h.end());
 bool changed=true;
 while(changed){changed=false;for(auto it=missing.begin();it!=missing.end();){
  bool found=false; V t=*it;
  for(V v:a){for(int sign:{1,-1}){c.tests++;if(a.count(sum(t,v,sign))){found=true;break;}}if(found)break;}
  if(found){a.insert(t);it=missing.erase(it);changed=true;}else ++it;
 }}return a;
}
bool feasible(const S& h){auto a=closure(h);for(V x:h)if(!a.count(x))return false;return true;}
S parent(S h){for(int i=int(h.size())-1;i>=0;i--){S p=h;p.erase(p.begin()+i);c.parent_tests++;if(feasible(p))return p;}throw std::runtime_error("inaccessible state");}
std::set<V> candidates(const std::set<V>& a){std::set<V>out;for(auto i=a.begin();i!=a.end();++i)for(auto j=i;j!=a.end();++j)for(int s:{1,-1}){V h=sum(*i,*j,s);if(h!=zero&&!a.count(h)&&!targets.count(h))out.insert(h);}return out;}
void arr(const std::vector<uint64_t>& x){std::cout<<"[";for(size_t i=0;i<x.size();i++){if(i)std::cout<<",";std::cout<<x[i];}std::cout<<"]";}
void state(const S& s){std::cout<<"[";for(size_t j=0;j<s.size();j++){if(j)std::cout<<",";std::cout<<"[";for(int i=0;i<4;i++){if(i)std::cout<<",";std::cout<<s[j][i];}std::cout<<"]";}std::cout<<"]";}
int main(int argc,char**argv){
 try{
 int k=argc>1?std::stoi(argv[1]):3;bool canonical=argc<3||std::string(argv[2])=="canonical";bool audit=argc<4||std::string(argv[3])!="no-audit";
 if(k<0||k>4)throw std::runtime_error("budget must be 0..4");
 std::set<S> seen; // Used only in memoized mode; canonical traversal never consults it.
 std::map<S,uint64_t> paths; // Test-only audit, populated after traversal.
 std::vector<S> recorded,stack(1);std::vector<uint64_t>levels(k+1),goals(k+1),ordered(k+1);
 S first;bool have=false;
 while(!stack.empty()){
 S h=stack.back();stack.pop_back();if(!canonical&&!seen.insert(h).second)continue;
 levels[h.size()]++;if(audit)recorded.push_back(h);auto a=closure(h);
 bool goal=true;for(V t:targets)if(!a.count(t))goal=false;
 if(goal){goals[h.size()]++;if(!have){first=h;have=true;}}
 if(int(h.size())==k)continue;
 for(V x:candidates(a)){c.proposals++;S g=h;g.push_back(x);std::sort(g.begin(),g.end());if(canonical&&parent(g)!=h)continue;stack.push_back(g);}
 }
 // Audit copies are not needed by the canonical algorithm. This verifies uniqueness
 // and counts all ordered helper histories by dynamic programming on recorded sets.
 std::sort(recorded.begin(),recorded.end(),[](const S&a,const S&b){return a.size()==b.size()?a<b:a.size()<b.size();});
 for(const S& h:recorded){if(paths.count(h))throw std::runtime_error("duplicate vertex");uint64_t q=h.empty()?1:0;for(size_t i=0;i<h.size();i++){S p=h;p.erase(p.begin()+i);auto it=paths.find(p);if(it!=paths.end())q+=it->second;}if(!q)throw std::runtime_error("missing predecessor");paths[h]=q;ordered[h.size()]+=q;}
 std::cout<<"{\"method\":\""<<(canonical?"canonical":"memoized")<<"\",\"by_depth\":";arr(levels);std::cout<<",\"goals\":";arr(goals);std::cout<<",\"ordered_histories_by_depth\":";if(audit)arr(ordered);else std::cout<<"null";
 std::cout<<",\"closures\":"<<c.closures<<",\"pair_tests\":"<<c.tests<<",\"parent_tests\":"<<c.parent_tests<<",\"proposals\":"<<c.proposals<<",\"vertices\":"<<([&](){uint64_t v=0;for(auto x:levels)v+=x;return v;})()<<",\"audit_records\":"<<recorded.size()<<",\"first_helper_set\":";state(first);std::cout<<"}\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}
}
