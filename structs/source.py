"""
Defines the source interface for use betwene modules in O+
"""

from dataclasses import dataclass, Field
from structs.package import Package
from datetime import datetime

@dataclass
class Source():
    """
    Represents a source.
    """
    short_name: str
    description: str
    image_uri: str
    image_version: int
    package_list_uri: str
    is_installed: bool
    last_update: datetime
    last_upgrade: datetime
    last_full_upgrade: datetime
    installed_packages: list[Package]
    _source: int = 1

