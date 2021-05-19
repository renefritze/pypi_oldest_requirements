import contextlib
import os
import sys
from pathlib import Path


@contextlib.contextmanager
def cd(path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    except:
        print('Exception caught: ', sys.exc_info()[0])
    finally:
        os.chdir(cwd)


def cd_common_base_dir(paths):
    basedir = set(Path(r).resolve().parent for r in paths)
    if len(basedir) != 1:
        raise RuntimeError(f"Paths must have same basedir: {paths}")
    return cd(basedir.pop())
