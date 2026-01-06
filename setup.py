from setuptools import find_packages,setup
from typing import List

hyphen_dot_e="-e ."
def get_requirements(file_path:str) ->List[str]:
    requirements=[]
    with open(file_path) as temp_file:
        requirements=temp_file.readlines()
        [req.replace("\n","") for req in requirements]

        if hyphen_dot_e in requirements:
            requirements.remove(hyphen_dot_e)

setup(
    name="mlprojects",
    version='0.0.1',
    author='Ayush',
    author_email='ayukhanalsh100@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)