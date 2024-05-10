import matplotlib.pyplot as plt
from collections import Counter
import networkx as nx
import numpy as np
import itertools
import torch

def init_graph_from_atm(atm):
    """
    Initializes an unconnected, undirected graph from an ASE atoms object
    Parameters:
    * atm (ASE atoms object): The input molecule
    Returns: 
    * g (nx graph object): An unconnected graph made up of the atoms in our molecule, with attributes for the number and symbol of the element for each node
    """
    #Creates a blank graph with no nodes
    g = nx.Graph()
    #Adds nodes from atms object
    for atom in atm:
        g.add_node(atom.index, number = atom.number, element = atom.symbol)
    return g

# Adapted from: https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx
# This func takes in a graph and returns every CONNECTED subgraph it has
def c_subgraph_finder(Graf):
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
    
def graph_visual(Gin, cdict, label_string = "Type", printout = False, font = [22, "black"]):
    """
    Creates a convenient visualization of the input graph for the feature classes and colours present in cdict
    Parameters:
    * Gin (nx graph): An input graph, with labelled nodes
    * cdict (ditc): A dict object containing int-colour combinations for each label type (i.e. {1 : "Red", 2: "Blue"})
    * label_string (str): A str object used to pick the visualized label type, default is "Type" 
    * printout (bool): A bool object that determines if the colour-coding is printed to the user, default is False
    * font (list): A list that contains the font size (int) and the font colour (str) of the user's choice, default is [22, "black"]
    Returns: 
    * None
    """
    # Get type labels from the graph input
    labels = [Gin.nodes[i][label_string] for i in Gin.nodes]
    clabels = [cdict[i] for i in labels]
    if printout:
        print("Showing graph colours, types, and labels")
        print([(c, l, g) for c, l, g in zip(clabels, labels, Gin.nodes)])
    pos = nx.spring_layout(Gin, seed=117)  # positions for all nodes
    nx.draw_networkx_edges(Gin, pos, width=1.0, alpha=0.5)
    nx.draw_networkx(Gin, pos, node_color = clabels, node_size = 750, with_labels = True, font_size=font[0], font_color=font[1])
    plt.tight_layout()
    plt.axis("off")
    plt.show()
    return None


def gdegree(G):
    """
    Obtains an array counting degrees of nodes present in graph G
    Parameters:
    * G (nx graph): Input graph 
    Returns:
    * G_count (np array): An array indicating the number of nodes with i edges in G, where i is the index of G_count
    """
    G_degree = []
    # Degree values for an unknown graph could range from 0 to n, where n is the number of nodes in the graph
    G_count = np.zeros((1,len(G)+1))
    for n in list(G.nodes()):
        G_degree.append(G.degree[n])
    # This covers connection possibilities
    for r in range(len(G)+1):
        G_count[0][r] += (G_degree.count(r))
    return G_count


def state_stacker(state_array, num_class, readout = True):
    """
    Produces arrays that contain information on uniqueness of state compositions for regions of interest with num_class distinct class numbers present
    
    Parameters:
    * state_array (array): A numpy array that acts as a dataset of ROI data containing types/classifications
    * num_class (int): The number of different classes in the data that we are being asked to sort
    Returns:
    * unique_states (array): The unique states present in the input data
    * unique_counts (array): Counts for unique states
    * unique_firsts (array): Indices for first instances of unique states
    * unique_inverse (array): The mapping needed to recreate the input data
    """
    
    print("States provided in np array of shape {}".format(state_array.shape))
    # One-hot encode the torch tensor version of the ndarray and use the provided number of classes to classify them
    # reduce values of all class numbers by 1 since one_hot() counts from 0 for classes
    hot_state_array = one_hot(torch.tensor(state_array - 1), num_classes = num_class)
    print("States now in shape {}".format(hot_state_array.shape))
    # Take the sum across each state to get the total count per class for a single state as a row vector of length 5
    hot_state_array = torch.sum(hot_state_array, 1)
    print("States now in shape {}".format(hot_state_array.shape))
    print(hot_state_array[0:10])
    # Convert back to numpy
    hot_state_array = hot_state_array.numpy()
    # Get the unique rows and how often they occur
    unique_states, unique_firsts, unique_inverse, unique_counts = np.unique(hot_state_array, axis = 0, return_counts = True, return_inverse = True, return_index = True)
    
    if readout:
        print("unique_states", unique_states.shape)
        print(unique_states[0:10])
        print("unique_counts", unique_counts.shape)
        print(unique_counts[0:10])
        print("unique_first", unique_firsts.shape)
        print(unique_firsts[0:10])
        print("unique_inverse", unique_inverse.shape)
        print(unique_inverse[0:10])
    
    return unique_states, unique_counts, unique_firsts, unique_inverse
