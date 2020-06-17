import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
    
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_category(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO Category(ParentID, Title)
              VALUES(?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    except Error as e:
        print(e)
        
    return cur.lastrowid

def create_location(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO Location(Title)
              VALUES(?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    except Error as e:
        print(e)
        
    return cur.lastrowid

def create_status(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO Status(Title)
              VALUES(?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    except Error as e:
        print(e)
        
    return cur.lastrowid

def create_expense_item(conn, task):

    sql = ''' INSERT INTO Expense(Date, CategoryID, SubCategoryID, LocationID, DescriptionID, Amount, StatusID, Remark)
              VALUES(?,?, ?,?,?,?,?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    except Error as e:
        print(e)
        
    return cur.lastrowid

def create_description(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO Description(Title, LocationID)
              VALUES(?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    except Error as e:
        print(e)
        
    return cur.lastrowid

def query_DescriptionID(conn, title, index):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT ID 
                        FROM Description 
                        WHERE Title = ? AND LocationID = ? """, (title,index[0]))
        id = cur.fetchone()
        #print (id)
        return id
    except Error as e:
        print(e)

def query_CategoryID(conn, title):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT CategoryID 
                        FROM Category 
                        WHERE Title = ? """, (title,))
        id = cur.fetchone()
        #print (id)
        return id
    except Error as e:
        print(e)

def query_LocationID(conn, title):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT ID 
                        FROM Location 
                        WHERE Title = ? """, (title,))
        id = cur.fetchone()
        #print (id)
        return id
    except Error as e:
        print(e)

def query_StatusID(conn, title):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT ID 
                        FROM Status 
                        WHERE Title = ? """, (title,))
        id = cur.fetchone()
        #print (id)
        return id
    except Error as e:
        print(e)

def query_CategoryID2(conn, title, index):
    try:
        #print(index[0])
        cur = conn.cursor()
        cur.execute("""SELECT CategoryID 
                        FROM Category 
                        WHERE Title = ? AND ParentID = ?""", (title,index[0]))
        id = cur.fetchone()
        return id
    except Error as e:
        print(e)