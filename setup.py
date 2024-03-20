from setuptools import setup, find_packages

import json
import os

def get_requirements(filename='requirements.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires

if __name__ == '__main__':
    setup(
        name='restoreformer',
        version=os.getenv('PACKAGE_VERSION', '1.0.0'),
        package_dir={'': 'RestoreFormer'},
        packages=find_packages('RestoreFormer'),
        description='RestoreFormer',
        install_requires=get_requirements()
    )