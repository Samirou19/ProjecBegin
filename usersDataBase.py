class UserBase() :
	userList = {}	

	def Save(self, user):
		self.userList[user.Id] = user.name

	def GetUser(self,): 
		return self.userList

	# UserDataBase.{user1.Id} = user1.name
	# UserDataBase.{user1.Id} = user1.name