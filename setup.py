# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_sitemap import __version__


setup(
    name='aldryn-sitemap',
    version=__version__,
    description=open('README.rst').read(),
    author='what.digital',
    author_email='None',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
