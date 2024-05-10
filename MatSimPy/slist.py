import re
from copy import deepcopy
import numpy as np
import itertools as it

# Adapted from https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list
def strainer(someList, indices):
    """
    Takes list and extracts a sub-list containing only entries found in index list
    Parameters:
    * someList (list): A list object to pull a subset from
    * indices (list): The indices of someList to keep
    Returns:
    * strainedList (list): someList subsampled by indices provided
    """
    strainedList = [i for j, i in enumerate(someList) if j not in indices]
    return strainedList

def repeatedDataSampler(inList, reps, maxReps):
    """
    Takes a list containing len(inList)/maxReps ordered categories and subsamples reps entries from each group (Ex. For trivial case of repeated letters, [A, A, A, B, B, B...] --> [A, B...])
    Parameters:
    * inList (list): A list object to pull a subset from
    * reps (int): The number of entries to extract from each sub-category in inList
    * maxReps (int): The total number of entries in each sub-category in the input list
    Returns:
    * output (list): The extracted subsampled list of repeats
    """
    print("Input list has length {} and contains {} repeats per entry".format(len(inList), maxReps))
    if reps > maxReps:
        print("reps > maxReps will lead to an array out of bounds exception. Returning None")
        return None
    elif reps == maxReps:
        print("reps = maxReps. Returning original inList")
        return inList
    else:
        output = [inList[i:i+reps] for i in range(0, len(inList), maxReps)]
        output = list(it.chain.from_iterable(output))
        return output

# Taken directly from https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49
def pyargmax(l):
    f = lambda i: l[i]
    return max(range(len(l)), key=f)

# Adapted from https://stackoverflow.com/questions/14008440/how-to-extract-numbers-from-filename-in-python
def trim_nums(string_name, num_pos = 0):
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

  
# Python user-defined exception
class InvalidOutputException(Exception):
    "Raised when output format is not an approved data type"
    pass


# Python user-defined exception
class InputMismatchException(Exception):
    "Raised when input lengths/sizes do not match"
    pass


# Generates a list/array of all possible compositions (irrespective of order, with replacement) for a list of classes/categories of a given length
def comp_list(string_classes, num_per, list_form = False, out_form = "int"):
    """
    Parameters:
    * string_classes (String): The classes of items available, in terms of 1 index iterables, i.e. "ABCD", "1234" 
    * num_per (int): A POSITIVE integer value for the number of items allowed in each state
    * list_form (bool: A switch to decide if output a nested list or np array, default False (np)
    * out_form (str): Determines if output is "int" or "str" formatted, default "int"
    Returns: 
    * out (nested list or np array: All possible compositions under the input conditions
    """

    combos = it.combinations_with_replacement(string_classes, num_per)
    out = []
    try:
        if out_form == "int":
            for i in combos:
                out.append(list(map(int, list(i))))
        elif out_form == "str":
            for i in combos:
                out.append(list(map(str, list(i))))
        else:
            raise InvalidOutputException

    except InvalidOutputException:
      print("Exception occurred: Invalid out_form data type")   

    # Output in np array form or nested list as per user input
    if list_form:
        return out
    else:
        return np.array(out)


def index_mapper(stateSet, tranSet, uniqueSet):
    """
    Parameters:
    * stateSet (array): An array containing the unique compositions of each state (row), where each column represents a particular atom type
    * tranSet (array): An array containing transition type choices corresponding to each state (row) in stateSet
    * uniqueSet (array): An array containing the composition of each state (row), where each column represents a particular atom type
    Returns: None
    * state_mapping (array): An array that maps each state from stateSet to a unique state index from uniqueSet and indicates the transition atom type
    """
    if len(tranSet) == len(stateSet):
        # Store where each unique state occurs in the dataset
        ix_list = []
        #https://stackoverflow.com/questions/18927475/numpy-array-get-row-index-searching-by-a-row
        for i in uniqueSet:
            # Check row equalities to get confirmation that state is present and save the index in the unique_states list
            ix_list.append(np.where(np.all(stateSet==i,axis=1)))
    
        state_mapping = np.zeros((len(tranSet), 2), dtype = int)
        state_mapping[:,0] = [i for i in range(len(tranSet))]
    
        for t, i in enumerate(ix_list):
            # Find the values of the steps that match those found in the idx for a particular unique state
            # This creates a list of len(i) where each element is a true/false ndarray as long as step_state
            # Taking the sum reduces the output to a single binary 1D array which has 1s where the entry belongs to state t and zeros where it does not
            # True false evaluate to zero and 1 with sum, which is exceedingly useful here
            # Temp becomes a 1D array here with length equal to the number of steps, as expected from checking over step_state
            temp = sum([state_mapping[:,0] == j for j in i[0]])
            # Ensure int type to 1/0
            temp = temp.astype(int)
            # Pull all locations where the same state shows up
            temp = np.where(temp == 1)
            # Put in the unique state index for that state at those indices
            state_mapping[temp, 1] = t
    
        # And we also tack on the stacked next atoms
        state_mapping = np.append(state_mapping, np.reshape(tranSet, (tranSet.shape[0],1)), axis = 1)
        return state_mapping
        
    else:
        print("Error: Lengths of next atoms list and state dataset do not match")
        raise InputMismatchException


def ave_masker(data_times, data_other, stop, increment, readout = True):
  """
  This function returns the mean and standard deviation across multiple items by stepping through cumulative time and data arrays in incremental fashion.
  
  Inputs:
  * data_times (list of array): List of arrays containing cumulative time data 
  * data_other (list of array): List of arrays containing Cumulative spacial/frequency data, i.e. total transitions, diffusion, etc.
  * stop (int): The last index for averaging over
  * increment (int): Dictates the size of the averaging window/mask at each step
  * readout (bool): Prints data on first few rounds of process, default True
  Outputs:
  * ave_data (array):
  * sdev_data (array):
  """
  ave_data = []
  sdev_data = []
  for t in range(0, stop, increment):
    temp = []
    for i in range(10):
      mask = np.where(data_times[i] <= t)
      if len(mask[0]) != 0 and len(ave_data) <= 10 and readout:
        print("Mask {} is {} containing {} and final entry {}".format(i+1, mask, data_other[i][mask], data_other[i][mask][-1]))
        print(data_times[i][mask])

      # Get the last/latest entry at this time mask, since we only want one entry per trajectory here
      if len(mask[0]) != 0:
        temp.append(data_other[i][mask][-1])
      # Otherwise if no entries are found yet, just append a zero
      else:
        temp.append(0)

    # Take mean and sdev for this set of results from time mask
    ave_data.append(np.mean(temp))
    sdev_data.append(np.std(temp))
    
    # Readout for feedback on first few rounds
    if len(ave_data) <= 10 and readout:
      print("Captures for this round include {}".format(temp))
      print("Mean for this round is {}".format(ave_data[-1]))
      print("Sdev for this round is {}".format(sdev_data[-1]))

  return ave_data, sdev_data

def nesting(nested):
  """
  Print out individual and cumulative lengths for items in a dict of lists
  """  
  print("Individual", [len(nested[n]) for n in nested])
  print("Cumulative", np.cumsum([len(nested[n]) for n in nested]))
  return None
