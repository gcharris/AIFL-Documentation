# setup.py
from setuptools import setup, find_packages

setup(
    name="aifl",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'lark>=1.1.5',
        'pytest>=7.0.0'
    ],
    python_requires='>=3.7',
)