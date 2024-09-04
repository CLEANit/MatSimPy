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

This page is a WIP for documentation relating to the string & list functions of MatSimPy.

## trim_nums
<dl>
<dt>def trim_nums(string_name, num_pos = 0)</dt>
<dd> 
This allows integer values to be picked out from filenames.  A specified integer value is used as an index to return an integer found in the filepath.  Adapted from resource [here](https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python)
</dd>
</dl>

  **Parameters:**
  * string_name (str): Path which possibly contains integer elements
  * num_pos (int): Position of desired integer from parsed string, default 0
  
  **Returns:**
  *  num_list[num_pos] (int): The desired integer value from the file path
 
  **Example:**
  ```python
  trim_nums("\home\file_1.txt") # Returns 1
  trim_nums("\home\file_1_2.txt", num_pos = 1) # Returns 2
  ```

## pyargmax
<dl>
<dt>def pyargmax(l)</dt>
<dd> 
Find the argmax in a python list of numbers.  Adapted from resource [here](https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49).
</dd>
</dl>

  **Parameters:**
  * l (list): A list of numbers
  
  **Returns:**
  *  (int): The index of the item with the maximum value in the list

## strainer
<dl>
<dt>def strainer(someList, indices)</dt>
<dd> 
Takes a list and extracts a sub-list containing only entries found at the indices provided.  Useful for working with lists of objects that cannot simply be converted to numpy arrays or pandas dataframes.  Adapted from resource [here](https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list)
</dd>
</dl>

  **Parameters:**
  * someList (list): A list of objects that cannot simply be converted to np arrays or pd dataframes
  * indices (list): A list of integer valued indices to be extracted from another list
  
  **Returns:**
  *  (list): A version of the input list containing only objects found at the indices provided

## repeatDataSampler
<dl>
<dt>def repeatDataSampler(inList, reps, maxReps)</dt>
<dd> 
Take a list inList made of consistently-sized ordered data groupings with size maxReps and containing len(inList)/maxReps groups. This function then subsamples reps entries from each group.
</dd>
</dl>

  **Parameters:**
  * inList (list): A list of consistently-sized ordered groupings
  * reps (int): The desired number of repeats in the final list
  * maxReps (int): The number of repeats found for each list element in the input list
  
  **Returns:**
  * (list): A list containing a reduced number of repeats

  **Example:**
  ```python
  repeatDataSampler(['A1', 'A2', 'A3', 'B1', 'B2', 'B3'], 1, 3)
  ['A1', 'B1']
  ```

## index_mapper
<dl>
<dt>def index_mapper(stateSet, tranSet, uniqueSet)</dt>
<dd> 
Takes arrays of states, transition types, and unique states and returns a mapping between the states present and the unique state indices. Borrows from resource [here](https://stackoverflow.com/questions/18927475/numpy-array-get-row-index-searching-by-a-row).
</dd>
</dl>

  **Parameters:**
  * stateSet (array): An array containing the unique compositions of each state (row), where each column represents a particular type
  * tranSet (array): An array containing transition type choices corresponding to each state (row) in stateSet
  * uniqueSet (array): An array containing the composition of each state (row), where each column represents a particular atom type
  
  **Returns:**
  * state_mapping (array): An array that maps each state from stateSet to a unique state index from uniqueSet and indicates the transition type
