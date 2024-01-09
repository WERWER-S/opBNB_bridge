import json
import time
import random
from tqdm import tqdm
from config import PAUSA_MIN, PAUSA_MAX
from typing import Optional


def read_json(path: str, encoding: Optional[str] = None) -> list | dict:
    return json.load(open(path, encoding=encoding))


def sleeping(ot=PAUSA_MIN, do=PAUSA_MAX):
    x = random.randint(ot, do)
    for _ in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)


with open('keys.txt', 'r') as keys_file:
    accounts = [line.strip() for line in keys_file.readlines()]