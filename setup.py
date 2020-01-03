import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdmlib",
    version="0.1.2",
    author="Alex Van de Kleut",
    author_email="avandekleut@gmail.com",
    description="A fast, numpy-based implementation of Kanerva's Sparse \
    Distributed Memory (SDM)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avandekleut/sdmlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'scipy'],
    python_requires='>=3.7',
)
