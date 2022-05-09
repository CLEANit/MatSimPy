from setuptools import setup, find_packages

setup(
    name='Materials Science Simulation Tools for Python',
    url='https://github.com/CLEANit/MatSimPy',
    author='Christoff Reimer',
    author_email='Christoff.Reimer@uottawa.ca',
    packages=find_packages(),
    install_requires=['numpy', 'copy', 'pickle', 'itertools', 're', 'collections', 'ase', 'networkx', 'ovito'],
    version='0.1',
    license='MIT',
    description='A python package for materials science from pre-existing code',
    long_description=open('README.txt').read(),
)
