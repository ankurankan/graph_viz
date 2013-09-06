from networkx import nx 

class viz_graph(nx.Graph):
    def viz_neighbors(self, node, color='blue'):
        neighbor_nodes = self.neighbors(node)
        colors_list = [color if i in neighbor_nodes else 'red' for i in self.nodes()]
        nx.draw_networkx(self, nx.spring_layout(self), node_color=colors_list)
