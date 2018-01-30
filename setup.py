#!/usr/bin/env python3.6

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='codename',
    version='1.1',
    description='Codename generator. Credits to "projectcodename.com".',
    long_description=long_description,
    url='https://github.com/and3rson/codename',
    author='Andrew Dunai',
    author_email='a@dun.ai',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='python project codename generator code name',
    packages=['codename'],
    entry_points={
        'console_scripts': [
            'codename=codename:main'
        ]
    }
)

