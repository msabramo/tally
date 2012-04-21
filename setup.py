# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="tally",
    version=":versiontools:tally:",
    url='http://github.com/d0ugal/tally',
    license=readme,
    description="Redis powered tally",
    long_description=readme,
    author='Dougal Matthews',
    author_email='dougal85@gmail.com',
    setup_requires=[
        'versiontools >= 1.6',
    ],
    test_suite="nose.collector",
    tests_require=[
        'nose',
        'unittest2',
    ],
    packages=find_packages(exclude=('tests', 'docs'))
)
