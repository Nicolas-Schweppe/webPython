import pymysql
from decouple import config

def obtenerConexion():
    return pymysql.connect(host=config('MYSQL_HOST'),
                            user=config('MYSQL_USER'),
                            passwd=config('MYSQL_PASSWORD'),
                            database=config('MYSQL_DB'))