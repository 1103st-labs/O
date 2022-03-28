"""
Module for saving and loading the state of the package manager.
"""

import json
import dataclasses
from structs.repo import Repo
from structs.source import Source
from structs.package import Package
import datetime
import out
import os
import errors

class OJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if (dataclasses.is_dataclass(o)):
            out.info(f'Exported {o}', 5)
            return dataclasses.asdict(o)
        elif (isinstance(o, datetime.datetime)):
            return {"datetime": o.isoformat()}
        return super().default(o)

class OJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook,
                *args, **kwargs)
    def object_hook(self, obj):
        if ("_repo" in obj):
            tmp = Repo(**obj)
            out.info(f'Loaded {tmp}', 5)
            return tmp
        elif ("_source" in obj):
            tmp = Source(**obj)
            out.info(f'Loaded {tmp}', 5)
            return tmp
        elif ("_package" in obj):
            tmp = Package(**obj)
            out.info(f'Loaded {tmp}', 5)
            return tmp
        elif ("datetime" in obj):
            return datetime.datetime.fromisoformat(obj["datetime"])
        else:
            return obj

class State():
    """
    A state manager to load and save the state of the system.
    """
    def __enter__(self) -> dict:
        self.check_perm()
        try:
            with open(".ostate", "r") as f:
                self.ret = json.load(f, cls=OJSONDecoder)
            out.info("Using found .ostate", 2)
        except (json.JSONDecodeError, FileNotFoundError):
            out.warn("New .ostate created", 2)
            ret = {
                    "repos": []
                }
            self.ret = ret
        out.info(f'Loaded .ostate = \n {self.ret}', 3)
        return self.ret

    def __exit__(self, exc_type, exc_value, traceback):
        with open(".ostate", "w") as f:
            json.dump(self.ret, f, cls=OJSONEncoder)
            out.info(f'Saving to .ostate = \n {self.ret}', 3)

    def check_perm(self) -> None:
        """
        Checks to see if the nessary files are accessable. Raises
        :raises OStartUpErr: If the nessary permissions are not avalible.
        """
        out.info("Testing file access.", 4)
        if not(os.access("./", os.R_OK | os.W_OK)):
            raise errors.OStartUpErr("Can not read / write to home directory.")
