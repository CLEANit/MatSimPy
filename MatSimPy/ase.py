from ase.build import add_vacuum
from slist import uniques
from itertools import chain

# Removes vacuum from an ASE atoms object and centres the object
def vacuum_adjust(ASE_Extracted, remove_vac):
    """
    Parameters:
    * ASE_Extracted (ASE atoms object): 
    * remove_vac (float): A POSITIVE float value, the amount of vacuum to remove from the Atoms object
    Returns: 
    * ASE_Extracted (ASE Atoms object): the centred modified ASE atoms object
    """
    add_vacuum(ASE_Extracted, -remove_vac)
    ASE_Extracted.center()
    return ASE_Extracted  
  
# Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols
def composition_identifier(Atoms_object):
    """
    Parameters:
    * Atoms_object (ASE atoms object): The molecule/atom to be analyzed
    Returns: 
    * [elem_list, num_list] (list): Paired lists of element symbols and element #'s'
    """
    entries = []
    entries = [Atoms_object.get_chemical_symbols(), Atoms_object.get_atomic_numbers()]
    elem_list = uniques(entries[0])
    num_list = uniques(entries[1])
    return [elem_list, num_list]  
