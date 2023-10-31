This repo stores Python functions and classes that help with materials science work.  Particularly for ASE and Networkx, but also with VASP and (WIP) OVITO.

Edit 31-10-2023: graph.py has now been documented below.  Further documentation pending.

## Documentation:

### io.py    -->    File Input/Output

**Class CIF_CAR_ASE** <br> Used for converting CIF and Vasp (CONTCAR, POSCAR) files to the ASE atoms object representation.  It is typically used as follows, after importing a file in need of conversion.

> extracted_CIF = CIF_CAR_ASE(file_path, "FILE_EXTENSION")<br>ASE_Extracted = extracted_CIF.convert(False)

File extensions in this case are CIF, CONTCAR, or POSCAR, ignoring case.  Feeding .convert 'True' will result in an attempt by ASE to create a visualization of the converted atoms object.  Please note that at this time, only the default view mode is implemented and it will not run in Google Colab as of last check.

**Func pickle_factory** <br> Creates a pickle file when given a file path (and name) string and a list object containing the information to be pickled.

**Func can_opener** <br> Unpickles pickle files when provided a file path to a valid pickle file.

### slist.py    -->    String and List

**Func trim_nums(string_name, num_pos = 0)** <br> This allows integer values to be picked out from filenames (i.e. "\home\file_1.txt" would return [1]).  A specified integer value is used to return an integer found in the filename (i.e.  "\home\file_1_2.txt" would return [1] by default, but would return [2] if num_pos = 1).

**Func pyargmax(l)** <br> Find the argmax in a python list of numbers.  From the resource here: https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49

### graph.py    -->    Graph methods

**Func init_graph_from_atm** <br> Initializes an unconnected, undirected graph from a provided ASE atoms object.

**Func c_subgraph_finder** <br> Takes a graph and returns every connected subgraph it has.

**Func graph_visual** <br> Produces a labelled matplotlib visualization of a nx graph object.

**Func gdegree** <br> Obtains an array counting degrees of nodes present in graph G.
