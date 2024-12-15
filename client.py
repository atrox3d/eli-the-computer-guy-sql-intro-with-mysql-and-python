from datetime import datetime
from datetime import UTC
from time import sleep

from options import parse_args
from database import (
    exec_statement,
    MySQLConnection
)

def get_last_temp(db:MySQLConnection=None) -> int:
    result = exec_statement(
        '''
        select * from temp
        order by timestamp desc
        limit 1
        ''',
        db
    )
    return result[0]

if __name__ == "__main__":
    options = parse_args()
    # last_timestamp = datetime.now(UTC)
    # print(last_timestamp)
    last_id = 0
    count = 0
    while True:
        if options.max is not None:
            if count >= options.max:
                break
        id, temp, timestamp = get_last_temp()
        # if timestamp > last_timestamp:
        print(id, last_id)
        if id > last_id:
            print(id, temp, timestamp)
            last_id = id
        sleep(options.interval)
        count += 1

