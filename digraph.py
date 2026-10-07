import matplotlib.pyplot as plt
import networkx as nx


class Digraph:
    def __init__(self, labels: list[str]):
        self.edges: list[list[bool]] = [
            [False for _ in range(len(labels))] for _ in range(len(labels))
        ]
        self.labels: list[str] = labels

    def add_edge(self, u: str, v: str):
        assert u in self.labels and v in self.labels
        u_index = self.labels.index(u)
        v_index = self.labels.index(v)
        self.edges[u_index][v_index] = True

    def render(self):
        graph = nx.DiGraph()

        n = len(self.edges)
        graph.add_nodes_from(range(n))

        for i, row in enumerate(self.edges):
            for j, has_edge in enumerate(row):
                if has_edge:
                    graph.add_edge(i, j)

        pos = nx.nx_pydot.pydot_layout(graph, prog="dot")
        nx.draw_networkx

        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_size=1200,
            arrows=True,
            arrowsize=20,
        )

        plt.show()
