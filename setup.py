from setuptools import setup

setup(
    name="pdl",
    version="0.8.13",
    author="Zero to singularity",
    author_email="jan@zerotosingularity.com",
    install_requires=['requests>=2.18.4'],
    url="https://github.com/zerotosingularity/pdl",
    description="Python Download Lib",
    long_description="Easily download and explore public datasets.",
    license="MIT",
    packages=['pdl']
)
