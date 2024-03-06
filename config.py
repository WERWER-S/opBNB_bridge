import os
import sys
import random
from pathlib import Path

PAUSA_MAX = 30
PAUSA_MIN = 10

if getattr(sys, 'frozen', False):
    directory_path = Path(sys.executable).parent.absolute()
else:
    directory_path = Path(__file__).parent.parent.absolute()

absolute_path = directory_path.absolute()

ABIS_DIR = os.path.join(absolute_path, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
BRIDGE_ABI = os.path.join(ABIS_DIR, 'bridge.json')

value = random.uniform(0.001, 0.0015) #Your amount to bridge
