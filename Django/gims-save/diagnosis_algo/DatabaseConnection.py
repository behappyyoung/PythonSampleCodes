import mysql.connector
from mysql.connector import errorcode

class DatabaseConnector(object):
    cnx = None
    config = {
    'user': 'dba',
    'password': 'testThisThing&7',
    'database': 'public_db',
    'host': '173.194.254.195',
    'raise_on_warnings': True,
    'ssl_ca':'./rds-ssl-ca-cert.pem',
    'ssl_cert':'./rds-ssl-client-cert.pem',
    'ssl_key':'./rds-ssl-client-privatekey.pem'


}
    def getConnection(self):
        if self.cnx == None:
            self.cnx = self.connect()
        return self.cnx

    def closeConnection(self):
        if self.cnx != None:
            self.cnx.close()

    def connect(self):
        try:
            connection = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            raise err
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            raise err
          else:
            print(err)
            raise err

        return connection

    def main(self,args):
        dbConnector = DatabaseConnector()
        try:
            connection = dbConnector.getConnection()
        except Exception as ex:
            raise ex

if __name__ == '__main__':
    import sys

    DatabaseConnector().main(sys.argv)




