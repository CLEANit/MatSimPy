---
title: ASE Functions
layout: default
filename: ASE.md
excerpt: Documentation on the Atomic Simulation Environment (ASE) functions of this project.
nav_order: 4
nav_exclude: false
search_exclude: false
---

### ase.py    -->    ASE methods

**Func vacuum_adjust** <br> Removes a user-specified amount of vacuum from an ASE atoms object and centres the object.

**Func composition_identifier** <br> Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols.
```python
elem_list, num_list = composition_identifier(atmObjASE)
```
