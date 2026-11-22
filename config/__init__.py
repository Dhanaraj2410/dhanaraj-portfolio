# config package
# Use PyMySQL as the MySQLdb driver without requiring mysqlclient.
import pymysql

pymysql.install_as_MySQLdb()
