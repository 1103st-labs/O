"""
Contains the diffrent erros that can occure.
"""

class OStartUpErr(Exception):
    """
    Raised when O+ can not start.
    """
    ...

class ORunErr(Exception):
    """
    Raised when O+ can not run the asked action.
    """
    ...
