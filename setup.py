"""
Setup configuration for PleasQLarify
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text(encoding="utf-8").strip().split("\n")

setup(
    name="pleasqlarify",
    version="1.0.0",
    author="Robin Shing Moon Chan",
    author_email="",
    description="Interactive SQL Query Clarification System for End Users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chanr0/pleasqlarify",
    project_urls={
        "Bug Reports": "https://github.com/chanr0/pleasqlarify/issues",
        "Source": "https://github.com/chanr0/pleasqlarify",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pleasqlarify=pleasqlarify.__main__:main",
        ],
    },
    keywords="sql query clarification database hci visualization",
    include_package_data=True,
)
