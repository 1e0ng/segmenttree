#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'segmenttree',
    version = '0.0.6',
    keywords = ('segment', 'tree'),
    description = 'A Python implementation of Segment Tree',
    license = 'MIT License',

    url = 'http://liangsun.org',
    author = 'Liang Sun',
    author_email = 'i@liangsun.org',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)
