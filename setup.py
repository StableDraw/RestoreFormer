from setuptools import setup, find_packages

import json
import os

def read_pipenv_dependencies(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]

if __name__ == '__main__':
    setup(
        name='restoreformer',
        version=os.getenv('PACKAGE_VERSION', '1.0.0'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'restoreformer'
        ]),
        description='RestoreFormer',
        install_requires=[
              *read_pipenv_dependencies('Pipfile.lock'),
        ]
    )