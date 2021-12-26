from mysql.connector import connect, Error
import queries.insert_queries as insert
import queries.select_query as select

try:
    con = connect(
        host="localhost",
        user="Admin",
        password="admin",
        database="ytmusic_analizer",
    )
except Error as e:
    print(e)
else:
    with con.cursor() as cursor:
        # print(add_track("12345", "test", 2222))
        cursor.execute(insert.add_user("test@ya.ru", "test", '2222'))
        # result = cursor.fetchall()
        #
        # for el in result:
        #     print(el)
        con.commit()

