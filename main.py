"""
The driver file for the cli.
"""
import state
import out
from commands import install
import runtime

out.LEVEL = 5

if __name__ == "__main__":
    with state.State() as STATE:
        runtime.STATE = STATE
        install.resolve(input("resolve "))

