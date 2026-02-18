"""
{{ cookiecutter.pypi_package_name }} module
"""
from typing import List
from importlib.metadata import version, PackageNotFoundError



__all__: List[str] = []
__copyright__: str = 'Copyright 2026, {{ cookiecutter.full_name }} ({{ cookiecutter.email }})'
try:
    __version__ = version('{{ cookiecutter.pypi_package_name }}')
except PackageNotFoundError:
    __version__ = '0.0.0'
