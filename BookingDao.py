


import sql_actions.py
import tables.py


class BookingDao(SqlActions):
	"""docstring for UsersDao"""


	tablesNames = TableNames()
	column_list = ['id', 'room_id', 'table_id','hotel_id', 'booked_by', 'from_date', 'to_date', 'payment_status', 'date_added']
	
	def __init__(self, booking_id):
		super().__init__()
		self.booking_id = booking_id
		self.where_clause = {

			{

				"column_name": column_list[0],
				"data": self.booking_id
			}


		}

	def setBooking(data):
		return self.setDataToDB(tablesNames.BOOKING, column_list, data)
	
	def getBooking():
		#set where where_clause
		where_clause['column_name'] = column_list[0]
		where_clause['data'] = self.booking_id
		return self.getDataFromDB(tablesNames.BOOKING, column_list, self.where_clause, 1)

	def updateBooking(columns, data):

		return self.updateDataOnDb(tablesNames.BOOKING, columns, data, self.where_clause)

	def deleteBooking():

		#where id = self.booking_id
		where_clause = []

		return self.deleteData(tablesNames.BOOKING, self.where_clause)
		
