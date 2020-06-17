import sql
db_dir = "./db/database1.db"

sql_create_category_table = """ CREATE TABLE IF NOT EXISTS Category (
                                        ParentID integer,
                                        CategoryID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        Title text NOT NULL
                                    ); """
sql_create_location_table = """ CREATE TABLE IF NOT EXISTS Location (
                                        ID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        Title text NOT NULL
                                    ); """
sql_create_description_table = """ CREATE TABLE IF NOT EXISTS Description (
                                        ID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        LocationID integer NOT NULL,
                                        Title text NOT NULL,
                                        FOREIGN KEY (LocationID) REFERENCES Location (ID)
                                    ); """
sql_create_status_table = """ CREATE TABLE IF NOT EXISTS Status (
                                        ID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        Title text NOT NULL
                                    ); """
sql_create_expense_table = """ CREATE TABLE IF NOT EXISTS Expense (
                                        ID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        Date text NOT NULL,
                                        CategoryID integer,
                                        SubCategoryID integer,
                                        LocationID integer,
                                        DescriptionID integer,
                                        Amount REAL,
                                        StatusID text,
                                        Remark text,
                                        FOREIGN KEY (CategoryID) REFERENCES Category (CategoryID),
                                        FOREIGN KEY (SubCategoryID) REFERENCES Category (CategoryID),
                                        FOREIGN KEY (LocationID) REFERENCES Location (ID),
                                        FOREIGN KEY (DescriptionID) REFERENCES Description (ID),
                                        FOREIGN KEY (StatusID) REFERENCES Status (ID)
                                    ); """

initial = False
# category ={
# }

f = open("./data/data.txt", "r")
while True:
    read_data = f.readline()
    #print (read_data)
    if not read_data:
        break
    i = 0 
    n = 0
    l = []
    while n!=10:
        if(read_data[i] == ','):
            n = n + 1
            l.append(i)
            i = i + 1
        else :
            i = i + 1
    l.append(i)
    #print (read_data[l[0]+1:l[1]])   
    header = []
    for z in range(9):   # 0 = dates, 1 = Cat, 2 = subCat, 3 = Loc, 4 = Des, 5 = Amount, 6 = Status, 7 = Remark
        if z !=6:
            header.append(read_data[l[z]+1:l[z+1]])
    #print (header[6])
    conn = sql.create_connection(db_dir)    
    with conn:
        if initial:
            if conn is not None:                                     #initialize category table
                sql.create_table(conn, sql_create_category_table)
                sql.create_table(conn, sql_create_location_table)
                sql.create_table(conn, sql_create_description_table)
                sql.create_table(conn, sql_create_status_table)
                sql.create_table(conn, sql_create_expense_table)
            else:
                print("Error loading database")
            
            '''
            Category Start
            '''
            index1 = sql.query_CategoryID(conn, header[1])
            if index1 is None:
                task = ("null",  header[1])
                idd = sql.create_category(conn, task)
                #print (idd)
            '''
            Category End
            '''
        else:
            '''
            Category Start
            '''
            index1 = sql.query_CategoryID(conn,  header[1])
            if index1 is None:
                task = ("null",  header[1])
                sql.create_category(conn, task)
                index2 = sql.query_CategoryID(conn,  header[1])
                task = (index2[0],  header[2])
                sql.create_category(conn,task)    
            else:
                index2 = sql.query_CategoryID2(conn, header[2], index1)
                if index2 is None:
                    task = (index1[0], header[2])
                    sql.create_category(conn,task) 
            '''
            Category End
            '''
            '''
            Location Start
            ''' 
            index1 = sql.query_LocationID(conn,  header[3])
            #print (header[3])
            #print (index1)
            if index1 is None:
                
                task = (header[3], )
                sql.create_location(conn, task)
            '''
            Location End
            '''    
            '''
            Status Start
            ''' 
            index1 = sql.query_StatusID(conn,  header[6])
            if index1 is None:
                
                task = (header[6], )
                sql.create_status(conn, task)
            '''
            Status End
            '''      
            '''
            Decription Start
            ''' 
            
            index2 = sql.query_LocationID(conn,  header[3])
            index1 = sql.query_DescriptionID(conn,  header[4], index2)
            if index1 is None:
                task = (header[4], index2[0])
                sql.create_description(conn, task)
            '''
            Discription End
            '''      
f.close()
######################################################################
    # if Cat in category:
    #     if subCat not in category[Cat]:
    #         category[Cat].append(subCat)
            # conn = sql.create_connection(db_dir)
            # with conn:
            #     #print (type(Cat))
            #     index = sql.query_CategoryID(conn, Cat)
            #     #print (index)
            #     task = (index[0], subCat)
            #     sql.create_category(conn,task)
    # else:
    #     category[Cat] = [subCat]
        # conn = sql.create_connection(db_dir)
        # with conn:
        #     task = ("null", Cat)
        #     sql.create_category(conn, task)
        #     index = sql.query_CategoryID(conn, Cat)
        #     #print (index)
        #     task = (index[0], subCat)
        #     sql.create_category(conn,task)


# for x, y in category.items():                 #print category dictionary
#   print(x, y)


