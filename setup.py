import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="STATSTools_by_dropout",
    version="0.0.1",
    author="drop-out",
    author_email="drop-out@foxmail.com",
    description="statistics tools including bootstrap...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drop-out/STATS-Tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)