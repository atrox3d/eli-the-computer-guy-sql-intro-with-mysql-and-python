import mysql.connector
from mysql.connector import MySQLConnection

config = dict(
    host='localhost',
    user='user',
    password='123',
    database='company'
)

def get_db(config:dict=config) -> MySQLConnection:
    return mysql.connector.connect(**config )

def test_connection(config:dict):
    db = get_db(config)
    db.close()
    print(db.is_connected())
    return(
            db.user,
            db.server_host,
            db.server_port,
        )

if __name__ == "__main__":
    try:
        user, server, port = test_connection(config)
        print('SUCCESS| ', f'{user}@{server}:{port}')
    except Exception as e:
        print('ERROR |', e.__class__.__qualname__)
        print('ERROR |', e)


def create_table_temp(db:MySQLConnection):
    cursor = db.cursor()
    cursor.execute(
        '''
        create table if not exists temp(
            id int auto_increment primary key,
            temp int,
            timestamp timestamp default now()
        )
        '''
    )


def drop_table(db:MySQLConnection, name:str):
    cursor = db.cursor()
    cursor.execute(f'drop table if exists {name}')


def exec_statement(db:MySQLConnection, stmt:str):
    cursor = db.cursor()
    cursor.execute(stmt)
    # print(cursor.statement)
    result = cursor.fetchall()
    return result

