from database import get_db

db = get_db()

def run_select_query(query:str) -> list:
    # cursor = db.cursor(named_tuple=True)    # named tuple rows # DEPRECATED
    # cursor = db.cursor(dictionary=True)     # dict rows
    cursor = db.cursor()                    # tuple rows
    cursor.execute(query)
    columns = tuple([item[0] for item in cursor.description])
    print(columns)
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        print(row)

if __name__ == "__main__":
    run_select_query('select * from client')

    run_select_query(
        'select * '
        'from client '
        'inner join city '
        'on client.city = city.city'
    )

    run_select_query(
        '''
        select *
        from client
        inner join city
        on client.city = city.city
        '''
    )



