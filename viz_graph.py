from networkx import nx 

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
    
    def viz_dfs(self, node, color='b'):
        animate = dfs(G, node)
        for i in animate:
            temp_colors = colors[::]
            for j in i:
                temp_colors[j-1] = 'b'
            final.colors.append(temp_colors)
        animation.FuncAnimation(fig, animati)
        
    def dfs(G, s):
        animate = []
        Q = [s]
        visited = [s]
        animate.append(visited[::])
        while Q:
            node = Q.pop(0)
            for v in G.neighbors(node):
                if v not in visited:
                    visited.append(v)
                    Q.append(v)
            animate.append(visited[::])
       return (animate)
