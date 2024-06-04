from setuptools import setup, find_packages

setup(
    name="acronym",
    version="0.1.0",
    packages=find_packages(where="src"),
    py_modules=["main"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "acronym=main:main",
        ],
    },
    install_requires=[
        "pyyaml",
    ],
    author="Elijah Blackmore",
    description="A tiny terminal learning tool for memorising acronyms.",
    url="https://github.com/elijahblackmore/acronym",
)
