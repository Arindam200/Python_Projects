// Approach 2
class Solution {
public:
    string breakPalindrome(string palindrome) {
        
        int n = palindrome.size();
        // if string size less than 1
        if(n==1) 
        return ""; // return empty string
        int i=0;
        while(i<n && palindrome[i]=='a'){
            i++;
        }
        if(i==n/2 and n%2 !=0){
            palindrome[n-1] = 'b';
            return palindrome;
        }
        if(i<n) palindrome[i] = 'a';
        if(i>=n){
            palindrome[n-1] = 'b';
        }
        return palindrome;
    }
};
