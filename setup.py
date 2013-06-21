#!/usr/bin/env python

import os
try:
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'activitystreams',
    version = '0.0',
    description = 'Activity Streams Parser for Python',
    author = 'Martin Atkins',
    license = read('LICENSE'),
    url = 'https://github.com/apparentlymart/activity-streams-python',
    packages = ['activitystreams'],
)
