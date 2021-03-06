#!/usr/bin/env python
# -*- coding: utf-8 -*-


import setuptools
requirements = [
    "gtfparse>=1.2.1",
    "validators>=0.18.2"
]

setuptools.setup(
    name = 'lrgasp',
    version = '0.5.0',
    description = "LRGASP tools",
    long_description = "LRGASP tools for submission",
    author = "Mark Diekhans",
    author_email = 'markd@ucsc.edu',
    url = 'https://github.com/LRGASP/lrgasp-submissions',
    scripts=[
        'bin/lrgasp-validate-experiment-metadata',
        'bin/lrgasp-validate-expression-matrix',
        'bin/lrgasp-validate-gtf',
        'bin/lrgasp-validate-read-model-map',
        'bin/lrgasp-validate-team-metadata',
    ],
    packages = [
        'lrgasp',
    ],
    package_dir = {'': 'lib'},
    include_package_data = True,
    install_requires = requirements,
    license = "MIT",
    zip_safe = True,
    keywords = ['Bioinformatics', 'genomics', 'transcriptomics'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.7',
)
