import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="belqis", # Replace with your own username
    version="0.0.2",
    author="Ahmed Khorsi",
    author_email="ahmedkhorsi18@gmail.com",
    description="A python client for Belqis System",
    long_description="Allows you to query the services of Belqis system from a python program",
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedkhorsi/pybelqis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
