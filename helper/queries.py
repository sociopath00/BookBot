import MySQLdb
import pandas as pd


def fetch_data(column, value, expected_cols):
    """
    A function to fetch data from database
    :param column: column name in db table
    :param value: value to filter
    :return: dataframe
    """
    conn = MySQLdb.connect("localhost", "socio", "Root@123", "books")
    cursor = conn.cursor()
    query = "SELECT * from books where {}='{}'".format(column, value)
    cursor.execute(query)

    # convert the data into dataframe
    data = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
    conn.close()
    return data[expected_cols].values


if __name__ == "__main__":
    print(fetch_data("author", "ravinder singh", "name"))
