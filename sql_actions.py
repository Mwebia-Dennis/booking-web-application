"""import mysql.connector // import your mysql connector"""
import connection.py

class SqlActions():
	"""docstring for SqlActions
		*used to set all data to database 
		*will be inherited 
	"""

	def __init__(self):
		self.myCursor = conn.cursor()
		self.conn = conn


	def setDataToDB(table, column_list, data):

		col_info = getColNameAndValue(column_list)
		sql = "INSERT INTO "+ table + " ("+col_info[0]+") VALUES ("+col_info[1]+")"
		myCursor.execute(sql, data)
		result = conn.commit()
		return result




	#define function for getting data

	def getDataFromDB(table, column_list, where_clause, limit = ''):

		col_info = getColNameAndValue(column_list)

		sql = "SELECT "+col_info[0]+" FROM "+table

		if where_clause:

			sql += " WHERE "+where_clause[0]['column_name']+" = "+where_clause[0]['data']
				

		if limit != '':

			sql += " limit = "+limit

		sql += " ORDER BY date_added DESC"

		myCursor.execute(sql)

		result = conn.fetchall()

		return result

		





	#define update data on db

	def updateDataOnDb(table, column_list, data, where_clause):

		sql = "UPDATE "+table+" SET "

		i = 0;
		for column in column_list:
			sql += column + " = "+"%s"

		sql += " WHERE "+where_clause[0]['column_name']+" = "+where_clause[0]['data']



		myCursor.execute(sql, data)
		result = conn.commit()
		return result

	#define deleting data
	# delete and return true if any rows were deleted

	def deleteData(table, where_clause):

		sql = "DELETE FROM "+table+" WHERE `"+where_clause[0]['column_name']+" = "+where_clause[0]['data']

		myCursor.execute(sql)
		result = conn.commit()
		return result

	def getColNameAndValue(column_list):


		column_names = ""
		column_value = ""
		"""	

			*since we dont know the exact columns that will be needed to be inserted we have to use a list or dict
			*so column_list is a list
			*we loop column_list concatenating each column name to one string
			*also add the escape string to column value

		"""
		i = 0;
		for column in column_list:
			column_names += column
			column_value += "%s"
			i++

			if i != len(column_list):
				column_names += ","
				column_value += ","



		return (column_list,column_value)






		
