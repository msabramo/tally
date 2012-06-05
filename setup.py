# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name="tally",
    version=":versiontools:tally:",
    url='http://github.com/d0ugal/tally',
    license=license,
    description="Python Analytics powered by Redis, Flask and D3",
    long_description=readme,
    author='Dougal Matthews',
    author_email='dougal85@gmail.com',
    setup_requires=[
        'versiontools >= 1.6',
    ],
    test_suite="nose.collector",
    tests_require=[
        'Flask-Testing',
        'mock',
        'nose',
        'unittest2',
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    zip=False,
    entry_points="""[console_scripts]
        tally_web= tally.web.__main__:main
    """,
    install_requires=requirements
)
