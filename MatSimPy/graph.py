import networkx as nx
from collections import Counter
import itertools

def init_graph(atm):
    """
    Parameters:
    * atm (ASE atoms object): The input molecule
    Returns: 
    * g (nx graph object): An unconnected graph made up of the atoms in our molecule, with attributes for the number and symbol of the element for each node
    """

    #Creates a blank graph with no nodes
    g = nx.Graph()

    #Adds the nodes from slab we made earlier (considering slab is an Atoms object the nodes are the atoms in the slab)
    for atom in atm:
        g.add_node(atom.index, number = atom.number, element = atom.symbol)

    #Get the node labels that we just set up a moment ago
    #node_labels = nx.get_node_attributes(g,'number')

    return g

# Adapted from: https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx
# This func takes in a graph and returns every CONNECTED subgraph it has
def C_Subgraph_finder(Graf):

    """
    Parameters:
    * graf (nx graph): The input graph
    Returns: 
    * subgraphs (dict): A dictionary object, containing the CONNECTED subgraphs of graf, organized by size
    """

    # Get the unique node IDs
    nodeID = [nodeid[0] for nodeid in Graf.nodes.data()]

    # Create a dictionary to store subgraphs
    subgraphs = {}
    # Create lists for each of the possible subgraph sizes (0 is not an accepted size, so we start at 1)
    for i in range(1, Graf.number_of_nodes() + 1):
    subgraphs[i] = []

    for nb_nodes in range(1, Graf.number_of_nodes() + 1):
      for SA in (selected_nodes for selected_nodes in itertools.combinations(Graf, nb_nodes)):
          if nx.is_connected(Graf.subgraph(SA)):
            subgraphs[nb_nodes].append(SA)

    for i in range(1, Graf.number_of_nodes() + 1):
    for j in range(len(subgraphs[i])):
      for k in subgraphs[i][j:]:
        if subgraphs[i][j] != k:
          if Counter(subgraphs[i][j]) == Counter(k):
            subgraphs[i].pop(subgraphs[i].index(k))

    return subgraphs