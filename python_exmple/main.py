from random import randint
from time import sleep
from datetime import UTC, datetime as dt
import mysql.connector

config = dict(
    host='localhost',
    user='user',
    password='123',
    database='company',
    time_zone='+01:00'
)

db = mysql.connector.connect(**config)

def run_sql(sql, *values):
    cursor = db.cursor()
    cursor.execute(sql, values)
    # print(f'RUN_SQL| {cursor.statement}')
    result = cursor.fetchall()
    # print(f'RUN_SQL| {result = }')
    db.commit()
    cursor.close()
    return result

def setup_table():
    run_sql('drop table if exists temp')
    run_sql(
            '''
            create table if not exists temp(
                id int auto_increment primary key,
                temp int,
                -- timestamp timestamp default (UTC_TIMESTAMP)
                timestamp timestamp default CURRENT_TIMESTAMP
            )
            '''
    )

def insert_temp():
    temp = randint(0, 100)
    # print(f'INSERT_TEMP| {temp = }')
    sql = 'insert into temp(temp) values(%s)'
    values = (temp, )
    run_sql(sql, *values)

def get_last_temp():
    result, *_ = run_sql('select * from temp order by timestamp desc limit 1')
    # print(f'GET_LAST_TEMP| {result = }')
    return result

def get_stats():
    sql = '''
    select
        min(temp),
        max(temp),
        avg(temp)
    from (
        select temp from temp
        order by id desc
        limit 5
    ) as last5
    '''
    result, *_ = run_sql(sql)
    return result

setup_table()
while True:
    insert_temp()
    id, temp, timestamp = get_last_temp()
    now = dt.now().replace(microsecond=0)
    _min, _max, _avg = get_stats()
    with open('dashboard.html', 'w') as fp:
        header = '<meta http-equiv="refresh" content="5">'
        body = f'''
        <p>current temp {temp}</p>
        <p>min     temp {_min}</p>
        <p>max     temp {_max}</p>
        <p>avg     temp {_avg}</p>
        '''
        html = f'{header}{body}'
        fp.write(html)

    print()
    sleep(5)