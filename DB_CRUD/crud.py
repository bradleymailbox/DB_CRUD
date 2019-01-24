import dbops as dbconn
import sys

class crud:
    def create(self):
        # Get the sql connection
        connection = dbconn.connect()
        name = str(raw_input('Enter Name = '))
        address = str(raw_input('Enter Address = '))
        try:
            query = "insert into customers(name, address) Values(%s,%s)" 
            cursor = connection.cursor()
            # Execute the sql query
            val = (name.upper(), address.upper())
            cursor.execute(query, val)
            # Commit the data
            connection.commit()
            print('Record Saved Successfully')
        except:
            print("Exception ",sys.exc_info()[0],"occured.")
        finally:
            # Close the connection
            connection.close()

    def read(self):   
        try:
            # Get the sql connection
            connection = dbconn.connect()
            cursor = connection.cursor()
            # Execute the sql query
            cursor.execute('Select * from customers')
            # Print the data
            for row in cursor:
                print('row = %r' % (row,))
            print('Records Retrieved Successfully')
        except:
            print("Exception ",sys.exc_info()[0],"occured.")
        finally:
            # Close the connection
            connection.close()

    def update(self):
        # Get the sql connection
        connection = dbconn.connect()
        id = str(raw_input('Enter customer id = '))
    
        try:
            # Fetch the data
            sql = "select * From customers Where id = %s" 
            val = (id,)
            cursor = connection.cursor()
            cursor.execute(sql, val)
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Address')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = str(raw_input('Enter Name = '))
            address = str(raw_input('Enter Address = '))
            query = "Update customers set name = %s, address =%s Where id = %s" 
            val = (name.upper(), address.upper(), id,)
            # Execute the update query
            cursor.execute(query, val)
            connection.commit()
            print('Record Updated Successfully')
        except:
            print("Exception ",sys.exc_info()[0],"occured.")
        finally:
            # Close the connection
            connection.close()

    def delete(self):
        # Get the sql connection
        connection = dbconn.connect()
        id = str(raw_input('Enter customer id = '))
   
        try:
            # Fetch the data
            sql = "select * From customers Where id = %s" 
            val = (id,)
            cursor = connection.cursor()
            cursor.execute(sql, val)
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Address')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = str(raw_input('Are you sure to delete this record (Y/N)?'))
            # Delete after confirmation
            if confirm.lower() == 'y':
               deleteQuery = "delete from customers Where id = %s"
               cursor.execute(deleteQuery,val)
               connection.commit()
               print('Record deleted successfully!')
            else:
                print('Delete cancelled')
        except:
            print("Exception ",sys.exc_info()[0],"occured.")
        finally:
            connection.close()