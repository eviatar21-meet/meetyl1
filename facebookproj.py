class User(object):
	def __init__ (self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts = []

	def add_friend (self, email):
		self.friends_list.append(email)
		print (self.name + " has added " + email + " as a friend.")

	def remove_friend (self, email):
		self.friends_list.remove(email)
		print (self.name + " has removed " + email + " as a friend.")

	def post (self, text):
		self.posts.append(text)
		print (self.name + " has posted: " + text )

	def get_userInfo (self):
		print("Name: ["+self.name+"]"+"Email: ["+self.email+"]"+"Password: ["+self.password+"]"+"Friends: ["+str(self.friends_list)+']'+'Posts: ['+str(self.posts)+']')

class Post(object):
	def __init__ (self)



user1 = User("jesus","jesus@meet.mit.edu", "imalive")
user2 = User("moses","moses@meet.mit.edu", "imdead")
user2.add_friend("jesus@meet.mit.edu")
user1.post("I am the way and the truth and the life. No one comes to the Father except through me. John 14:6 NIV")
user1.get_userInfo()
user2.get_userInfo()
user2.remove_friend("jesus@meet.mit.edu")
