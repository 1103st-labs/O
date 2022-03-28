"""
Installs a repo, source, or package.
"""
import argparse as ap
from runtime import STATE, ENV
import errors
import re
import urllib.request
import json
import state

INSTALL_TYPES = ["repo", "source", "package"]
EXPORT_TYPES = ["cli", "gui", "service", "internal"]

def install_repo(uri: str):
    """
    Installs a repo from a uri.

    :args uri: The uri to pull from.
    """
    if (not re.search(r'https?:\/\/[\w./:]*', uri)):
        raise errors.ORunErr("Malformed Repo URI.")
    r = urllib.request.Request(uri, data=None,
            headers={'User-Agent': 'O+'})
    repo_json = urllib.request.urlopen(r).read().decode('utf-8')
    try:
        repo_json = json.loads(repo_json, cls=state.OJSONDecoder)
    except (json.JSONDecodeError, FileNotFoundError):
        raise errors.ORunErr("Malformed Repo Json.")
    STATE['repos'] = repo_json



def resolve(sub_cmd: str) -> None:
    """
    Takes the sub command args and and reloves it to the corect function.

    :args sub_cmd: The string that makes up the subcomand and its args.
    """
    parser = ap.ArgumentParser(prog="o install", description=__doc__)
    parser.add_argument("TYPE",
            help="The type of thing you want to install.",
            choices=INSTALL_TYPES, default="package")
    parser.add_argument("TARGET",
            help="The uri for the thing you want to install. If a full uri"
                 " is ommited, a search will be performed."
                 " EG: https://example.com/repo||source||package")
    parser.add_argument("--export",
            help="Inidcates how a package should be linked into the host"
                 " system.",
                 choices=EXPORT_TYPES, default=None)
    args = parser.parse_args(sub_cmd.split())
    if (args.TYPE == "repo"):
        install_repo(args.TARGET)
    elif (args.TYPE == "source"):
        install_source(args.TARGET)
    elif (args.TYPE == "package"):
        install_package(args.TARGET, args.export)


if __name__ == "__main__":
    resolve(input("reslolve? "))
