import MySQLdb
import csv
from pprint import pprint as pp

class CSV2DB(object):
    def __init__(self, csv_file):
        self.csvFile = csv_file
        self.conn = MySQLdb.connect('localhost','root','pass','somedb')
        self.__load_data()

    def __load_data(self):
        cur = self.conn.cursor()
        query = "insert into passwd values (%s %s %s %s %s %s %s)"

        with open(self.csvFile) as fp:
            content = csv.reader(fp, delimiter=':')
            data_set = list(content)
            cur.executemany(query, data_set)

        cur.close()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    CSV2DB('D:\PythonTraining\day1\passwd.txt')


