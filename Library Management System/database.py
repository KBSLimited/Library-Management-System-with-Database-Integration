import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Establishes a connection to the MySQL database.

    Returns:
    - mysql.connector.connection.MySQLConnection: The database connection object.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='library_db'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def execute_query(query, params=()):
    """
    Executes a SQL query on the MySQL database.

    Args:
    - query (str): The SQL query to execute.
    - params (tuple): Parameters to pass to the SQL query.

    Returns:
    - list: A list of fetched results.
    """
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return []

def fetch_one(query, params=()):
    """
    Fetches a single result from a SQL query.

    Args:
    - query (str): The SQL query to execute.
    - params (tuple): Parameters to pass to the SQL query.

    Returns:
    - tuple: The fetched result.
    """
    results = execute_query(query, params)
    return results[0] if results else None
