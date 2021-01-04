"""Setup ethermine library."""

from setuptools import find_packages, setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='ethermine',
    packages=find_packages(include=['ethermine']),
    version='0.2.0',
    description='Ethermine API python wrapper',
    long_description=long_description,
    author='Chris Landa',
    author_email='stylesuxx@gmail.com',
    url='https://github.com/stylesuxx/python-ethermine',
    license='MIT',
    keywords=['ethermine', 'etherium', 'eth'],
    install_requires=['requests'],
    setup_requires=['pytest-runner', 'pypandoc'],
    tests_require=['pytest'],
    test_suite='tests',
)
