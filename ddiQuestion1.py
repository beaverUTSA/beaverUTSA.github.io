#Question 1:
#Given a table that holds websites (WEBSITE_ID, Name, URL),
#website pages (PAGE_ID, WEBSITE_ID, path), and website 
#vulnerabilities (VULN_ID, PAGE_ID, data), find all of the vulnerabilities 
#on website foo.com that pertain to the login page login.html. 
#Your SQL should be performant for larger data sets.

#SQL answer
#SELECT VULN_ID, PAGE_ID, data
#    FROM vulnerabilities
#    WHERE PAGE_ID IN (
#    	SELECT PAGE_ID 
#	FROM pages 
#        WHERE WEBSITE_ID IN (
#		SELECT WEBSITE_ID 
#       		FROM websites 
#		WHERE Name = "foo") 
#	AND path LIKE '%login.html%');

import mysql.connector
import sys

#dont store passwords in scripts
server = mysql.connector.connect(
    host="",
    user="",
    password=""
    database=""
)

cursor = server.cursor()

#TODO scrub inputs to stop SQL injection
site = argv[1]
page = argv[2]

query = ('SELECT VULN_ID, PAGE_ID, data'
         'FROM vulnerabilities'
         'WHERE PAGE_ID IN ('
         '   SELECT PAGE_ID '
         '    FROM pages '
         '    WHERE WEBSITE_ID IN ('
         '        SELECT WEBSITE_ID '
         '        FROM websites '
         '        WHERE Name = "' + site + '")' 
         '    AND path LIKE "%' + page + '%");')

cursor.excecute(query)

return cursor.fetchall()
