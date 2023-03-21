from setuptools import find_packages, setup

with open("requirements.txt") as install_requires_file:
    requirements = install_requires_file.read().strip().split("\n")

setup(
    name="utilities",
    description="Custom modules for Prefect flows",
    license="Apache License 2.0",
    author="Austin Weisgrau",
    author_email="data@workingfamilies.org",
    long_description_content_type="text/markdown",
    version="1.0",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.10",
    install_requires=requirements,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
