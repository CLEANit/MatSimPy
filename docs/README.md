This repo stores Python functions and classes that help materials science tasks with simulations.  Particularly for ASE and NetworkX, but also with VASP and (WIP) OVITO.  A number of these tools were found online and credit is given where possible.  If there are any items lacking suitable accreditation please let me know and I will correct them at once.

TODO: Update syntax for markdown

## Documentation:

### slist.py    -->    String and List

**Func trim_nums(string_name, num_pos = 0)** <br> This allows integer values to be picked out from filenames (i.e. "\home\file_1.txt" would return [1]).  A specified integer value is used to return an integer found in the filename (i.e.  "\home\file_1_2.txt" would return [1] by default, but would return [2] if num_pos = 1).  Adapted from resource [here](https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python)

**Func pyargmax(l)** <br> Find the argmax in a python list of numbers.  Adapted from resource [here](https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49)

**Func strainer(someList, indices)** <br> Takes someList and extracts a sub-list containing only entries found in the indices list. Useful for working with lists of objects that cannot simply be converted to numpy arrays or pandas dataframes.  Adapted from resource [here](https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list)

**Func repeatDataSampler(inList, reps, maxReps)** <br> Take a list *inList* made of consistently-sized ordered data groupings with size *maxReps* and containing *len(inList)/maxReps* groups. This function then subsamples *reps* entries from each group
'''python
repeatDataSampler([A, A, A, B, B, B...], 1, 3)
[A, B...]
'''

**Func index_mapper(stateSet, tranSet, uniqueSet)** <br> Takes arrays of states, chosen transition types, and unique states and returns a mapping between the states present and the unique state indices. Borrows from resource [here](https://stackoverflow.com/questions/18927475/numpy-array-get-row-index-searching-by-a-row)
</dl>

### graph.py    -->    Graph methods

**Func init_graph_from_atm** <br> Initializes an unconnected, undirected graph from a provided ASE atoms object.

**Func c_subgraph_finder** <br> Takes a graph and returns every connected subgraph it has. Adapted from resource [here](https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx)

**Func graph_visual** <br> Produces a labelled matplotlib visualization of a nx graph object.

**Func gdegree** <br> Obtains an array counting degrees of nodes present in graph G. Similar but distinct from the G.degree already present in the nx package.

### ase.py    -->    ASE methods

**Func vacuum_adjust** <br> Removes a user-specified amount of vacuum from an ASE atoms object and centres the object.

**Func composition_identifier** <br> Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols.
'''python
elem_list, num_list = composition_identifier(atmObjASE)
'''

### plots.py    -->    Matplotlib & Seaborn plotting
TBD
