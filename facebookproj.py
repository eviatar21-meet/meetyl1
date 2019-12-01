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
		

user1 = User("matt","matt@meet.mit.edu", "1234")
user2 = User("dave","dave@meet.mit.edu", "9876")
user0 = ""


start_menu=""
while start_menu != "1" and start_menu != "2":
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	start_menu = input("LOG IN - PRESS 1 \n SIGN UP - PRESS 2 \n ||")
if start_menu == "1":
	iemail=input("what is your email?")
	ipass = input("what is your password?")
	for x in users:
		if iemail == x.email and ipass == x.password:
			print("you are logged in as " + x.name)
			user0 = x
			break
		else:
			print("you are not a registerd user!")
			quit()
elif start_menu == "2":
	aname = input("enter your name: \n ||")
	aemail = input("enter your email: \n ||")
	apass = input("create a password: \n ||")
	user0 = User(aname,aemail,apass)
	print("you are logged in as " + aname)


activity_menu=""
while 1==1:
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	activity_menu = input("POST - PRESS 1 \n COMMENT - PRESS 2 \n ADD FRIEND - PRESS 3 \n REMOVE FRIEND - PRESS 4 \n SURF - PRESS 5 \n QUIT - PRESS 6 \n||")
	if activity_menu == "1":
		title=input("enter title: ")
		date=input("enter date: ")
		text=input("enter text: ")
		user0.add_post(text,date,0,title)
	elif activity_menu == "2":
		title=input("enter title: ")
		date=input("enter date: ")
		text=input("enter text: ")
		user0.create_comment(text,date,0,title)
	elif activity_menu == "3":
		friend=input("enter friend's email: ")
		user0.add_friend(friend)
	elif activity_menu == "4":
		friend=input("enter friend's email: ")
		user0.remove_friend(friend)
	elif activity_menu == "5":
		break
	elif activity_menu == "6":
		print("good bye!")
	else:
		print("you entered an invalid input")



user2.add_friend("matt@meet.mit.edu")
user1.add_post("whats up?","10.5.2019",2,"thepost")
#user1.get_userInfo()	
#user2.get_userInfo()
user2.remove_friend("matt@meet.mit.edu")

user1.create_comment("lejfmdirkejs","5.2.2002",64,"thepost")
