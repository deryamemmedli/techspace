import pymysql
import pymysql.cursors



# CONNECT TO THE DATABASE

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345',
    db='TechSpace',
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)
# print(connection.host_info)





# CREATE A TABLE

def create_blog():
    with connection:
        with connection. cursor() as cursor:
            sql = """CREATE TABLE if not exists TechSpace.Blogs (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR (100),
                        author_name varchar (100)
                        );"""

            cursor.execute (sql)
        connection.commit()
# create_blog()






# INSERT DATA INTO TABLES

def insert_into_blog(title,author):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO TechSpace.Blogs(title,author_name) VALUES (%s, %s)"
            cursor.execute(sql, (title,author))
        connection.commit()

#  insert_into_blog('Python', 'John Doe')
# insert_into_blog('Java','Jane Doe')
# insert_into_blog('Java2','Jane Doe')






# GET ALL BLOGS

def get_all_blogs():
    with connection.cursor() as cursor:
        sql= "SELECT * FROM TechSpace.Blogs"
        cursor.execute(sql)
        return cursor.fetchall()
    
#print(get_all_blogs())






# UPDATE A BLOG

def update_blog(id,title):
    with connection:
        with connection.cursor() as cursor:
            sql="""UPDATE TechSpace.Blogs 
                    SET title=%s 
                    WHERE id=%s """
            cursor.execute(sql, (title,id))
        connection.commit()

# update_blog(1,'Python2')






# GET A SINGLE BLOG

def get_single_blog(id):
    with connection:
        with connection.cursor() as cursor:
            sql="SELECT * FROM TechSpace.Blogs WHERE id=%s"
            cursor.execute(sql,(id))
            return cursor.fetchone()
# print(get_single_blog(2))







# FILTER BY BLOG NAME

def filter_by_name(title):
    # with connection:
        with connection.cursor() as cursor:
            sql=f"SELECT * FROM TechSpace.Blogs WHERE title like '%{title}%' "
            cursor.execute(sql)
            return cursor.fetchall()
# print(filter_by_name('Python'))



# DELETE A BLOG

def delete_single_blog(id):
    with connection:
        with connection.cursor() as cursor:
            sql= """DELETE FROM TechSpace.Blogs WHERE id = %s"""
            cursor.execute(sql,(id))
        connection.commit()
# delete_single_blog(3)







