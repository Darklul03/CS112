#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;

int n,m;
vector<vector<int>> g;
vector<int> connect;
vector<int> visited;

int main() {
    #ifdef Keqing
        freopen("input.txt","r",stdin);
        // freopen("output.txt","w",stdout);
    #else
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
    #endif

    cin >> n >> m;
    g.resize(n+1);
    visited.resize(n+1);
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    for (int i = 1; i <= n; i++) {
        if (visited[i]) continue;

        int cnt = 0;
        queue<int> q;
        q.push(i);
        visited[i] = 1;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            cnt++;

            for (auto v : g[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }

        connect.push_back(cnt);
    }
    
    ll res = 0;
    for (int i = 0; i < connect.size(); i++) {
        for (int j = i+1; j < connect.size(); j++) {
            res += 1LL * connect[i] * connect[j];
        }
    }
    cout << res;

    return 0;
}