################################################33
# ABOUT: CRUD OPERATIONS USING PYTHON CLASS
# MYSQL Adapatation of article
# https://www.codeproject.com/Articles/1275121/CRUD-Operations-in-Python-with-SQL-Database
# written using python 2.+
# can easily be written in 3+
################################################33
# database table
# CREATE TABLE `customers` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `name` varchar(255) DEFAULT NULL,
#  `address` varchar(255) DEFAULT NULL,
#  PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
################################################33

import genops as gen
#import the crud class
from crud import crud

choice = ""
# loop while choice not equal to 999
while choice.lower() != "q":
    gen.printoptions()
    choice = str(raw_input('Selection:')).lower()
    crudobj=crud()
    if choice == 'c':
        crudobj.create()
    elif choice == 'r':
        crudobj.read()
    elif choice == 'u':
        crudobj.update()    
    elif choice == 'd':
        crudobj.delete()
    elif choice == 'q':
        print 'program ended!'
        break
    else:
        print('Error in selection')


