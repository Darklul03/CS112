#include <bits/stdc++.h>
using namespace std;
int p[10], color[10], new_color[10], c[10], t[10];
vector<int> a[10];
int main()
{
    int max_size = 1;
    p[0] = 1;
    for (int i = 0; i < 9; i++)
    {
        cin >> t[i];
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++)
        {
            a[i].push_back(s[j] - '0' - 1);
        }
        max_size *= 3;
        if (i > 0)
            p[i] = p[i - 1] * 3;
    }
    string s;
    cin >> s;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == 'X')
            color[i] = 0;
        if (s[i] == 'V')
            color[i] = 1;
        if (s[i] == 'D')
            color[i] = 2;
    }
    int mi = 1e9;
    for (int i = 0; i < max_size; i++)
    {
        int cur = i;
        for (int j = 8; j >= 0; j--)
        {
            new_color[j] = color[j];
            if (cur >= p[j] * 2)
            {
                c[j] = 2;
                cur -= p[j] * 2;
            }
            else if (cur >= p[j])
            {
                c[j] = 1;
                cur -= p[j];
            }
            else
            {
                c[j] = 0;
            }
        }
        for (int j = 0; j < 9; j++)
        {
            for (auto v : a[j])
            {
                new_color[v] = (new_color[v] + c[j]) % 3;
            }
        }
        int ans = 0, check = 0;
        for (int j = 0; j < 9; j++)
        {
            if (new_color[j] != 0)
            {
                check = 1;
                break;
            }
            ans += t[j] * c[j];
        }
        if (check == 0)
            mi = min(mi, ans);
    }
    if (mi == 1e9)
        mi = -1;
    cout << mi;
}