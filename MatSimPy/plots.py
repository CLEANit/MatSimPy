import matplotlib.pyplot as plt
import numpy as np
from MatSimPy.MatSimPy.io import can_opener
from MatSimPy.MatSimPy.slist import merger

def histo_distro(userpkl, unpack = True, index_key = None, merge = False, x_label = "x", xlims = None, ylims = None, title = "title", decim = 1, scaleFac = 1, bins = 25, descriptive = False, legLab = None, line = False):
  """
  Returns a histogram of a user-provided distribution in a variety of formats, with customizeable formatting options to display various properties of the data in a pleasing format
  
  Parameters:
  * userpkl (pkl, list, dict, array): pkl or other file storing the input data
  * unpack (bool): unpickles the input file if in pkl format, default True
  * index_key (key): dict key for input data, default None
  * merge (bool): merges lists if input is a list of lists, default False
  * bins (int): number of histogram bins to use, default 25
  * scaleFac (float): scaling factor for the input data, default 1
  * line (bool): apply mean line to plot, default False 
  * descriptive (bool): put mean and sdev in plot title, default False
  * legLab (str): legend entry for data, default None 
  * decim (int): decimal places for value displays, default 1 
  * x_label (str): label for x-axis, default "x" 
  * xlims (tuple): 2-tuple for x-axis limits, default None
  * ylims (tuple): 2-tuple for y-axis limits, default None
  * title (str): title of plot, default "title" 
  Returns:
  * None
  """
  
  x = userpkl
  if unpack:
    x = can_opener(x)
  if index_key != None:
    x = x[index_key]
  if merge:
    print(type(x), len(x))
    x = merger(x)
    print(type(x), len(x))

  x = np.array(x)/scaleFac

  plt.figure(figsize = (4,2.5))
  # the histogram of the data
  if line:
    plt.axvline(np.mean(x), color='red')

  # Get mean and std dev for the input data
  mu = np.round(np.mean(x), decim)
  sdev = np.round(np.std(x), decim)

  if xlims != None:
    plt.xlim(left = xlims[0])
    plt.xlim(right = xlims[1])
  else:
    plt.xlim(left = 0)

  if ylims != None:
    plt.ylim(bottom = ylims[0])
    plt.ylim(top = ylims[1])
  else:
    plt.ylim(bottom = 0)

  if legLab != None:
    plt.hist(x, bins, range = xlims, density=1, label = legLab)
  else:
    plt.hist(x, bins, range = xlims, density=1)

  if descriptive:
    plt.title("{} ({} :{} {} :{})".format(title, r'$\mu$', mu, r'$\sigma$', sdev), fontsize = 10)
  else:
    plt.title(title)
    
  plt.xlabel(x_label)
  plt.ylabel('Probability density')

  # Tweak spacing to prevent clipping of axis labels
  plt.tight_layout()
  plt.show()
