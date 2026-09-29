import psycopg2

with psycopg2.connect(
    dbname="ai_dev_journey", user="aaqibkhan", host="localhost", port="5432"
) as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT customer_id, name, city, email FROM customers WHERE city = %s;",
            ("Islamabad",),
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)
