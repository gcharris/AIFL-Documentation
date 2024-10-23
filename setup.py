# setup.py
from setuptools import setup, find_packages

setup(
    name="aifl",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'flask>=2.2.2',
        'python-dotenv>=0.19.0',
        'openai>=1.0.0',
        'cryptography>=3.4.7',
        'lark-parser>=0.11.3',
        'requests>=2.26.0',
    ],
    python_requires='>=3.7',
)