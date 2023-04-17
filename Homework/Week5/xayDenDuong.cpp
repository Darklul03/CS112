#include<bits/stdc++.h>
using namespace std;
int a[1009];
int n,m;
int main()
{
    cin>>n>>m;
    if (n==0){
        cout<<1;
        return 0;
    }
    for (int i=1;i<=n;i++) cin>>a[i];
    sort(a+1,a+n+1);
    int ans=0;
    for (int i=1;i<=a[n]/2+1;i++)
    {
        int j=1, cur;
        for (int t=1;t<=m;t++)
        {
            if (j<=n) {
                cur=a[j];
                j++;
            }
            while(cur+2*i>=a[j] && j<=n) j++;
            if (j>n) {
                break;
            }
        }
        if (j>n) ans=i;
        if (ans){
            break;
        }
    }
    cout<<ans;
}