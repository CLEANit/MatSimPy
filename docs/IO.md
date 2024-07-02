---
title: I/O Functions
layout: default
filename: IO.md
excerpt: Documentation on the I/O functions of this project.
nav_order: 1
nav_exclude: false
search_exclude: false
---

### io.py    -->    File Input/Output

This page is a WIP for documentation relating to the I/O functions of MatSimPy

**Class CIF_CAR_ASE** <br> Used for converting CIF and Vasp (CONTCAR, POSCAR) files to the ASE atoms object representation.  It is typically used as follows, after importing a file in need of conversion.
```python
extracted_CIF = CIF_CAR_ASE(file_path, "FILE_EXTENSION")
ASE_Extracted = extracted_CIF.convert(False)
```
File extensions in this case are CIF, CONTCAR, or POSCAR, ignoring case.  Feeding .convert 'True' will result in an attempt by ASE to create a visualization of the converted atoms object.  Please note that at this time, only the default view mode is implemented and it will not run in Google Colab as of last check.

**Func pickle_factory** <br> Creates a pickle file when given a file path (and name) string and a list object containing the information to be pickled.
```python
pickle_factory("path/to/your/dir/file.pkl", yourData)
```

**Func can_opener** <br> Unpickles pickle files when provided a file path to a valid pickle file.
```python
importData = can_opener("path/to/your/dir/file.pkl")
```
