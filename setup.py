from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="convertio",
      version="1.1.1",
      description="An API wrapper for convertio.co",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="PetitPotiron",
      packages=["convertio"],
      license="GNU General Public License v3.0",
      url='https://github.com/PetitPotiron/python-convertio/'
      )
