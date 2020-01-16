import mysql.connector


def connector(query):
    mydb = mysql.connector.connect(
      host="localhost",
      user="frisdrank",
      passwd="V8WDra*57ANz",
      database="frisdrankautomaat"
    )
    cursor = mydb.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    mydb.close()
    return rows
