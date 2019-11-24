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

	def add_post (self,p_text,date,likes,title):
		post1=Post(p_text,date,likes,self.email,title)
		posts.append(post1)
		print (self.name + " has posted: " + p_text  + " on the date " + date)

	def create_comment(self,text,date,likes,title):
		for x in posts:
			if title == x.title:
				pst=x.title
		comment1=Comment(text,date,likes,self,pst)
		comments.append(comment1)
		print(self.name + " has commented " + text + " on the post " + pst)

	def get_userInfo (self):
		my_posts=[]
		for x in posts:
			if self.email == x.author:
				my_posts.append(x.title)
		print("Name: ["+self.name+"]"+"\nEmail: ["+self.email+"]"+"\nPassword: ["+self.password+"]")
		print("Friends: "+str(self.friends_list)+'\nPosts: '+str(my_posts))

class Post(object):
	def __init__ (self,text,date,likes,author,title):		
		self.author=author
		self.text=text
		self.date=date
		self.likes=likes
		self.title=title
	

	def remove_comment(self):
		self.comments.remove(text)

	def add_like(self,likes):
		likes=likes+1
		print("likes" + str(likes))

class Comment(Post):
	def __init__(self,text,date,likes,author,title):
		Post.__init__(self,text,date,likes,author,title)
		self.text=text
		

user1 = User("jesus","jesus@meet.mit.edu", "imalive")
user2 = User("moses","moses@meet.mit.edu", "imdead")

iemail=input("what is your email?")
ipass = input("what is your password?")
for x in users:
	if iemail == x.email and ipass == x.password:
		print(x.name + "you are logged in!")
	else:
		quit()





user2.add_friend("jesus@meet.mit.edu")
user1.add_post("whats up?","10.5.0",2,"thepost")
user1.get_userInfo()	
user2.get_userInfo()
user2.remove_friend("jesus@meet.mit.edu")

user1.create_comment("lejfmdirkejs","5.2.2002",64,"thepost")