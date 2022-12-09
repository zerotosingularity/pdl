from setuptools import setup

exec(open('pdl/version.py').read())


setup(
    name="pdl",
    version=__version__,
    author="Jan Van de Poel",
    author_email="jan.vandepoel@seeme.ai",
    install_requires=['requests>=2.18.4'],
    url="https://github.com/zerotosingularity/pdl",
    description="Public Download Library",
    long_description="Download public datasets & files in one line of code",
    license="MIT",
    packages=['pdl']
)
