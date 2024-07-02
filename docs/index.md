---
layout: default
title: Index
nav_exclude: true
---

This repo stores Python functions and classes that help materials science tasks with simulations.  Particularly for ASE and NetworkX, but also with VASP and (WIP) OVITO.  A number of these tools were found online and credit is given where possible.  If there are any items lacking suitable accreditation please let me know and I will correct them at once.

TODO:
* [ ] Update syntax for markdown to distinguish each function
* [ ] Shuffle documentation from main index to designated pages
* [ ] Update to PEP 8 standards
      
## Documentation:

### ase.py    -->    ASE methods

**Func vacuum_adjust** <br> Removes a user-specified amount of vacuum from an ASE atoms object and centres the object.

**Func composition_identifier** <br> Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols.
```python
elem_list, num_list = composition_identifier(atmObjASE)
```

### plots.py    -->    Matplotlib & Seaborn plotting
TBD
