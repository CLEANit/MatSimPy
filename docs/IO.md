---
title: I/O Functions
layout: default
filename: IO.md
excerpt: Documentation on the I/O functions of this project.
nav_order: 1
nav_exclude: false
search_exclude: false
---

# File Input/Output - io.py

This page documents MatSimPy functions related to processing file inputs, outputs, and conversions.

## CIF_CAR_ASE
<dl>
<dt>class CIF_CAR_ASE(filename, filetype)</dt>
<dd> 
Used for converting CIF and Vasp (CONTCAR, POSCAR) files to the ASE atoms object representation. File extensions are CIF, CONTCAR, or POSCAR, ignoring case.  Feeding .convert 'True' will result in an attempt by ASE to create a visualization of the converted atoms object.  Please note that at this time, only the default view mode is implemented and it will not run in Google Colab as of last check.
</dd>
</dl>

  **Parameters:**
  * filename (str): A title for a CIF or POSCAR file (please include directory in title).
  * filetype (str): A file type string, such as POSCAR, CONTCAR, or CIF (case is irrelevant).

### convert
<dl>
<dt>def convert(check)</dt>
<dd> 
Creates a pickle file when given a file path (and name) string and a list object containing the information to be pickled.
</dd>
</dl>

  **Parameters:**
  * check (Bool): If True, returns an ASE interactive view of the atoms object (does not work in Google Colab).

  **Returns:**
  * out (ASE Atoms object): The output atom stored from the init.

  **Example:**
  ```python
  extracted_CIF = CIF_CAR_ASE(file_path, "FILE_EXTENSION")
  ASE_Extracted = extracted_CIF.convert(False)
  ```

## pickle_factory 
<dl>
<dt>def pickle_factory(file_title, data_list)</dt>
<dd> 
Creates a pickle file when given a file path (and name) string and a list object containing the information to be pickled.
</dd>
</dl>

  **Parameters:**
  * file_title (str): A title for a pickle file (please include directory in title).
  * data_list (list): A list of data to go into a pickle file.

  **Returns**
  * None

  **Example:**
  ```python
  pickle_factory("path/to/your/dir/file.pkl", yourData)
  ```

## can_opener
<dl>
<dt>def can_opener(filename)</dt>
<dd> 
Unpickles pickle files when provided a file path to a valid pickle file.
</dd>
</dl>

  **Parameters:**
  * filename (str): A title for a pickle file (please include directory in title).
  
  **Returns:**
  * Dills (n/a): An object loaded from the provided pickle file.
 
  **Example:**
  ```python
  importData = can_opener("path/to/your/dir/file.pkl")
  ```
