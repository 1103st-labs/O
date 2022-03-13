"""
The output module, should probably be replaced by logging.
"""
import sys
LEVEL = 2

def log(sevarity: str, message: str, level: int) -> None:
    """
    logs a message to the appopreate output with the corect format.
    :args sevarity: 'warn', 'err', or 'info', the prior goes to stderr the
    other to stdout.
    :args message: The message to log.
    :args level: How detailed the message is, 0 is the most general.
    """
    if (level > LEVEL):
        return
    if (sevarity == "warn"):
        print(f'WARN:{level}: {message}', file=sys.stderr)
    if (sevarity == "err"):
        print(f'ERR{level}:: {message}', file=sys.stderr)
    if (sevarity == "info"):
        print(f'INFO:{level}: {message}')

def info(message: str, level: int) -> None:
    """
    Wraper for log.
    :args message: The message to log.
    :args level: How detailed the message is, 0 is the most general.
    """
    log("info", message, level)

def warn(message: str, level: int) -> None:
    """
    Wraper for log.
    :args message: The message to log.
    :args level: How detailed the message is, 0 is the most general.
    """
    log("warn", message, level)

def err(message: str, level: int) -> None:
    """
    Wraper for log.
    :args message: The message to log.
    :args level: How detailed the message is, 0 is the most general.
    """
    log("info", message, level)

def table(keys: list[str], *rows: list[list[str]]) -> None:
    """
    Prints keyed information.

    :args keys: The headers of the table.
    :args rows: lists of lists ordered by the values in keys.
    """
    for row in rows:
        print("DATA::")
        for key, value in keys, row:
            print(f'    {key}: {value}')

def section(name: str, bold: bool = False) -> None:
    """
    Prints a section title.

    :args name: name of the section.
    :args bold: add extra omph.
    """
    print(f'SECTION: {name}')

def bar(step_count: int) -> None:
    """
    Displays a loading bar.

    :args step_count: How many steps in the process.
    """
    for x in range(step_count):
        yield x

