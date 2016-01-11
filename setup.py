#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'segmenttree',
    version = '1.0.2',
    keywords = 'segment tree',
    description = 'A Python implementation of Segment Tree',
    license = 'MIT License',

    url = 'https://leons.im/posts/a-python-implementation-of-segment-tree/',
    author = '1e0n',
    author_email = 'i@leons.im',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)
