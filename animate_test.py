import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class animate_test(nx.Graph):
    def colors(self, init_color, end_color):
        number_of_nodes = self.number_of_nodes()
        self.color_arr = [[end_color if j<i else init_color for j in range(number_of_nodes)] for i in range(number_of_nodes)]
    def animate(self, i):
        nx.draw_circular(self, node_color=self.color_arr[i])
        
    def start_animation(self):
        fig = plt.figure()
        animation.FuncAnimation(fig, self.animate)
