"""
Installs a repo, source, or package.
"""
import argparse as ap
from dataclasses import is_dataclass
import errors
import re
import urllib.request as request
import json
import out as o
import state

INSTALL_TYPES = ["repo", "source", "package"]
EXPORT_TYPES = ["cli", "gui", "service", "internal"]
STATE = []
ENV = {}

def install_repo(uri: str) -> None:
    """
    Installs a repo from a uri.

    :args uri: The uri to pull from.
    """
    o.info("Checking uri validity.", 5)
    if (not re.search(r'https?:\/\/[\w./:]*', uri)):
        raise errors.ORunErr("Malformed Repo URI.")
    try:
        o.info(f'Requesting data from {uri}.', 2)
        with request.urlopen(uri) as res:
            ## TODO check 404?
            data = json.loads(res.read(), cls=state.OJSONDecoder)
            o.info(f'Got the folowing data: {data}', 3)
    except Exception as e:
        raise errors.ORunErr(f"Could not fetch repo info: {e}")
    STATE.append(data)
    o.info("Added Source.", 1)

def install_source(uri: str) -> None:
    """
    Installs a source image and sets it up.

    :args uri: The uri or short-name.
    """
    repo = None
    source = None
    o.info("Checking to see if source is a short name or a uri.", 5)
    search1 = re.search(r'(https?:\/\/[\w./:]*)\|\|(\w*)', uri)
    search2 = re.search(r'(\w*)', uri)
    if (search1):
        repo = search1[1]
        source = search1[2]
        o.info("It is a URI.", 5)
    elif (search2):
        source = search2[1]
        o.info("It is a short name.", 5)
    else:
        raise errors.ORunErr("Malformed Repo URI or short name.")
    if (repo is None):
        o.info(f"Searching installed repos for {source}.", 2)
        all_sources = [x.get("sources", {"short_name": ""}) for x in STATE]
        all_sources = [x.__dict__ if (is_dataclass(x)) else x for
                x in all_sources]
        all_sources = [x.short_name for x in all_sources]
        if (source in all_sources):


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
                 choices=EXPORT_TYPES)
    args = parser.parse_args(sub_cmd.split())
    print(STATE)


if __name__ == "__main__":
    resolve(input("reslolve? "))
