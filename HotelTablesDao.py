


import sql_actions.py
import tables.py


class HotelTablesDao(SqlActions):
	"""docstring for UsersDao"""


	tablesNames = TableNames()
	column_list = ['id','hotel_id', 'table_number', 'table_description', 'total_members', 'price', 'availability_status', 'date_added']

	
	def __init__(self, table_id):
		super().__init__()
		self.table_id = table_id
		self.where_clause = {

			{

				"column_name": column_list[0],
				"data": self.table_id
			}


		}

	def setHotel(data):
		return self.setDataToDB(tablesNames.HOTEL_TABLES, column_list, data)
	
	def getHotel():
		#set where where_clause

		return self.getDataFromDB(tablesNames.HOTEL_TABLES, column_list, self.where_clause, 1)

	def updateHotel(columns, data):


		return self.updateDataOnDb(tablesNames.HOTEL_TABLES, columns, data, self.where_clause)

	def deleteHotel():

		#where id = self.table_id

		return self.deleteData(tablesNames.HOTEL_TABLES, self.where_clause)
		
