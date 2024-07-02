This repo stores Python functions and classes that help materials science tasks with simulations.  Particularly for ASE and NetworkX, but also with VASP and (WIP) OVITO.  A number of these tools were found online and credit is given where possible.  If there are any items lacking suitable accreditation please let me know and I will correct them at once.

TODO: 
* [ ] Update syntax for markdown to distinguish each function
* [ ] Shuffle documentation from main index to designated pages
* [ ] Update to PEP 8 standards

## Documentation:

### graph.py    -->    Graph methods

**Func init_graph_from_atm** <br> Initializes an unconnected, undirected graph from a provided ASE atoms object.

**Func c_subgraph_finder** <br> Takes a graph and returns every connected subgraph it has. Adapted from resource [here](https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx)

**Func graph_visual** <br> Produces a labelled matplotlib visualization of a nx graph object.

**Func gdegree** <br> Obtains an array counting degrees of nodes present in graph G. Similar but distinct from the G.degree already present in the nx package.

### ase.py    -->    ASE methods

**Func vacuum_adjust** <br> Removes a user-specified amount of vacuum from an ASE atoms object and centres the object.

**Func composition_identifier** <br> Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols.
```python
elem_list, num_list = composition_identifier(atmObjASE)
```

### plots.py    -->    Matplotlib & Seaborn plotting
TBD
