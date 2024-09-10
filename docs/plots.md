---
title: Plot Functions
layout: default
filename: plots.md
excerpt: Documentation on the plt and sns functions of this project.
nav_order: 5
nav_exclude: false
search_exclude: false
---

# Plotting - plots.py

This page documents MatSimPy functions relating to handling matplotlib and seaborn plots.

## histo_distro
<dl>
<dt>def histo_distro(userpkl, unpack = True, index_key = None, merge = False, x_label = "x", xlims = None, ylims = None, title = "title", decim = 1, scaleFac = 1, bins = 25, descriptive = False, legLab = None, line = False)
</dt>
<dd> 
Returns a histogram of a user-provided distribution in a variety of formats, with customizeable formatting options to display various properties of the data in a pleasing format.
</dd>
</dl>

  **Parameters:**
  * userpkl (pkl, list, dict, array): pkl or other file storing the input data.
  * unpack (bool): unpickles the input file if in pkl format, default True.
  * index_key (key): dict key for input data, default None.
  * merge (bool): merges lists if input is a list of lists, default False.
  * x_label (str): label for x-axis, default "x".
  * xlims (tuple): 2-tuple for x-axis limits, default None.
  * ylims (tuple): 2-tuple for y-axis limits, default None.
  * title (str): title of plot, default "title".
  * decim (int): decimal places for value displays, default 1.
  * scaleFac (float): scaling factor for the input data, default 1.
  * bins (int): number of histogram bins to use, default 25.
  * descriptive (bool): put mean and sdev in plot title, default False.
  * legLab (str): legend entry for data, default None.
  * line (bool): apply mean line to plot, default False.
  
  **Returns:**
  * None
