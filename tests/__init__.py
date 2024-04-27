from binarytree import tree, bst

t = bst()

# Generate a graphviz.Digraph object
# Arguments to this method are passed into Digraph.__init__
graph = t.graphviz()

# Get DOT (graph description language) body
graph.body

# Render the binary tree
graph.render()