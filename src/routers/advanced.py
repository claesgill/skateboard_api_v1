import numpy as np
from src.util.helpers import load_all

def advanced_flip() -> str:
    stances, rotations, degrees, flips, grinds, _ = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    rotation = np.random.choice(rotations)
    degree = degrees[0]
    flip = np.random.choice(flips[0:9])
    return {"payload": f"{stance} {rotation} {degree} {flip}".strip() }

def advanced_grind() -> str:
    stances, rotations, degrees, flips, grinds, _ = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    degree = degrees[0]
    rotation = f"{np.random.choice(rotations)} {degree}"
    flip = f"{np.random.choice(flips[0:5])} {np.random.choice(rotations)}"
    rot_or_flip = np.random.choice([rotation, flip])
    grind = np.random.choice(grinds[0:9])
    return {"payload": f"{stance} {rot_or_flip} {grind}".strip() }

def advanced_manual() -> str:
    stances, _, degrees, flips, _, manuals = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    degree = degrees[0]
    flip = np.random.choice(flips[0:5])
    rot_or_flip = np.random.choice([degree, flip])
    manual = np.random.choice(manuals[0:2])
    return {"payload": f"{stance} {rot_or_flip} {manual}" }
