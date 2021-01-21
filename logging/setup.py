# Code adapted from:
# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

from distutils.core import setup

# To create package:
# python setup.py sdist


setup(
    name="robot-garden-logging",
    version="0.0",
    packages=["logging-source",],
    license='MIT',
    long_description=open('README.txt').read(),
)