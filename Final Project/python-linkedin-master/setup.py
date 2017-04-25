#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from linkedin import __version__


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(name='python-linkedin',
      version=__version__,
      description='Python Interface to the LinkedIn API',
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Natural Language :: English',
      ],
      keywords='linkedin python',
      author='Ozgur Vatansever',
      author_email='ozgurvt@gmail.com',
      maintainer='Marshall Humble',
      maintainer_email='humblejm@gmail.com',
      url='https://github.com/marshallhumble/python-linkedin',
      license='MIT',
      packages=['linkedin'],
      install_requires=['requests>=2.8.1', 'requests-oauthlib>=0.5.0'],
      zip_safe=False
)
