# Bellman Ford Algorithm in Python

class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        # self.print_solution(dist)
        return dist

if __name__ == '__main__':
    with open('graphInput.txt', 'r') as f:
        lines = f.readlines()
        V = lines[0]
        g = Graph(int(V))
        for line in lines[1:]:
            s, d, w = line.split()
            g.add_edge(int(s), int(d), int(w))
        
        with open('shortestPaths.txt', 'r') as sf:
            shortest_path_lines = sf.readlines()
            for line in shortest_path_lines:
                s, d = line.split()
                dist = g.bellman_ford(int(s))
                print("A shortest path from {0} {1} has length {2}".format(s,d,dist[int(d)]))
            f.close()
        f.close()
