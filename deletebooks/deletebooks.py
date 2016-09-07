import MySQLdb
import csv 

db = MySQLdb.connect(host='localhost', user='root', passwd='19963',db='test_library')

cursor = db.cursor()


#result = cursor.fetchall()

#for record in result:
#	print record


aFile = open('test.csv','r')
reader = csv.reader(aFile)
for row in reader:
    #print row[1]
    #xrow = row[1]
    #print row
    sql = "DELETE FROM `importbook` WHERE BookName = '%s'" % (row[1],)



db.commit()


