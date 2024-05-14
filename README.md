This repo stores Python functions and classes that help materials science tasks with simulations.  Particularly for ASE and NetworkX, but also with VASP and (WIP) OVITO.  A number of these tools were found online and credit is given where possible.  If there are any items lacking suitable accreditation please let me know and I will correct them at once.

Edit 04-03-2024: Accreditations and function examples updated.  Further documentation pending.

## Documentation:

### io.py    -->    File Input/Output

**Class CIF_CAR_ASE** <br> Used for converting CIF and Vasp (CONTCAR, POSCAR) files to the ASE atoms object representation.  It is typically used as follows, after importing a file in need of conversion.

> extracted_CIF = CIF_CAR_ASE(file_path, "FILE_EXTENSION")<br>ASE_Extracted = extracted_CIF.convert(False)

File extensions in this case are CIF, CONTCAR, or POSCAR, ignoring case.  Feeding .convert 'True' will result in an attempt by ASE to create a visualization of the converted atoms object.  Please note that at this time, only the default view mode is implemented and it will not run in Google Colab as of last check.

**Func pickle_factory** <br> Creates a pickle file when given a file path (and name) string and a list object containing the information to be pickled.
> pickle_factory("path/to/your/dir/file.pkl", yourData)

**Func can_opener** <br> Unpickles pickle files when provided a file path to a valid pickle file.
> importData = can_opener("path/to/your/dir/file.pkl")

### slist.py    -->    String and List

**Func trim_nums(string_name, num_pos = 0)** <br> This allows integer values to be picked out from filenames (i.e. "\home\file_1.txt" would return [1]).  A specified integer value is used to return an integer found in the filename (i.e.  "\home\file_1_2.txt" would return [1] by default, but would return [2] if num_pos = 1).  Adapted from resource [here](https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python)

**Func pyargmax(l)** <br> Find the argmax in a python list of numbers.  Adapted from resource [here](https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49)

**Func strainer(someList, indices)** <br> Takes someList and extracts a sub-list containing only entries found in the indices list. Useful for working with lists of objects that cannot simply be converted to numpy arrays or pandas dataframes.  Adapted from resource [here](https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list)

**Func repeatDataSampler(inList, reps, maxReps)** <br> Take a list *inList* made of consistently-sized ordered data groupings with size *maxReps* and containing *len(inList)/maxReps* groups. This function then subsamples *reps* entries from each group (Ex. For trivial case of repeated letters with *reps = 1*, *maxReps = 3*, [A, A, A, B, B, B...] --> [A, B...])

**Func index_mapper(stateSet, tranSet, uniqueSet)** <br> Takes arrays of states, chosen transition types, and unique states and returns a mapping between the states present and the unique state indices. Borrows from resource [here](https://stackoverflow.com/questions/18927475/numpy-array-get-row-index-searching-by-a-row)

### graph.py    -->    Graph methods

**Func init_graph_from_atm** <br> Initializes an unconnected, undirected graph from a provided ASE atoms object.

**Func c_subgraph_finder** <br> Takes a graph and returns every connected subgraph it has. Adapted from resource [here](https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx)

**Func graph_visual** <br> Produces a labelled matplotlib visualization of a nx graph object.

**Func gdegree** <br> Obtains an array counting degrees of nodes present in graph G. Similar but distinct from the G.degree already present in the nx package.

### ase.py    -->    ASE methods

**Func vacuum_adjust** <br> Removes a user-specified amount of vacuum from an ASE atoms object and centres the object.

**Func composition_identifier** <br> Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols.
> elem_list, num_list = composition_identifier(atmObjASE)
