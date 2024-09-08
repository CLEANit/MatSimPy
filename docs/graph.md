---
title: Graph Functions
layout: default
filename: Graph.md
excerpt: Documentation on the NetworkX graph functions of this project.
nav_order: 3
nav_exclude: false
search_exclude: false
---

### Graph methods - graph.py

## init_graph_from_atm
<dl>
<dt>def ()</dt>
<dd> 
Initializes an unconnected, undirected graph from a provided ASE atoms object.
</dd>
</dl>

  **Parameters:**
  * atm (ASE atoms object): The input molecule.
    
  **Returns:**
  * g (nx graph object): An unconnected graph made up of the atoms in our molecule, with attributes for the number and symbol of the element for each node.

## c_subgraph_finder [^1]
<dl>
<dt>def c_subgraph_finder(graf)</dt>
<dd> 
Takes a graph and returns every connected subgraph it has. Adapted from resource in footnote.
</dd>
</dl>

  **Parameters:**
  * graf (nx graph object): The input graph.
  
  **Returns:**
  * subgraphs (dict): A dictionary object, containing the connected subgraphs of graf, organized by size.

## graph_visual
<dl>
<dt>def graph_visual(graf, cdict, label_string = "Type", printout = False, font = [22, "black"])</dt>
<dd> 
Produces a labelled matplotlib visualization of a nx graph object.
</dd>
</dl>

  **Parameters:**
    * graf (nx graph): An input graph, with labelled nodes.
    * cdict (ditc): A dict object containing int-colour combinations for each label type (i.e. {1 : "Red", 2: "Blue"}).
    * label_string (str): A str object used to pick the visualized label type, default is "Type".
    * printout (bool): A bool object that determines if the colour-coding is printed to the user, default is False.
    * font (list): A list that contains the font size (int) and the font colour (str) of the user's choice, default is [22, "black"].
  
  **Returns:**
  * None

## gdegree
<dl>
<dt>def gdegree(graf)</dt>
<dd> 
Obtains an array counting degrees of nodes present in a graph. Similar but distinct from the G.degree already present in the nx package.
</dd>
</dl>

  **Parameters:**
  * graf (nx graph): Input graph.
  
  **Returns:**
  * g_count (np array): An array indicating the number of nodes with i edges in graf, where i is the index of g_count.

## state_stacker
<dl>
<dt>def state_stacker(state_array, num_class, readout = True)</dt>
<dd> 
Produces arrays that contain information on uniqueness of state compositions for regions of interest with distinct class numbers present.
</dd>
</dl>

  **Parameters:**
  * state_array (array): A numpy array that acts as a dataset of ROI data containing types/classifications.
  * num_class (int): The number of different classes in the data that we are being asked to sort.
  * readout (bool): Determines if the user is shown a readout of the stacked states.
  
  **Returns:**
  * unique_states (array): The unique states present in the input data.
  * unique_counts (array): Counts for unique states.
  * unique_firsts (array): Indices for first instances of unique states.
  * unique_inverse (array): The mapping needed to recreate the input data.

## Footnotes
[^1]: Adapted from [link](https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx)
