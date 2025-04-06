from setuptools import setup,find_packages


with open("requirements.txt") as f:
    requirements=f.read().splitlines()


setup(
    name="MLOps-Project-1",
    version="0.1",
    author="Tilak Varma",
    packages=find_packages(),
    description="Founder of MxA",
    install_requires=requirements 
)

