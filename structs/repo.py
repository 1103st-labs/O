"""
Defines the repo interface for use betwene modules in O+
"""

from dataclasses import dataclass, Field
from structs.source import Source

@dataclass
class Repo():
    """
    Represents a Repo.
    """
    repo_uri: str
    repo_version: int
    repo_matainer: str
    repo_homepage: str
    sources: list[Source]
    _repo: int = 1
