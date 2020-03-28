from os import path

from setuptools import find_namespace_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="bitbucket-webhooks",
    version="0.0.9",
    description="Routes bitbucket webhook API event payloads to consumable decorators with payload serialized to python objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mukund-murali/bitbucket-webhooks",
    author="Mukund Muralikrishnan",
    author_email="mukund.muralikrishnan@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="bitbucket webhooks development git",
    packages=find_namespace_packages(include=["bitbucket_webhooks"]),
    python_requires=">=3.5",
    install_requires=["marshmallow-objects>=2.2.2", "marshmallow>=3.0.0"],
    extras_require={"dev": ["pytest", "black", "isort", "flake8", "mypy"]},
    project_urls={
        "Bug Reports": "https://github.com/mukund-murali/bitbucket-webhooks/issues",
        "Source": "https://github.com/mukund-murali/bitbucket-webhooks",
    },
)
