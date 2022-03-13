"""
Defines the package interface for use betwene modules in O+
"""

from dataclasses import dataclass, Field
from datetime import datetime

@dataclass
class Package():
    """
    Represents a Package.
    """
    package_name: str
    description: str
    version: str
    export_type: str
    install_date: datetime
    _package: int = 1

