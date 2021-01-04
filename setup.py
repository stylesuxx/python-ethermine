"""Setup ethermine library."""

from setuptools import find_packages, setup
setup(
    name='ethermine',
    packages=find_packages(include=['ethermine']),
    version='0.1.0',
    description='Ethermine python wrapper',
    author='stylesuxx@gmail.com',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)