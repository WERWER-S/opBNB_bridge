import os
import random
from pathlib import Path

PAUSA_MAX = 30
PAUSA_MIN = 10
# Создаем объект Path для директории
directory_path = Path("C:/Users/NAME/Desktop/opBNB bridge") #Тут твой путь

absolute_path = directory_path.absolute()

ABIS_DIR = os.path.join(absolute_path, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
BRIDGE_ABI = os.path.join(ABIS_DIR, 'bridge.json')

value = random.uniform(0.001, 0.0015)
