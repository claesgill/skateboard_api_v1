import numpy as np
from src.util.helpers import load_all

def basic_flip() -> str:
    stances, rotations, _, flips, _, _ = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    flip = np.random.choice(flips)
    return {"payload": f"{stance} {flip}".strip() }

def basic_grind() -> str:
    stances, rotations, _, _, grinds, _ = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    rotation = np.random.choice(rotations)
    grind = np.random.choice(grinds)
    return {"payload": f"{stance} {rotation} {grind}".strip() }

def basic_manual() -> str:
    stances, rotations, _, _, _, manuals = load_all()
    stance = np.random.choice(stances)
    stance = stance if stance != "Normal" else ""
    manual = np.random.choice(manuals[0:2])
    return {"payload": f"{stance} {manual}" }
