---
title: String & List Functions
layout: default
filename: slist.md
excerpt: Documentation on string and list functions.
nav_order: 2
nav_exclude: false
search_exclude: false
---

# String & List - slist.py

This page documents MatSimPy functions relating to handling strings and lists.

## trim_nums
Adapted from web resource. [^1]
<dl>
<dt>def trim_nums(string_name, num_pos = 0)</dt>
<dd> 
This allows integer values to be picked out from filenames.  A specified integer value is used as an index to return an integer found in the filepath.
</dd>
</dl>

  **Parameters:**
  * string_name (str): Path which possibly contains integer elements.
  * num_pos (int): Position of desired integer from parsed string, default 0.
  
  **Returns:**
  * (int): The desired integer value from the file path.
 
  **Example:**
  ```python
  trim_nums("\home\file_1.txt")
  1
  trim_nums("\home\file_1_2.txt", num_pos = 1)
  "File has more than one number entry"
  2
  ```

## pyargmax
Adapted from web resource. [^2]
<dl>
<dt>def pyargmax(ls)</dt>
<dd> 
Find the argmax in a python list of numbers.
</dd>
</dl>

  **Parameters:**
  * ls (list): A list of numbers.
  
  **Returns:**
  *  (int): The index of the item with the maximum value in the list.

## strainer
Adapted from web resource. [^3]
<dl>
<dt>def strainer(someList, indices)</dt>
<dd> 
Takes a list and extracts a sub-list containing only entries found at the indices provided.  Useful for working with lists of objects that cannot simply be converted to numpy arrays or pandas dataframes.
</dd>
</dl>

  **Parameters:**
  * someList (list): A list of objects that cannot simply be converted to np arrays or pd dataframes.
  * indices (list): A list of integer valued indices to be extracted from another list.
  
  **Returns:**
  *  (list): A version of the input list containing only objects found at the indices provided.

## repeatedDataSampler
<dl>
<dt>def repeatedDataSampler(inList, reps, maxReps)</dt>
<dd> 
Take a list inList made of consistently-sized ordered data groupings with size maxReps and containing len(inList)/maxReps groups. This function then subsamples reps entries from each group.
</dd>
</dl>

  **Parameters:**
  * inList (list): A list of consistently-sized ordered groupings
  * reps (int): The desired number of repeats in the final list.
  * maxReps (int): The number of repeats found for each list element in the input list.
  
  **Returns:**
  * (list): A list containing a reduced number of repeats.

  **Example:**
  ```python
  repeatDataSampler(['A1', 'A2', 'A3', 'B1', 'B2', 'B3'], 1, 3)
  ['A1', 'B1']
  ```

## index_mapper
Borrows from web resource. [^4]
<dl>
<dt>def index_mapper(stateSet, tranSet, uniqueSet)</dt>
<dd> 
Takes arrays of states, transition types, and unique states and returns a mapping between the states present and the unique state indices.
</dd>
</dl>

  **Parameters:**
  * stateSet (array): An array containing the unique compositions of each state (row), where each column represents a particular type.
  * tranSet (array): An array containing transition type choices corresponding to each state (row) in stateSet.
  * uniqueSet (array): An array containing the composition of each state (row), where each column represents a particular atom type.
  
  **Returns:**
  * state_mapping (array): An array that maps each state from stateSet to a unique state index from uniqueSet and indicates the transition type.

## chopper
<dl>
<dt>def chopper(big_list, cpus)</dt>
<dd> 
This takes in a list and the number of pool processes/cpus you want to run on.  It produces a list of lists of indices such that you have all indices evenly distributed across each subprocessor.
</dd>
</dl>

  **Parameters:**
  * big_list (list): A list of objects to split into sublists.
  * cpus (int): The number of cpus/processes available to divide big_list over.
  
  **Returns:**
  * list_o_lists (list): A list of lists made by separating big_list across cpus sublists as evenly as possible.


## find_min_idx
Adapted from web resource. [^5]
<dl>
<dt>def find_min_idx(x, n_low = 1, sym = False, two_D = True)</dt>
<dd> 
This function finds the minimum index/indices of a 2D matrix x with options for multiple minima, symmetric matrices, and 1D matrices.  However, it does not account for multiple identical minima, each will be returned individually.  The input matrix is deepcopied before being processed to obtain a list of minima for output.
</dd>
</dl>

  **Parameters:**
  * x (array): The input array, a 2D or 1D matrix.
  * n_low (int): The number of minima to retrieve.
  * sym (Bool): Designates a symmetric array.
  * two_D (Bool): Designates a 2D array.
  
  **Returns:**
  * minima (list): A list of index tuples where the minima were found.

## Footnotes
[^1]: Adapted from [link](https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python)
[^2]: Adapted from [link](https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49)
[^3]: Adapted from [link](https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list)
[^4]: Borrows from [link](https://stackoverflow.com/questions/18927475/numpy-array-get-row-index-searching-by-a-row)
[^5]: Adapted from [link](https://stackoverflow.com/questions/30180241/numpy-get-the-column-and-row-index-of-the-minimum-value-of-a-2d-array)
