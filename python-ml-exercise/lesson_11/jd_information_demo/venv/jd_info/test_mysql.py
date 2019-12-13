import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             db='crm',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT * FROM xadmin_log WHERE action_flag=%s"
        #args = "'create'"
        # sql = "SELECT * FROM xadmin_log WHERE action_flag=" + args + ";"
        sql = "SELECT * FROM user WHERE age = 15"
        print(sql)
        # cursor.execute(sql, ('create',))
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

#s = ('ssss',)
#print(s)
#print(type(s))
