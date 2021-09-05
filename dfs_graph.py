#!/bin/python3
#User function Template for python3

#>>> My answer
class Solution:
    graph = None
    
    #Function to return   a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V,  adj):
        self.graph = adj
        visited = []
        self.dfsVisited(0,visited)
        
        return visited
        
    def dfsVisited(self, vtx , visited):
        visited.append(vtx)
        
        for neig in self.graph[vtx]:
            if neig not in visited:
                self.dfsVisited(neig,visited)
        

# GFG Input

#{ 
#  Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends