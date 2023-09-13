from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Customer Personality'
VERSION = '0.0.1'
AUTHOR = 'Priya'
DESCRIPTION = 'End to End ML Project for customer Personality'
HYPHEN_E_DOT = '-e .'
FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    with open(FILE_NAME) as f:
        requirement_list = f.readlines()
        requirement_list = [x.replace('\n','') for x in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    author_email='priya1803.singh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements_list()
)