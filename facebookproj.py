
posts=[]
users=[]
comments=[]


class User(object):
	def __init__ (self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		users.append(self)

	def add_friend (self, email):
		self.friends_list.append(email)
		print (self.name + " has added " + email + " as a friend.")

	def remove_friend (self, email):
		self.friends_list.remove(email)
		print (self.name + " has removed " + email + " as a friend.")

	def add_post (self,p_text,date):
		post1=Post(p_text,date,self)
		posts.append(post1)
		print (self.name + " has posted: " + p_text  + " on the date " + date)

	def get_userInfo (self):
		my_posts=[]
		for x in posts:
			if self == x.author:
				my_posts.append(x)
		print("Name: ["+self.name+"]"+"Email: ["+self.email+"]"+"Password: ["+self.password+"]")
		print("Friends: "+str(self.friends_list)+'Posts: '+str(my_posts))

class Post(object):
	def __init__ (self,p_text,date,author):		
		self.author=author
		self.text=p_text
		self.date=date

	def create_comment(self,c_text,date,author):
		comment1=Comment(c_text,date,self)
		comments.append(comment1)
		print("has posted" + self.c_text)

	def remove_comment(self):
		self.comments.remove(c_text)

	"""
	def post_date(self):
		print("the post was posted on "+ self.date)

	def edit_comment(self,new_c_text):
		self.c_text=new_c_text
		print("the comment has been changed:")
	def __repr__(self):
		return self.text
		"""

class Comment(Post):
	def __init__(self):
		Post.__init__(self)
		self.c_text=c_text
		

user1 = User("jesus","jesus@meet.mit.edu", "imalive")
user2 = User("moses","moses@meet.mit.edu", "imdead")
user2.add_friend("jesus@meet.mit.edu")
user1.add_post("whats up?","10.5.0")
user1.get_userInfo()	
user2.get_userInfo()
user2.remove_friend("jesus@meet.mit.edu")
