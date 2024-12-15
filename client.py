from datetime import datetime
from datetime import UTC
from time import sleep

from database import (
    drop_table,
    create_table_temp, 
    get_db, 
    exec_statement,
    MySQLConnection
)

db = get_db()

def get_last_temp(db:MySQLConnection) -> int:
    result = exec_statement(
        db,
        '''
        select * from temp
        order by timestamp desc
        limit 1
        '''
    )
    return result[0]

if __name__ == "__main__":
    # last_timestamp = datetime.now(UTC)
    # print(last_timestamp)
    last_id = 0
    while True:
        id, temp, timestamp = get_last_temp(db)
        # if timestamp > last_timestamp:
        print(id, last_id)
        if id > last_id:
            print(id, temp, timestamp)
            last_id = id
        sleep(3)