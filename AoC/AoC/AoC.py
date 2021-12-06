from itertools import islice
import re, math
from collections import defaultdict, Counter
from pathlib import Path


# Parsen von String in int List und float List
RE_INT   = re.compile(r"\d+")
RE_FLOAT = re.compile(r"\d?\.\d+")

def ints(s: str):
    return list(map(int, RE_INT.findall(s)))

def floats(s: str):
    return list(map(float, RE_FLOAT.findall(s)))


# ----Hier für die zum auslesen der Dateien
def resolve_path(**kwargs) -> Path:
    for folder in kwargs.get("folders", ["inputs/{day}", "."]):
        path = Path(folder.format(**kwargs)) / "input"
        if path.exists():
            return path

def read_string(**kwargs):
    with open(resolve_path(**kwargs)) as file:
        return file.read()

def read_lines(**kwargs):
    return read_string(**kwargs).splitlines()

#def read_grid(f=identity, **kwargs):
#    return [list(map(f, line)) for line in read_lines(**kwargs)]