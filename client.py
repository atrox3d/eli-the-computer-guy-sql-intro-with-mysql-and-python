from datetime import datetime
from datetime import UTC
from time import sleep

from options import parse_args
from database import (
    exec_statement,
    MySQLConnection
)

def get_last_temp(db:MySQLConnection=None) -> int:
    ''' returns last temp inserted on db '''

    result = exec_statement(
        '''
        select * from temp
        order by timestamp desc
        limit 1
        ''',
        db
    )
    print(f'GET_LAST_TEMP| {result = }')
    return result[0]

def check_loop(count:int, max_loop:int) -> bool:
    if max_loop is None:
        return True
    elif count < max_loop:
        return True
    else:
        return False

if __name__ == "__main__":
    options = parse_args()
    # TODO: localize timestamp and use it
    # TODO: instead of id
    # last_timestamp = datetime.now(UTC)
    # print(last_timestamp)
    last_id = 0
    count = 0
    while check_loop(count, options.max):
        id, temp, timestamp = get_last_temp()
        # TODO: localize timestamp and use it
        # TODO: instead of id
        # if timestamp > last_timestamp:
        if id > last_id:
            print('INFO| found new record: ', id, temp, timestamp)
            last_id = id
        else:
            print('INFO| no new record found')
        sleep(options.interval)
        count += 1

