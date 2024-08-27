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

<dl>
<dt>class CIF_CAR_ASE(filename, filetype)</dt>
<dd> 
Used for converting CIF and Vasp (CONTCAR, POSCAR) files to the ASE atoms object representation. File extensions in this case are CIF, CONTCAR, or POSCAR, ignoring case.  Feeding .convert 'True' will result in an attempt by ASE to create a visualization of the converted atoms object.  Please note that at this time, only the default view mode is implemented and it will not run in Google Colab as of last check.
</dd>
</dl>

  **Parameters:**
  * filename (str): A title for a CIF or POSCAR file (please include directory in title)
  * filetype (str): A file type string, such as POSCAR, CONTCAR, or CIF (case is irrelevant)

  **Example:**
  ```python
  extracted_CIF = CIF_CAR_ASE(file_path, "FILE_EXTENSION")
  ASE_Extracted = extracted_CIF.convert(False)
  ```

<dl>
<dt>def pickle_factory(file_path, file_extension)</dt>
<dd> 
Creates a pickle file when given a file path (and name) string and a list object containing the information to be pickled.
</dd>
</dl>

  **Parameters:**
  * File_title (str): A title for a pickle file (please include directory in title)
  * Data_list (list): A list of data to go into a pickle file

  **Example:**
  ```python
  pickle_factory("path/to/your/dir/file.pkl", yourData)
  ```

<dl>
<dt>def can_opener(filename)</dt>
<dd> 
Unpickles pickle files when provided a file path to a valid pickle file.
</dd>
</dl>

  **Parameters:**
  * filename (string): A title for a pickle file (please include directory in title)
  
  **Returns:**
  * Dills (n/a): An object loaded from the provided pickle file
 
  **Example:**
  ```python
  importData = can_opener("path/to/your/dir/file.pkl")
  ```
