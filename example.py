from datetime import datetime
import sys
#https://www.geeksforgeeks.org/command-line-arguments-in-python/
n=len(sys.argv[0])
ticket_id=sys.argv[1]
print(ticket_id)

myFile = open('/Users/shubhamjha/Desktop/append.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now())+ "  "+ticket_id)
print("hii")
