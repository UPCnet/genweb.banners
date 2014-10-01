# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.8.dev0'

README = open("README.rst").read()
HISTORY = open(os.path.join("docs", "HISTORY.rst")).read()

setup(
    name='genweb.banners',
    version=version,
    description='Extra content and utilities for Genweb',
    long_description=README + "\n" + HISTORY,

    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
    ],
    author='Carles Bruguera',
    author_email='carles.bruguera@upcnet.es',
    url='https://github.com/plone/genweb.banners',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['genweb', ],
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'five.grok',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
