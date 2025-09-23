from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="MULTI_AI AGENT",
    version="0.1.0",
    author = "Abdullah",
    packages=find_packages(),
    install_requires=requirements,
)