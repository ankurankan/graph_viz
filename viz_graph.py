import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class viz_graph(nx.Graph):

    def viz_neighbors(self, node, color='b'):
        """
        Draw the graph using matplotlib with highlighted neighbors.
	
	    Parameters
	    ----------
	    node: Networkx node
	        The node whose neighbors are to be highlighted.
	
	    color: 
		    The color of neighbouring nodes.
		    If not specified the default color is blue
	"""
	neighbor_nodes = self.neighbors(node)
        colors_list = [color if i in neighbor_nodes else 'r' for i in self.nodes()]
        nx.draw_networkx(self, nx.spring_layout(self), node_color=colors_list)
        
    def viz_bfs(self, node, color='b'):
        """
        Animation for breadth first search
        
        Parameters
        ----------
        node: Networkx node
            The node where to start the breadth first search from
            
        color:
            The color of the visited nodes.
            If color not specified the default color is blue
        """        
        def animati(i):
            nx.draw_circular(self, node_color=final_colors[i])
                     
        def bfs(s):
            animate = []
            Q = [s]
            visited = [s]
            animate.append(visited[::])
            while Q:
                node = Q.pop(0)
                for v in self.neighbors(node):
                    if v not in visited:
                        visited.append(v)
                        Q.append(v)
                animate.append(visited[::])
            return (animate)
     
        colors = ['r' for i in range(self.number_of_nodes())]
        final_colors = []
        animate = bfs(node)
        for i in animate:
            temp_colors = colors[::]
            for j in i:
                temp_colors[j-1] = 'b'
            final_colors.append(temp_colors)
        print(final_colors)
        fig = plt.figure()
        animation.FuncAnimation(fig, self.animate, fargs=final_colors)

    def animate(self, color_list):
        print color_list
        nx.draw_circular(self, node_color=color_list[i])	
