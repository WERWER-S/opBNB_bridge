import random
from utils import accounts, sleeping
from loguru import logger
from config import value
from models import BSC
from client import Client
from opBNB_bridge import Bridge
from web3.middleware import geth_poa_middleware


def bridge_main(nomer_puti, parametrs):

    max_acconts = len(accounts)
    parametrs['max_acconts'] = max_acconts

    count_max = parametrs['count_max']
    count_min = parametrs['count_min']

    for current_tranz in range(0, count_max):
        logger.info(f'Транзакция: {current_tranz+1}/{count_max}')
        current_account = 0

        for account in accounts:
            client = Client(private_key=account, network=BSC)
            client.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

            current_account += 1
            parametrs['current_account'] = current_account

            if (current_tranz+1) > random.randint(count_min, count_max):#проверка на кол-во
                continue

            if nomer_puti == 1:
                bridge_instance = Bridge(client=client)
                bridge_instance.bridge_to_opBNB(value=value)


            sleeping()
        sleeping(45, 60)
