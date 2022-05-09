import re
from copy import deepcopy
import numpy as np


# Taken directly from https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49
def pyargmax(l):
  f = lambda i: l[i]
  return max(range(len(l)), key=f)


# Adapted from https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python
def Trim_nums(string_name, num_pos = 0):
    """
    Parameters:
    * string_name (string): a filename string
    * num_pos (int): The index of the # the user wants from the filename, if all #'s were in a list (optional, default is 0)
    Returns:
    * num_list[num_pos]: The extracted # from the num_list pulled from the filename 
    """
    regex = re.compile(r'\d+')
    regex.findall(string_name)
    num_list = [int(x) for x in regex.findall(string_name)]
    if len(num_list) != 1:
      print("File has more than one number entry")
    elif len(num_list) == 0:
      print("ERROR: Zero INTs in provided string filename")      
    return num_list[num_pos]

# Creates a list from the unique entries in a list
def uniques(trends): 
    """
    Parameters:
    * trends (list): a list of entries containing some redundant/repeat entries
    Returns:
    * output (list): The input list without any repeated entries
    """
    output = []
    for x in trends:
        if x not in output:
            output.append(x)
    return output

# This merges a list of lists into a super-list
def merger(seglist):
    """
    Parameters:
    * seglist (list): a list of lists
    Returns:
    * total_list (list): The combined list
    """
    total_list = []
    for seg in seglist:
        total_list.extend(seg)
    return total_list

# This takes in a list and the number of pool processes/cpus you want to run on
# It produces a list of lists of indices such that you have all indices evenly distributed across each subprocessor
def Chopper(big_list, cpus):
    """
    Parameters:
    * big_list (list): A list of items
    * cpus (int): The number of cpus/processes available to divide our big_list over
    Returns:
    * list_o_lists (list): The list of lists, separating big_list into equally sized chunks and distributing the remainder
    """
    # How many items we have to divide
    Entries_wanted = len(big_list)
    # The boundaries of our chopping
    slice_caps = []
    # The list of lists for output
    list_o_lists = []
    # The indices we are working with from big_list
    index_list_thing = [i for i in range(Entries_wanted)]

    # Get dividend/divisor
    b = Entries_wanted//cpus
    # Get remainder
    r = Entries_wanted%cpus

    # Create slice caps
    for i in range(cpus + 1):
        slice_caps.append(int(b*i))

    # Add the remainder to our final slice cap
    slice_caps[-1] += r

    # Go through and bubble our remainder through our slice caps until it is as evenly-distributed as can be
    while r > 0:
        for i in range(len(slice_caps)-1, 1, -1):
            if r > 0:
                slice_caps[(i):-1] =  [(j+1) for j in slice_caps[(i):-1]]
                r = r - 1

    # divide our big_list across the slice caps
    for i in range(len(slice_caps) - 1):
        list_o_lists.append(list(index_list_thing[slice_caps[i]:slice_caps[i+1]]))

    print("Distributing", Entries_wanted, "entries over", cpus, "CPUs in segments of size", b, "with remainder", Entries_wanted%cpus, "distributed across nodes")
    print("Here are slice caps", slice_caps)
    return list_o_lists


# Finds the minimum index/indices of a 2D matrix x
# Options for multiple minima, symmetric matrices, and 1D matrices are present
# Does not account for multiple identical minima, each will be returned individually
# Adapted using https://stackoverflow.com/questions/30180241/numpy-get-the-column-and-row-index-of-the-minimum-value-of-a-2d-array
def find_min_idx(x, n_low = 1, sym = False, two_D = True):
    """
    Parameters:
    * x (array): The input array
    * n_low (int): How many minima we want to retrieve
    * sym (Bool): Is this a symmetric array
    * two_D (Bool): Is this a 2D array?
    Returns:
    * minima (list): a list of the indices tuples where the min values were found
    """
    # work with a copy of the array so we don't alter the original in place
    y = deepcopy(x)
    minima = []
    # Loop until we have found all the minima we were ordered to
    for i in range(n_low):
        # If we are looking at a 2D array, unravel the array and set the value of the minima we found to inf so we don't catch it again
        if two_D == True:
            minima.append(np.unravel_index(y.argmin(), y.shape))
            y[minima[i][0], minima[i][1]] = np.inf
            # if we are looking at a symmetric array, set the mirrored value to inf too
            if sym == True:
                y[minima[i][1], minima[i][0]] = np.inf
        # Otherwise if we are looking at a 1D array, use this code
        elif two_D == False:
            minima.append(y.argmin())
            y[minima[i]] = np.inf
    return minima
