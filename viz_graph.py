from networkx import *
import logging

logging.basicConfig(filename='viz_graph.log', level=logging.DEBUG)

class viz_graph(Graph):
    def viz_neighbors(self, node, color='blue'):
        neighbor_nodes = self.neighbors(node)
        logging.info("neighbor_nodes", str(neighbor_nodes))
        colors_list = [color if i in neighbor_nodes else 'red' for i in self.nodes()]
#        logging.info("colors_list", str(colors_list))
        draw_networkx(self, nx.spring_layout(self), node_color=colors_list)
