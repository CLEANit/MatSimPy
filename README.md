This repo stores Python functions and classes that help with materials science work.  Particularly for ASE and Networkx, but also with VASP and (Work-in-Progress) OVITO.

Edit 1-5-2022: Further documentation pending!

## Documentation:

### io.py

Class CIF_CAR_ASE is used for converting CIF and Vasp (CONTCAR, POSCAR) files to the ASE atoms object representation.  It is typically used as follows, after importing a file in need of conversion.

> extracted_CIF = CIF_CAR_ASE(file_path, "FILE_EXTENSION")<br>ASE_Extracted = extracted_CIF.convert(False)

File extensions in this case are CIF, CONTCAR, or POSCAR, ignoring case.  Feeding .convert 'True' will result in an attempt by ASE to create a visualization of the converted atoms object.  Please note that at this time, only the default view mode is implemented and it will not run in Google Colab as of last check.
