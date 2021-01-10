import os
import re

from setuptools import setup

name = 'easytalk'

def get_version(package=name):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)

def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()

def get_packages(package=name):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name="easytalk",
    version=get_version(),
    description="Manage your Postgres Database with user-frienldy queries",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/romainledru/Postgres-EasyTalk",
    author="Romain Ledru",
    author_email="romain.ledru2@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=get_packages(),
    include_package_data=True,
    install_requires=["psycopg2-binary"],
    entry_points={
        "console_scripts": [
            "welcome=easytalk.__main__:main",
        ]
    },
)