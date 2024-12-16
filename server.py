from typing import Generator
from time import sleep
from random import randint

from database import (
    drop_table,
    exec_statement,
    MySQLConnection
)
from options import parse_args

def create_table_temp(db:MySQLConnection=None):
    print(f'CREATE_TABLE_TEMP| creating table temp')
    result = exec_statement(
        '''
        create table if not exists temp(
            id int auto_increment primary key,
            temp int,
            timestamp timestamp default now()
        )
        ''',
        db
    )
    print(f'CREATE_TABLE_TEMP| {result = }')

def get_temperature(max_loops:int|None=None) -> Generator[int, None, None]:
    ''' generates infinite or max_loops random temperatures'''
    count = 0
    while True:
        if max_loops is not None:
            if count >= max_loops:
                return
        yield randint(0, 100)
        count += 1

def insert_temperature(temp:int, db:MySQLConnection=None):
    print(f'INSERT_TEMPERATURE| inserting {temp}')
    result = exec_statement(
            f'''
            insert into temp
                (temp)
            values ({temp})
            ''',
            db
    )

def reset_temp_table(db:MySQLConnection=None):
    ''' resets temp table '''
    drop_table('temp', db)
    create_table_temp(db)

if __name__ == "__main__":
    options = parse_args()
    print(options)

    reset_temp_table()

    for t in get_temperature(options.max):
        insert_temperature(t)
        sleep(options.interval)
