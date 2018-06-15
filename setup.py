from setuptools import setup, find_packages
from os import path
import os

here = path.abspath(path.dirname(__file__))

# long description from the README file

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


long_description = read('README.md')

setup(
    name='pyconfigstore',
    version='1.0.0',
    description=(
        'A Python module for handling config files. It helps handles persist config files and also giving the ability to set, get, update and delete config settings'
          ' its based on Configstore.js'
    ),
    long_description=long_description,
    license='MIT',
    url='https://github.com/CITGuru/ConfigStore',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: '
        'Libraries :: Application Frameworks',
    ],
    keywords='config, settings, .env, json, settings, configstore',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Oyetoke Toby',
    download_url='https://github.com/CITGuru/ConfigStore/archive/1.0.0.tar.gz',
    install_requires=[],
    author_email='oyetoketoby80@gmail.com',
)
