from collections import defaultdict

class GraphIndex:
    def __init__(self, edges):
        self.out = defaultdict(list)
        self.in_edges = defaultdict(list)

        for e in edges:
            self.out[e.src].append(e)

    def out_edges(self, node_id):
        return self.out.get(node_id, [])