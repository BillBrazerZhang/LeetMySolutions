//My Solution
#include <iostream>
#include <cstring>
using namespace std;

string CountAndSay(int n);
int main(){
  cout << CountAndSay(5);
}

string CountAndSay(int n){
  if (n==1){
    return "1";
  }
  else{
    string in = "1";
    for (int i = 1; i < n; i++){
      string out = "";
      int len = in.size();
      int index = 0;
      int num = 1;
      while (index < len-1){
        if (in[index] != in[index+1]){
          out = out + to_string(num) + in[index];
          index++;
          num = 1;
        }
        else{
          num ++;
          index ++;
        }
      }
      in = out + to_string(num) + in[index];
    }
    return in;
  }
}


//Standard Solution
class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";
        n-=2;
        string s = "11", temp;
         while(n--){
            int count = 1; temp = "";
            for(int i=1; i<s.size(); i++){
                if(s[i]==s[i-1]){
                    count++;
                }else{
                    temp.push_back('0'+count);
                    temp.push_back(s[i-1]);
                    count = 1;
                }
            }
             temp.push_back('0'+count);
             temp.push_back(s[s.size()-1]);
             s = temp;
        }
        return s;
    }
};
