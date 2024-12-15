from typing import Generator
from time import sleep
from random import randint

from database import (
    drop_table,
    create_table_temp, 
    get_db, 
    exec_statement,
    MySQLConnection
)
from options import parse_args

db = get_db()

def get_temperature(max:int|None=None) -> Generator[int, None, None]:
    count = 0
    while True:
        if max is not None:
            if count >= max:
                return
        yield randint(0, 100)
        count += 1

def insert_temperature(db:MySQLConnection, temp:int):
    exec_statement(
            db,
            f'''
            insert into temp
                (temp)
            values ({temp})
            '''
    )
    db.commit()

def setup(db:MySQLConnection):
    drop_table(db, 'temp')
    create_table_temp(db)

if __name__ == "__main__":
    options = parse_args()
    print(options)

    setup(db)

    for t in get_temperature(options.max):
        print(t)
        insert_temperature(db, t)
        sleep(options.interval)

