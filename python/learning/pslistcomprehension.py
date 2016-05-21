import sys
import io
#filepath to a file where fields are seperated by :
list_of_list = [l.rstrip().split(':') for l in open('filepath')]

def sortkey(record):
    #return record[3] #to sort with string column on index 3
    return int(record[2]) #to int sort on 2 column which is int column

sorted(list_of_list, key=sortkey)

#using lambda
data = sorted(list_of_list, key=lambda rec: int(rec[2]))