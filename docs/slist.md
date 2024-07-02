---
title: String & List Functions
layout: default
filename: slist.md
excerpt: Documentation on string and list functions.
nav_order: 2
nav_exclude: false
search_exclude: false
---

### slist.py    -->    String and List

This page is a WIP for documentation relating to the string & list functions of MatSimPy

**Func trim_nums(string_name, num_pos = 0)** <br> This allows integer values to be picked out from filenames (i.e. "\home\file_1.txt" would return [1]).  A specified integer value is used to return an integer found in the filename (i.e.  "\home\file_1_2.txt" would return [1] by default, but would return [2] if num_pos = 1).  Adapted from resource [here](https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python)

**Func pyargmax(l)** <br> Find the argmax in a python list of numbers.  Adapted from resource [here](https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49)

**Func strainer(someList, indices)** <br> Takes someList and extracts a sub-list containing only entries found in the indices list. Useful for working with lists of objects that cannot simply be converted to numpy arrays or pandas dataframes.  Adapted from resource [here](https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list)

**Func repeatDataSampler(inList, reps, maxReps)** <br> Take a list *inList* made of consistently-sized ordered data groupings with size *maxReps* and containing *len(inList)/maxReps* groups. This function then subsamples *reps* entries from each group
```python
repeatDataSampler([A, A, A, B, B, B...], 1, 3)
[A, B...]
```

**Func index_mapper(stateSet, tranSet, uniqueSet)** <br> Takes arrays of states, chosen transition types, and unique states and returns a mapping between the states present and the unique state indices. Borrows from resource [here](https://stackoverflow.com/questions/18927475/numpy-array-get-row-index-searching-by-a-row)
</dl>
