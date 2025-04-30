__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"

# importing required libraries
import mysql.connector

db_config={
    "user":"vivek",
    "passwd":"",
    "host":"localhost"
}


def mysql_connection(**kwargs):
    dataBase = mysql.connector.connect(
        **kwargs
    )
    print(dataBase)
    return dataBase

def create_db():
    db=mysql_connection(**db_config);
    cursor=db.cursor()
    # cursor.execute("create database axio")
    cursor.execute("show databases")
    db.close()


def create_table():
    pass






if __name__=="__main__":
    create_db()


