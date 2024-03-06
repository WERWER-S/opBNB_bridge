from web3 import Web3
from typing import Optional
import time
from loguru import logger
from client import Client
from config import BRIDGE_ABI
from utils import read_json
from models import TokenAmount
from models import BSC


class Bridge:

    def __init__(self, client: Client):
        self.client = client

        if self.client.network == BSC:
            self.router_address = Web3.to_checksum_address('0xF05F0e4362859c3331Cb9395CBC201E3Fa6757Ea')
            self.decimals = 18

    router_abi = read_json(BRIDGE_ABI)

    def bridge_to_opBNB(self, value: [int | float | str]):
        contract = self.client.w3.eth.contract(
            abi=Bridge.router_abi,
            address=self.router_address
        )
        amount = TokenAmount(value)
        try:
            tx = self.client.send_transaction(
                to=self.router_address,
                data=contract.encodeABI('depositETH',
                                        args=(
                                            1,
                                            '0x'
                                        )),
                value=amount.Wei
            )

            success_tx = self.client.verif_tx(tx)

            if success_tx:
                logger.info(f"https://bscscan.com/tx/{tx.hex()}")
                logger.success(f'[{self.client.address}][opBNB Bridge] Successfully bridge to opBNB')
            else:
                logger.error(f'[{self.client.address}][opBNB Bridge] bridge error to opBNB')
        except Exception as err:
            logger.error(f'[{self.client.address}][opBNB Bridge] bridge error to opBNB: {type(err).__name__} {err}')
