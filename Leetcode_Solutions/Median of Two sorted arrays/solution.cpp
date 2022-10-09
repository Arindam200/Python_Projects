class Solution {
public:
    int max(int a,int b)
    {
        if(a>b)
            return a;
        else    
            return b;
    }
    int min(int a,int b)
    {
        if(a<b)
            return a;
        else
            return b;
    }

    double median(int *a,int i,int j)
    {
        int n=j-i+1;
        if(n%2==0) //even
        {
            return (a[i+(j-i+1)/2]+a[i+(j-i+1)/2-1])/2.0;
        }
        else //odd
        {
            return (a[i+(j-i+1)/2]);
        }
    }
    void discardleft(int &si,int &sj,int &li,int &lj)
    {
        if((sj-si+1)%2==0) //even 
        {
            lj=lj-(sj-si+1)/2+1;
            si=si+(sj-si+1)/2-1;
        }
        else
        {
            lj=lj-(sj-si+1)/2;
            si=si+(sj-si+1)/2;
        }
    }
    void discardright(int &si,int &sj,int &li,int &lj)
    {
        if((sj-si+1)%2==0) //even 
        {
            int d=(sj-si+1)-(sj-si+1)/2 -1;
            sj=sj-(sj-si+1)/2 +1;
            li=li+d;
        }
        else
        {
            int d=(sj-si+1)-(sj-si+1)/2-1;
            sj=sj-(sj-si+1)/2;
            li=li+d;
        }
    }
    void finalmedian(int *s,int si,int sj,int *l,int li,int lj,double &sln)
    {
        int ssize=sj-si+1;
        int lsize=lj-li+1;
        double med;
        if(ssize<=0)
        {
            med=median(l,li,lj);
        }
        else if(ssize==1)
        {
            if(lsize==1)
            {
                med=(s[si]+l[li])/2.0;
            }
            else if(lsize%2!=0) //size of large is odd
            {
                double temp;
                if(s[si]<l[li+lsize/2-1])
                {
                    temp=l[li+lsize/2-1];
                }
                else if(s[si]>l[li+lsize/2+1])
                {
                    temp=l[li+lsize/2+1];
                }
                else
                {
                    temp=s[si];
                }
                med=(l[li+lsize/2]+temp)/2.0;
            }
            else if(lsize%2==0) //larger array is even
            {

                int a=l[li+lsize/2-1];
                int b=l[li+lsize/2];

                if(s[si]<a)
                {
                    med=a;
                }
                else if(s[si]>b)
                {
                    med=b;
                }
                else
                {
                    med=s[si];
                }
            }
        }
        else if(ssize==2)
        {
            if(lsize==2)
            {
                int a=s[si];
                int b=s[sj];
                int c=l[li];
                int d=l[lj];
                int Max = max( a, max( b, max( c, d ) ) );
                int Min = min( a, min( b, min( c, d ) ) );
                med=( a + b + c + d - Max - Min ) / 2.0;
            }
            else if(lsize%2!=0 )//odd
            {
                int a=l[li+lsize/2];
                int b=max(s[si],l[li+lsize/2-1]);
                int c=min(s[sj],l[li+lsize/2+1]);
                med=float(a + b + c - max(a, max(b, c)) - min(a, min(b, c)));
            }
            else if(lsize%2==0) //even
            {
                int a=l[li+lsize/2-1];
                int b=l[li+lsize/2];
                int c=max(s[si],l[li+lsize/2-2]);
                int d=min(s[sj],l[li+lsize/2+1]);
                int Max = max( a, max( b, max( c, d ) ) );
                int Min = min( a, min( b, min( c, d ) ) );
                med=( a + b + c + d - Max - Min ) / 2.0;
            }
        }
        sln=med;
    }
    void solve(int *s,int si,int sj,int *l,int li,int lj,double &sln)
    {
        if((sj-si+1)<=2)
        {
            finalmedian(s,si,sj,l,li,lj,sln);
        }
        else 
        {
            int sm=median(s,si,sj);
            int lm=median(l,li,lj);
            if(sm<lm)
            {
                discardleft(si,sj,li,lj);
            }
            else
            {
                discardright(si,sj,li,lj);
            }
            if((sj-si+1)>(lj-li+1))
            {
                int *temp=s;
                s=l;
                l=temp;
                int t=si;
                si=li;
                li=t;
                t=sj;
                sj=lj;
                lj=t;
            }
            solve(s,si,sj,l,li,lj,sln);
        }
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m=nums1.size();
        int n=nums2.size();
        double sln;
        if(m<=2 && n<=2)
        {
            if(m==0 && n==0)
            {
                sln=0.00000;
            }
            else if(m==1 && n==0)
            {
                sln=double(nums1[0]);
            }
            else if(m==0 && n==1)
            {
                sln=double(nums2[0]);
            }
            else if(m==1 && n==1)
            {
                sln=double((nums1[0]+nums2[0])/2.0);
            }
            else if(m==2 && n==0)
            {
                sln=double((nums1[0]+nums1[1])/2.0);
            }
            else if(m==0 && n==2)
            {
                sln=double((nums2[0]+nums2[1])/2.0);
            }
            else if(m==2 && n==1)
            {
                int a=nums1[0];
                int b=nums1[1];
                int c=nums2[0];
                sln=double(a + b + c - max(a, max(b, c)) - min(a, min(b, c)));
            }
            else if(m==1 && n==2)
            {
                int a=nums1[0];
                int b=nums2[0];
                int c=nums2[1];
                sln=double(a + b + c - max(a, max(b, c)) - min(a, min(b, c)));
            }
            else 
            {
                int a=nums1[0];
                int b=nums1[1];
                int c=nums2[0];
                int d=nums2[1];
                int Max = max( a, max( b, max( c, d ) ) );
                int Min = min( a, min( b, min( c, d ) ) );
                sln=double( a + b + c + d - Max - Min ) / 2.0;
            }
            
        }
        else
        {
            int *s,*l;
            int si,sj,li,lj;
            if(m<n)
            {
                s=nums1.data();
                l=nums2.data();
                si=0,sj=m-1;
                li=0,lj=n-1;
            }
            else
            {
                s=nums2.data();
                l=nums1.data();
                si=0,sj=n-1;
                li=0,lj=m-1;
            }
            solve(s,si,sj,l,li,lj,sln);
        }
        
        
        return sln;
    }
};