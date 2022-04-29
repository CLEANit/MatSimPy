import pickle
from packaging import version
from ase.io.cif import parse_cif_ase
from ase.io.vasp import read_vasp
from ase.visualize import view

# Custom error class adapted from: https://www.programiz.com/python-programming/user-defined-exception
class VersionError(Exception):
    """Exception raised for incompatible ASE versions detected.

    Attributes:
        version -- ASE version which caused the error
        message -- explanation of the error
    """

    def __init__(self, version, message= "ASE version " + version + " is not > 3.17"):
        self.version = version
        self.message = message
        super().__init__(self.message)


#Creates pickle files
def pickle_factory(File_title, Data_list):
  """
  Parameters:
  * File_title (string): A title for a pickle file (please include directory in title)
  * Data_list (list): A list of data to go into a pickle file
  Returns: None
  """
  print(File_title)
  f = open(File_title, 'wb')
  pickle.dump(Data_list, f)
  print('done pickles')

# Opens pickle files
def can_opener(filename):
  """
  Parameters:
  * filename (string): A title for a pickle file (please include directory in title)
  Returns: processed pickle object
  """
  f = open(filename, 'rb')
  Dills = pickle.load(f)
  return Dills

# This class converts CIF or POSCAR files into ASE Atoms objects
# Warning: Only works with ASE versions after ~3.17
class CIF_CAR_ASE:

  if version.parse(ase.__version__) > version.parse("3.17"):
    continue
  else:
    raise VersionError(ase.__version__)

  def __init__(self, filename, filetype):
      """
      Parameters:
      * filename (string): A title for a CIF or POSCAR file (please include directory in title)
      * filetype (string): A file type string, such as POSCAR, CONTCAR, or CIF (case is irrelevant)
      """
      self.filetype = filetype
      self.name = filename

  def convert(self, check):
      """
      Parameters:
      * check (Bool): If True, returns an ASE interactive view of the atoms object (does not work in Google Collab)
      Returns: 
      * out (ASE Atoms object): the output atom stored in the init file
      """
      # holds our atoms object temporarily
      ASE_temp = []
  
      # Process cif files into ASE objects
      if self.filetype.lower() == "cif":
          test = parse_cif_ase(self.name)
          # Check to see how many things are in the parsed file
          for block in test:
            ASE_temp.append(block.get_atoms())
          
          # Lets us know if there are too many items in file or if we have a good output
          if len(ASE_temp) != 1:
              print("cif file contains too many entries")
          else:
              out = ASE_temp[0]
      # Process vasp files into ASE atoms
      elif self.filetype.lower() == "poscar" or self.filetype.lower() == "contcar":
          out = read_vasp(self.name)

      # Provide view to user on deman
      if check == True:
          view(out)
          print("view created")

      return out