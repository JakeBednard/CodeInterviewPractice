from Queue import Queue

class Graph(object):
    """Graph represented as dictionary of node_name: [edges]"""
    def __init__(self, nodes=None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = {}

    def add_node(self, node, edges):
        """If node exist, extend edges, otherwise add new node"""
        if node in self.nodes:
            self.nodes[node].extend(edges)
        else:
            self.nodes[node] = edges

    def remove_node(self, node):
        """Remove a node from the list"""
        self.nodes.pop(node, None)

    def dfs(self, start, visited=None):
        """Recursive DFS on Graph starting from start
        Returns list of elements found in order in DFS search
        """
        if start not in self.nodes:
            return []

        elif visited is None:
            visited = [start]

        visited.append(start)
        for node in self.nodes[start]:
            if node in self.nodes and node not in visited:
                self.dfs(node, visited)

        return visited

    def dfs_path(self, start, end, visited=None):
        """Recursive DFS on Graph starting from start
        Returns True if path from start to end, otherwise False
        """
        if start not in self.nodes or end not in self.nodes:
            return False

        elif visited is None:
            visited = []

        visited.append(start)
        for node in self.nodes[start]:
            if node in self.nodes and node not in visited:
                if node == end or self.dfs_path(node, end, visited):
                    return True

        return False

    def bfs(self, start):
        """Iterative approach using O(n) aux space

        If start does not exist, returns empty list
        If a node contains a edge to a unknown node, skip visiting that node

        Returns list of path taken during search
        """

        if start not in self.nodes:
            return []

        visited, i = [start], 0
        while i < len(visited):
            start = visited[i]
            i += 1
            for node in self.nodes[start]:
                if node in self.nodes and node not in visited:
                    visited.append(node)

        return visited

    def bfs_path(self, start, end):
        """Iterative approach using O(n) aux space

        If start does not exist, returns empty list
        If a node contains a edge to a unknown node, skip visiting that node

        Returns True if node was found, otherwise False
        """

        if start not in self.nodes or end not in self.nodes:
            return False

        elif start == end:
            return True

        visited, i, distance = [start], 0, 0
        while i < len(visited):
            start = visited[i]
            i += 1
            distance += 1
            for node in self.nodes[start]:
                if node not in visited and node in self.nodes:
                    if node == end:
                        return True
                    else:
                        visited.append(node)

        return False


if __name__ == '__main__':

    graph = Graph({
        "a": ["a", "b", "c", "d"],
        "b": ["e"],
        "c": ["e", "f"],
        "d": ["f", "z"],
        "e": ["g"],
        "f": ["g"],
        "g": ["b", "h"]
    })

    print("DFS")
    print(graph.dfs("a"))
    print(graph.dfs_path("a", "g"))
    print(graph.dfs_path("g", "a"))

    print("\nBFS")
    print(graph.dfs("a"))
    print(graph.bfs_path("a", "g"))
    print(graph.bfs_path("g", "a"))
