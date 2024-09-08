---
title: ASE Functions
layout: default
filename: ASE.md
excerpt: Documentation on the Atomic Simulation Environment (ASE) functions of this project.
nav_order: 4
nav_exclude: false
search_exclude: false
---

### Atomic Simulation Environment (ASE) Methods - ase.py

## vacuum_adjust
<dl>
<dt>def vacuum_adjust(ASE_Extracted, remove_vac)</dt>
<dd> 
Removes a user-specified amount of vacuum from an ASE atoms object and centres the object.
</dd>
</dl>

  **Parameters:**
  * ASE_xtract (ASE atoms object):
  * rm_vac (float): A positive float value, the amount of vacuum to remove from the Atoms object
  
  **Returns:**
  * ASE_xtract (ASE Atoms object): the centred modified ASE atoms object

## composition_identifier
<dl>
<dt>def composition_identifier(ASE_obj)</dt>
<dd> 
Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols.
</dd>
</dl>

  **Parameters:**
  * ASE_obj (ASE atoms object): The molecule/atom to be analyzed.
  
  **Returns:**
  * \[elem_list, num_list\] (list): Paired lists of element symbols and element #'s'
 
  **Example:**
  ```python
  elem_list, num_list = composition_identifier(ASE_obj)
  ```
