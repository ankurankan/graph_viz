Graph Vizualizer
================

Graph Vizualizer is a tool(based on networkx) for vizualizing various graph algorithms.

Dependency:
Networkx: http://networkx.github.io/
Matplotlib: http://matplotlib.org/

Example for vizualizing neighbors:
<pre><code>
import viz_graph as vg
G = vg.viz_graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (1,4), (1,3), (2,5), (3,5), (4,5)])
G.viz_neighbours(1, color='green')
</code></pre>
