from setuptools import find_packages, setup
from typing import List


HYPHON_E_DOT = "-e ."


def get_requirements(filepath: str) -> List[str]:
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHON_E_DOT in requirements:
        requirements.remove(HYPHON_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Rakesh",
    author_email="rakeshhalijol@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
