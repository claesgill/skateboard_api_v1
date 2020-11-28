import numpy as np
from src.util.helpers import load_all

def insane_flip() -> str:
    stances, rotations, degrees, flips, _, _ = load_all()
    stance = np.random.choice(stances[1:])
    rotation = np.random.choice(rotations)
    degree = np.random.choice(degrees[0:2])
    flip = np.random.choice(flips[4:])
    return {"payload": f"{stance} {rotation} {degree} {flip}".strip() }

def insane_grind() -> str:
    stances, rotations, degrees, flips, grinds, _ = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    rotation = np.random.choice(rotations)
    second_rotation = np.random.choice(rotations)
    degree = np.random.choice(degrees[0:2])
    flip = np.random.choice(flips)
    grind = np.random.choice(grinds)
    return {"payload": f"{stance} {rotation} {degree} {flip} {second_rotation} {grind}".strip() }

def insane_manual() -> str:
    stances, rotations, degrees, flips, _, manuals = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    rotation = np.random.choice(rotations)
    degree = degrees[0]
    flip = np.random.choice(flips)
    manual = np.random.choice(manuals[0:2])
    return {"payload": f"{stance} {rotation} {degree} {flip} {manual}" }