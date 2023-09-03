from setuptools import  find_packages,setup     # find all pakages automatically
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This Function will return a list of requirements
    
    """
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()      # Readlines will returns a \n 
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
            

setup(
    name='fraud Detection at self checkout retail',
    version='0.0.1',
    author='Hitendra',
    author_email='hitendrakatre10@gmail.com',
    package=find_packages(),                                  # To search packages in current project folder
    install_requires=get_requirements('requirements.txt')     # To install all packages
    
    
    )