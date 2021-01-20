import os
import psycopg2 as db
import time

def return_list(table_name):
    sql = "SELECT * FROM {}".format(table_name)
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def return_row_count(table_name):
    sql = "SELECT * FROM {}".format(table_name)
    x = []
    a = 0
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        a = len(x)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
        return 0
    finally:
        if connection is not None:
            connection.close()
    return a

def ip_user_join():
    sql = "SELECT ipaddresses.name, ipaddresses.country, users.name, ipaddresses.dateadded, ipaddresses.id FROM users INNER JOIN ipaddresses ON users.id = ipaddresses.user_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def hash_user_join():
    sql = "SELECT hashes.name, hashes.filetype, users.name, hashes.dateadded, hashes.id FROM users INNER JOIN hashes ON users.id = hashes.user_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def url_user_join():
    sql = "SELECT urls.name, urls.currentstatus, users.name, urls.dateadded, urls.id FROM users INNER JOIN urls ON users.id = urls.user_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def email_user_join():
    sql = "SELECT emails.name, emails.type, users.name, emails.dateadded, emails.id FROM users INNER JOIN emails ON users.id = emails.user_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def insert_ip(name, country, dateadded, userid):
    sql = "INSERT INTO ipaddresses(name, country, dateadded, user_id) VALUES('{}', '{}', '{}','{}')".format(name,country,dateadded,userid)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def modify_ip(name, country):
    sql = "UPDATE ipaddresses SET name = '{}', country = '{}' WHERE name = '{}'".format(name,country,name)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_email(name, type, dateadded, userid):
    sql = "INSERT INTO emails(name, type, dateadded, user_id) VALUES('{}', '{}', '{}','{}')".format(name,type,dateadded,userid)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def modify_email(name, type):
    sql = "UPDATE emails SET name = '{}', type = '{}' WHERE name = '{}'".format(name,type,name)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_hash(name, type, dateadded, userid):
    sql = "INSERT INTO hashes(name, filetype, dateadded, user_id) VALUES('{}', '{}', '{}','{}')".format(name,type,dateadded,userid)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def modify_hash(name, type):
    sql = "UPDATE hashes SET name = '{}', filetype = '{}' WHERE name = '{}'".format(name,type,name)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_url(name, status, dateadded, userid):
    sql = "INSERT INTO urls(name, currentstatus, dateadded, user_id) VALUES('{}', '{}', '{}','{}')".format(name,status,dateadded,userid)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def modify_url(name, status):
    sql = "UPDATE urls SET name = '{}', currentstatus = '{}' WHERE name = '{}'".format(name,status,name)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def check(name, table):
    sql = "SELECT name FROM {} WHERE name = '{}'".format(table,name)
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return len(x);

def search_user(name):
    sql = "SELECT name FROM users WHERE name = '{}'".format(name)
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return len(x);

def check_password(name):
    sql = "SELECT password FROM users WHERE name = '{}'".format(name)
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchone()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x[0];

def user_session_info(name):
    sql = "SELECT id,name,status FROM users WHERE name = '{}'".format(name)
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchone()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def insert_user(name, password):
    sql = "INSERT INTO users(name, password, status) VALUES('{}', '{}', '{}')".format(name,password,'member')
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def search_term(term, table):
    if(table == "ipaddresses"):
        sql = "SELECT ipaddresses.name, ipaddresses.country, users.name, ipaddresses.dateadded FROM users INNER JOIN ipaddresses ON users.id = ipaddresses.user_id;"
    elif(table == "hashes"):
        sql = "SELECT hashes.name, hashes.filetype, users.name, hashes.dateadded FROM users INNER JOIN hashes ON users.id = hashes.user_id;"
    elif(table == "urls"):
        sql = "SELECT urls.name, urls.currentstatus, users.name, urls.dateadded FROM users INNER JOIN urls ON users.id = urls.user_id;"
    elif(table == "emails"):
        sql = "SELECT emails.name, emails.type, users.name, emails.dateadded FROM users INNER JOIN emails ON users.id = emails.user_id;"
    y = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
        for rows in x:
            for elements in rows:
                try:
                    if(term in elements):
                        y.append(rows)
                except:
                    pass
        return y
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def delete_row(name,table):
    sql = "DELETE FROM {} WHERE name = '{}'".format(table,name)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_junction(type1,type2,id1, id2):
    sql = "INSERT INTO {}_{}_junction({}_id,{}_id) VALUES('{}', '{}')".format(type1,type2,type1,type2,id1,id2)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def search_id(name,table):
    sql = "SELECT id FROM {} WHERE name = '{}'".format(table,name)
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchone()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def junction_join():
    sql = "SELECT ipaddresses.name, ipaddresses.country, users.name, ipaddresses.dateadded FROM users INNER JOIN ipaddresses ON users.id = ipaddresses.user_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def hash_email_join():
    sql = "SELECT hashes.name, emails.name FROM emails INNER JOIN hash_email_junction ON emails.id = hash_email_junction.email_id INNER JOIN hashes ON hash_email_junction.email_id = emails.id WHERE hashes.id = hash_email_junction.hash_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def hash_url_join():
    sql = "SELECT hashes.name, urls.name FROM urls INNER JOIN hash_url_junction ON urls.id = hash_url_junction.url_id INNER JOIN hashes ON hash_url_junction.url_id = urls.id WHERE hashes.id = hash_url_junction.hash_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def url_email_join():
    sql = "SELECT urls.name, emails.name FROM emails INNER JOIN url_email_junction ON emails.id = url_email_junction.email_id INNER JOIN urls ON url_email_junction.email_id = emails.id WHERE urls.id = url_email_junction.url_id;"
    x = []
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        x = cursor.fetchall()
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return x;

def delete_from_hashurl(id,type):
    sql = "DELETE FROM hash_url_junction WHERE {}_id = '{}'".format(type, id)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def delete_from_hashemail(id,type):
    sql = "DELETE FROM hash_email_junction WHERE {}_id = '{}'".format(type, id)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def delete_from_urlemail(id,type):
    sql = "DELETE FROM url_email_junction WHERE {}_id = '{}'".format(type, id)
    try:
        connection = db.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()