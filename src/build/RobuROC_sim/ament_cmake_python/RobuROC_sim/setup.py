from setuptools import find_packages
from setuptools import setup

setup(
    name='RobuROC_sim',
    version='0.0.0',
    packages=find_packages(
        include=('RobuROC_sim', 'RobuROC_sim.*')),
)
