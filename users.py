


import sql_actions.py
import tables.py


class UsersDao(SqlActions):
	"""docstring for UsersDao"""


	tablesNames = TableNames()
	column_list = ['id','user_name', 'email', 'phone_number', 'password', 'date_added']

	def __init__(self, user_id):
		super().__init__()
		self.user_id = user_id
		self.where_clause = {

			{

				"column_name": column_list[0],
				"data": self.user_id
			}


		}


	def setUser(data):
		return self.setDataToDB(tablesNames.USERS, column_list, data)
	
	def getUser():
		#set where where_clause
		
		return self.getDataFromDB(tablesNames.USERS, column_list, self.where_clause, 1)

	def updateUser(columns_to_be_updated , data_input):

		where_clause = {

			{

				"column_name": column_list[0],
				"data": self.user_id
			}


		}

		return self.updateDataOnDb(tablesNames.USERS, columns_to_be_updated, data_input, self.where_clause)

	def deleteUser():

		#where id = self.user_id
		where_clause = {

			{

				"column_name": column_list[0],
				"data": self.user_id
			}


		}


		return self.deleteData(tablesNames.USERS, self.where_clause)
		
