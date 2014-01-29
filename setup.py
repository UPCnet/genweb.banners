# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


version = '0.1'
description = 'Extra content and utilities for Genweb'
long_description = open('README.rst').read() + open('HISTORY.rst').read() + \
    open('LICENSE').read()


setup(
    name='genweb.banners',
    version=version,
    description=description,
    long_description=long_description,
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
        'z3c.jbot'
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
