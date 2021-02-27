import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notebook-bogdanmagometa", # Replace with your own username
    version="0.0.1",
    author="Bohdan Mahometa",
    author_email="bohdan.mahometa@ucu.edu.ua",
    description="A Python project emulating a notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bogdanmagometa/notebook",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
)
