class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length=1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.length >= 1:
            self.last.next = new_node
            self.last = new_node
        else:
            self.first = new_node
            self.last = new_node
        self.length+=1
        
    def dequeue(self):
        if self.length >= 1:
            curr = self.first
            self.first = self.first.next
            self.length -=1
            return curr.value
        return False
        
            
class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} -> {edges}")
            
            
    def bfs(self, src_vertex):
        visited = set()
        visited.add(src_vertex)
        result = []
        q = Queue(src_vertex)
        
        while q.length > 0:
            curr = q.dequeue()
            result.append(curr)
            for neighbour in self.adj_list[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.enqueue(neighbour)
        print("BFS order:", result)
        
    def dfs(self, curr, visited, result):
        visited.add(curr)
        result.append(curr)
        for neighbours in self.adj_list[curr]:
            if neighbours not in visited:
                self.dfs(neighbours, visited, result)
            
            
            
graph = Graph()

for v in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_vertex(v)

# Add edges
graph.add_edges('A', 'B')
graph.add_edges('A', 'C')
graph.add_edges('B', 'D')
graph.add_edges('B', 'E')
graph.add_edges('C', 'F')

graph.print_graph()
graph.bfs('A')
visited = set()
result = []
graph.dfs('A', visited, result)
print(f"DFS order: {result}")