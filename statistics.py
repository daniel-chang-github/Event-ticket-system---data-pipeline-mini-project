

def query_popular_tickets(connection):
    sql_statement = '''
  SELECT event_name, count(*) as test
    FROM SALES

    GROUP BY event_name

    Having test = (
    SELECT max(max_count.ct) as ss
        FROM
        (	SELECT count(*) as ct
            FROM SALES
            GROUP BY event_name) as max_count
    )
    '''
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records
