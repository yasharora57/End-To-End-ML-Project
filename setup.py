from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        #while reading the requirements.txt file line by line, it will also read the new line character 
        #that is why we are replacing the new line character with a blank

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='End To End ML Project',
version='1.0.0',
author='Yash',
author_email='yasharoraedws@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

#find_packages() will find all the packages in this folder, for eg, src folder in this case since its a package
#If we write "-e ." in the requirements.txt file, it points out directly to the setup.py
#after making this file, we will run requirements.txt in the command prompt 