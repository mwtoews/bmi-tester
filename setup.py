#! /usr/bin/env python
from setuptools import find_packages, setup


def read(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read()


long_description = u"\n\n".join(
    [read("README.rst"), read("CREDITS.rst"), read("CHANGES.rst")]
)


setup(
    name="bmi-tester",
    version="0.5.6.dev0",
    author="Eric Hutton",
    author_email="eric.hutton@colorado.edu",
    url="https://github.com/csdms/bmi-tester",
    description="Test Python BMI bindings.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=["bmi"],
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["bmi-test=bmi_tester.bmipytest:main"],
        "bmi.plugins": ["bmi_test=bmi_tester.bmipytest:configure_parser_test"],
    },
)
