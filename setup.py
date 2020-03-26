#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

from django_flexible_manifest_staticfiles import __version__

setup(
    name='django-flexible-manifest-staticfiles',
    version=__version__,
    author='Tom Anthony',
    author_email='django@tomanthony.co.uk',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/TomAnthony/django-flexible-manifest-staticfiles',
    license='MIT',
    description='An extension of Django ManifestStaticFilesStorage that allows ignoring (excluding) specified files from being versioned, such as images or fonts.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
)
