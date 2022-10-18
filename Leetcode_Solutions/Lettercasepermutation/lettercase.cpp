#include<bits/stdc++.h>
using namespace std;

void changecase(string &sub,int x)
    {
        int i=0;
        while(i<x)
        {
            i++;
        }
        cout<<"At "<<sub[i]<<endl;
        if(sub[i]>='A' && sub[i]<='Z')
        {
            sub[i] = sub[i] - 'A' + 'a';
        }
        else if(sub[i]>='a' && sub[i]<='z')
        {
            cout<<"To bros smal to upper "<<endl;
            sub[i] = sub[i] - 'a' + 'A';
        }
        // return sub;
    }
    void generate(string s,int i,string sub,vector<string> &res)
    {
        if(i==s.length())
        {
            res.push_back(sub);
            return;
        }
        
        // if(s[i]>='0' && s[i]<='9' && i+1<s.length())
        // {
        //     i++;
        // }
        //else
        {
            //cout<<"Genrating for "<<i<<endl;
            generate(s,i+1,sub,res);
            changecase(sub,i);
            generate(s,i+1,sub,res);
            changecase(sub,i);
        }
    }
    vector<string> letterCasePermutation(string s) {
        
        vector<string> res;
        
        generate(s,0,s,res);
        
        return res;
        
    }
int main(){

    string sub = "abs";
    changecase(sub,1);
    cout<<sub;
}
