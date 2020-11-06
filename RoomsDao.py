


import sql_actions.py
import tables.py


class RoomsDao(SqlActions):
	"""docstring for UsersDao"""


	tablesNames = TableNames()
	column_list = ['id','hotel_id', 'room_number', 'room_description', 'total_members', 'price', 'availability_status', 'date_added']
	
	def __init__(self, room_id):
		super().__init__()
		self.room_id = room_id		
		self.where_clause = {

			{

				"column_name": column_list[0],
				"data": self.room_id
			}


		}

	def setRoom(data):
		return self.setDataToDB(tablesNames.HOTEL_TABLES, column_list, data)
	
	def getRoom():
		#set  where_clause
		return self.getDataFromDB(tablesNames.HOTEL_TABLES, column_list, self.where_clause, 1)

	def updateRoom(columns, data):

		return self.updateDataOnDb(tablesNames.HOTEL_TABLES, columns, data, self.where_clause)

	def deleteRoom():

		#where id = self.room_id
		return self.deleteData(tablesNames.HOTEL_TABLES, self.where_clause)
		
