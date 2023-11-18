"""
# Graph (difficulty: 4)
- Represent as tuple 
- edges: path

"""
from typing import Union


class Graph:
    def __init__(self, edges: tuple[str, str]) -> None:
        self.edges = edges
        self.graph_dict = {}

        # Converting tuple[str, str] -> dict[str, list]
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_graph_dict(self):
        print("graph_dict", self.graph_dict)

    def get_path(self, start, end, path: list = []):
        """
        Get path of the start point and destination
        within the routes (if any)
        Applying recursive

        """
        # BASE CASE
        path = path + [start]
        # EXIT
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return [None]

        # RECURSE
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)  # recurse base case
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path: list = []):
        # BASE CASE
        path = path + [start]
        # EXIT
        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)

                # Shortest path algo
                # return None or shortest path (recursed base case) if fit
                # else, just return the existed path
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    flight_routes = [
        ("PP", "KL"),
        ("PP", "PERLIS"),
        ("KL", "KEDAH"),
        ("PP", "KEDAH"),
        ("PERAK", "KEDAH"),
        ("JOHOR", "N9"),
        ("MELAKA", "SELANGOR"),
    ]
    route_graph = Graph(flight_routes)
    # print(route_graph.get_path(start="PERAK", end="KEDAH"))
    route_graph.get_graph_dict()
    print(route_graph.get_shortest_path("PP", "KEDAH"))
