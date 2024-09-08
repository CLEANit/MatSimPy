from ase.build import add_vacuum
from slist import uniques
from itertools import chain

def vacuum_adjust(ASE_xtract, rm_vac):
    """
    Removes vacuum from an ASE atoms object and centres the object.
    Parameters:
    * ASE_xtract (ASE atoms object): 
    * rm_vac (float): A positive float value, the amount of vacuum to remove from the Atoms object
    Returns: 
    * ASE_xtract (ASE Atoms object): the centred modified ASE atoms object
    """
    add_vacuum(ASE_xtract, -rm_vac)
    ASE_xtract.center()
    return ASE_xtract  
  
# Defines the composition of an ASE atoms object in a paired list output for chemical numbers and symbols
def composition_identifier(ASE_obj):
    """
    Parameters:
    * ASE_obj (ASE atoms object): The molecule/atom to be analyzed
    Returns: 
    * [elem_list, num_list] (list): Paired lists of element symbols and element #'s'
    """
    entries = []
    entries = [ASE_obj.get_chemical_symbols(), ASE_obj.get_atomic_numbers()]
    elem_list = uniques(entries[0])
    num_list = uniques(entries[1])
    return [elem_list, num_list]  
