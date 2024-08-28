from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "Python package"
LONG_DESCRIPTION = "Python package with a slightly longer description"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="packagetest",
    version=VERSION,
    author="Author Name",
    author_email="<youremail@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where="src"),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "test package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
