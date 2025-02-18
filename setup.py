from setuptools import find_packages,setup
from typing import List

HYPEN='-e .'

def get_requirements(file_path:str)->List[str]:
    '''this function return list requirements'''

    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)
    return requirements

setup(
    name='googleplaystore',
    version='0.0.1',
    author='Arya',
    author_email='khadkaarya15@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)