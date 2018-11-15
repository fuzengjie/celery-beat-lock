#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import sys
 

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
        name="django-celerybeat-lock",
        version="0.1.1",
        author="FuZongZong",
        author_email="linuxsvip@gmail.com",
        description="django celerybeat multiple nodes lock",
        long_description=long_description,
        license="Apache License",
        url="https://github.com/fuzengjie/celery-beat-lock",
        packages=find_packages(),
        install_requires=[],
        classifiers=[
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: Text Processing :: Indexing",
            "Topic :: Utilities",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
        ],
)
