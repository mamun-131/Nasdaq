#this is my pre build setup code to install any app

from setuptools import find_packages, setup
from typing import List

def find_requirements(path:str)->List[str]:
    requirements=[]
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements



setup(
name = 'ask_market_Data',
version = '0.0.1',
author='Md Mamunur Rahman',
author_email='mamun131@gmail.com',
packages=find_packages(),
install_requires=find_requirements('requirements.txt'),


)