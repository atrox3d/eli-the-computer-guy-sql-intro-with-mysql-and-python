import mysql.connector

config = dict(
    host='localhost',
    user='user',
    password='123',
    database='company'
)


def get_db(config:dict=config):
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

