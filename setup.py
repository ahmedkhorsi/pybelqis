from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pybelqis",
    version="0.3.1",
    author="Ahmed Khorsi",
    author_email="ahmedkhorsi18@gmail.com",
    description="A python client for Belqis Systems",
    long_description="Allows you to query the services of Belqis system from a python program",
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedkhorsi/pybelqis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
