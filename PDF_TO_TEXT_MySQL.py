
import sys  
import os  
import PyPDF2


pdf_file = open(path_of_pdf_file, 'rb') # Replace the path_of_pdf_file with the exact path of the pdf file
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()


text_list = []
for i in range(0,number_of_pages):
     text_list.append(read_pdf.getPage(i).extractText().encode("utf-8"))

	 

# Store the text extracted from pdf in a text file	 
thefile = open( path_of_text_file_to_be_stored + ".txt", 'w')


for item in text_list:
   thefile.write("%s\n" % item)

thefile.close()

# Storing the text into the MySQL Database

# First we need to connect to the MySQL database
import MySQLdb # Python Module for connecting to the MySQL Database

db = MySQLdb.connect("localhost","user","password","database")
# "user" should be replaced by the username of the MySQL server
# "password" should be replaced by the password of the MySQL server
# "database" should be replaced by the name of the database to which we need to connect
cursor = db.cursor()

file = open(path_of_the_text_file, 'r') # Replace the path_of_text_file with the exact path
file_content = file.read()
file.close()

query = "INSERT INTO table VALUES (%s)" # Replace the table with the name of the table in which data need to be inserted

cursor.execute(query, (file_content,))

db.commit()
db.close()