#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptest import test

setup(
    name='example_project',
    version='0.3-dev',
    description='test',
    author='test',
    packages=find_packages(),
    cmdclass={'test': test}
)
