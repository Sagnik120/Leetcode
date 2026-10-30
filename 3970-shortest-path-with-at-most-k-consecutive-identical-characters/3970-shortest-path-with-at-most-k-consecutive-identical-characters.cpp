class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int,int>>> g(n);
        for(auto& e:edges) g[e[0]].push_back({e[1],e[2]});
        vector<vector<int>> d(n,vector<int>(k+1,2e9));
        priority_queue<array<int,3>,vector<array<int,3>>,greater<>> q;
        d[0][1]=0;
        q.push({0,0,1});
        while(!q.empty()){
            auto [w,u,c]=q.top();
            q.pop();
            if(w>d[u][c]) continue;
            if(u==n-1) return w;
            for(auto& [v,wt] : g[u]){
                int nc=(labels[u]==labels[v]) ? c+1 : 1;
                if(nc<=k && w+wt<d[v][nc]){
                    d[v][nc]=w+wt;
                    q.push({d[v][nc],v,nc});
                    
                }
            }
        }
        return -1;
    }
};