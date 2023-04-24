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
  
# Defines the composition of the slab in a paired list output for chemical numbers and symbols
def Slab_composition_identifier(Atoms_object):
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


# Produces a list of indices matching an atom symbol
# Originally written by Yuxin Chang, UofT, Ted Sargent Group.  I claim no authorship of this function
def get_indices(atoms, symbol):
    """
    Parameters:
    * atoms (ASE atoms): The molecule/atom to be analyzed
    * symbol (string): The elemment symbol to be searched for
    Returns: 
    * indices (list): list of indices which match the atom type from symbol
    """
    indices = []
    for atom in atoms:
        if atom.symbol == symbol:
            indices.append(atom.index)
    return indices
    
# Produces an ase atoms slab with reordered indices based on the order of elements (to match VASP file atom indexing)
# Originally written by Yuxin Chang, UofT, Ted Sargent Group.  I claim no authorship of this function
def reorder_indices(slab):
    """
    Parameters:
    * slab (ASE atoms): The molecule/atom to be analyzed
    Returns: 
    * slab (ASE atoms): The modified slab
    * new indices (list): The new ordering of the old indices
    """
    new_indices = []
    for symbol in replace_symbols:
        new_indices.append(get_indices(slab, symbol))
    new_indices = list(chain.from_iterable(new_indices))
    slab = slab[new_indices]
    return slab, new_indices
