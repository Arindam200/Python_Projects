#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
bool isValid(string s1) {
    stack<char> s;
    for(int i=0;i<s1.size();i++)
    {
        if(s.empty())
        {
            s.push(s1[i]);
        }
        else if(s1[i]=='(' || s1[i]=='{' || s1[i]=='[')
        {
            s.push(s1[i]);
        }
        else
        {
            if(s1[i]==')')
            {
                if(s.top()=='(')
                {
                    s.pop();
                }
                else
                {
                    s.push(s1[i]);
                }
            }
            else if(s1[i]=='}')
            {
                if(s.top()=='{')
                {
                    s.pop();
                }
                else
                {
                    s.push(s1[i]);
                }
            }
            else
            {
                if(s.top()=='[')
                {
                    s.pop();
                }
                else
                {
                    s.push(s1[i]);
                }
            }
        }
    }
    if(s.size()==0)
        return true;
    return false;
}
int main()
{
    ios_base::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);
	string s;
	cin>>s;
	cout<<isValid(s)<<endl;
}

