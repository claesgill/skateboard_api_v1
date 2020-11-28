import numpy as np

def load_file(fname) -> np.array:
    with open(fname, "r") as f: 
        data = [line.strip("\n") for line in f.readlines()]
    return np.array(data)   

def load_all() -> list:
    """Returns:
        list: [stances, rotations, degrees, flips, grinds, manuals]
    """
    stances   = load_file("data/stances.txt")
    rotations = load_file("data/rotations.txt")
    degrees   = load_file("data/degrees.txt")
    flips     = load_file("data/flips.txt")
    grinds    = load_file("data/grinds.txt")
    manuals   = load_file("data/manuals.txt")
    return (stances, rotations, degrees, flips, grinds, manuals)