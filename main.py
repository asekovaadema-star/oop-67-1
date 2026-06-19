import sqlite3

from lessons.database import (create_tables,
                              add_student)

if __name__=="__main__":
    connection = sqlite3.connect("database.sqlite3")
    
    
    create_tables(connection)
    add_student(connection,
                'Jasmin',
                16,
                'Bishkek')

    connection.close()