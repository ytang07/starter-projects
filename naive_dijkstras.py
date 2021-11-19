from numpy import Inf

# create our graph using an adjacency list representation
# each "node" in our list should be a node name and a distance
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}

# takes the graph and the starting node
# returns a list of distances from the starting node to every other node
def naive_dijkstras(graph, root):
    n = len(graph)
    # initialize distance list as all infinities
    dist = [Inf for _ in range(n)]
    # set the distance for the root to be 0
    dist[root] = 0
    # initialize list of visited nodes
    visited = [False for _ in range(n)]
    # loop through all the nodes
    for _ in range(n):
        # "start" our node as -1 (so we don't have a start node yet)
        u = -1
        # loop through all the nodes to check for visitation status
        for i in range(n):
            # if the node 'i' hasn't been visited and 
            # we haven't processed it or the distance we have for it is less
            # than the distance we have to the "start" node
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        # all the nodes have been visited or we can't reach this node
        if dist[u] == Inf:
            break
        # set the node as visited
        visited[u] = True
        # compare the distance to each node from the "start" node
        # to the distance we currently have on file for it
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    return dist

print(naive_dijkstras(graph,1))
        