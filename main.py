from sys import stderr
from bridge_main import bridge_main
from loguru import logger

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")

if __name__ == '__main__':
    while True:
        print('Выбери действие: ')
        print('1. Официальный мост')
        print('0. Закончить работу')

        nomer = int(input('Номер действия: '))

        if nomer == 1:

            parametrs = {
                'count_min': 1,
                'count_max': 1,
            }

            bridge_main(nomer, parametrs)

        else:
            break

    print("Скрипт закончил работу!!!")