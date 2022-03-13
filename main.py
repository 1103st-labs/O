"""
The driver file for the cli.
"""
import state
import out

out.LEVEL = 5


if __name__ == "__main__":
    with state.State() as S:
        input("wait...")

