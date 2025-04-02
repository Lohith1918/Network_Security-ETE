'''
The setup.py file is a Python script used in packaging and distributing Python projects.
It serves as a configuration file that defines essential metadata about the project, specifies dependencies,
and provides instructions for building, installing, and distributing the package.

'''
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()

            for line in lines:
                requirements=line.strip()
    