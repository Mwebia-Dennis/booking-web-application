


import sql_actions.py
import tables.py


class HotelDao(SqlActions):
	"""docstring for UsersDao"""


	tablesNames = TableNames()
	column_list = ['id','hotel_name', 'Address1', 'Address2', 'Address3', 'added_by', 'location', 'date_added']
	
	def __init__(self, hotel_id):
		super().__init__()
		self.hotel_id = hotel_id
		self.where_clause = {

			{

				"column_name": column_list[0],
				"data": self.hotel_id
			}


		}

	def setHotel(data):
		return self.setDataToDB(tablesNames.HOTEL, column_list, data)
	
	def getHotel():
		#set where where_clause
		return self.getDataFromDB(tablesNames.HOTEL, column_list, self.where_clause, 1)

	def updateHotel(columns_to_be_updated,data_input):



		return self.updateDataOnDb(tablesNames.HOTEL, columns_to_be_updated, data_input, self.where_clause)

	def deleteHotel():

		#where id = self.hotel_id

		return self.deleteData(tablesNames.HOTEL, self.where_clause)
		
