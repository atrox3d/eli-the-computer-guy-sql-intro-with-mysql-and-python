from typing import Generator
from time import sleep
from random import randint

from database import create_table_temp, get_db

db = get_db()

def get_temperature(max:int|None=None) -> Generator[int, None, None]:
    count = 0
    while True:
        if max is not None:
            if count >= max:
                return
        yield randint(0, 100)
        count += 1

SLEEP_SECONDS = 2
if __name__ == "__main__":
    create_table_temp(db)
    for t in get_temperature(10):
        print(t)
        sleep(SLEEP_SECONDS)

