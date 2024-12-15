import psycopg2
from psycopg2 import sql

def save_calculation(operation, result):
    try:
        # Establish the database connection
        connection = psycopg2.connect(
            dbname="ai_calc_v2",
            user="postgres",
            password="deva",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Insert the operation and result into the database
        query = sql.SQL("INSERT INTO calculations (operation, result) VALUES (%s, %s)")
        cursor.execute(query, (operation, result))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print(f"Calculation saved: {operation} = {result}")

    except Exception as e:
        print(f"Error saving calculation: {e}")
        if connection:
            connection.rollback()
        if cursor:
            cursor.close()
            connection.close()

def load_history():
    try:
        # Establish the database connection
        connection = psycopg2.connect(
            dbname="ai_calc_v2",
            user="postgres",
            password="deva",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Query to retrieve all past calculations
        query = "SELECT * FROM calculations ORDER BY timestamp DESC"
        cursor.execute(query)

        # Fetch all rows from the query result
        history = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return history

    except Exception as e:
        print(f"Error loading history: {e}")
        return []
