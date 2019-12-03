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
		print("Name: ["+self.name+"]"+"\nEmail: ["+self.email+"]"+"\nPassword: [*************]")
		print("Friends: "+str(self.friends_list)+'\nPosts: '+str(my_posts)+"\n")

class Post(object):
	def __init__ (self,text,date,likes,author,title):		
		self.author=author
		self.text=text
		self.date=date
		self.likes=likes
		self.title=title

	def remove_comment(self):
		self.comments.remove(text)

	def add_like(self):
		self.likes=self.likes+1
		print("there are " + str(self.likes) + " likes on the post " + self.title)

class Comment(Post):
	def __init__(self,text,date,likes,author,title):
		Post.__init__(self,text,date,likes,author,title)
		self.text=text
		

user1 = User("matt","matt@meet.mit.edu", "1234")
user2 = User("dave","dave@meet.mit.edu", "9876")



start_menu=""
registerd = False
while start_menu != "1" and start_menu != "2":
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	start_menu = input(" LOG IN -- PRESS 1 \n SIGN UP - PRESS 2 \n ||")
if start_menu == "1":
	iemail=input("what is your email?")
	ipass = input("what is your password?")
	for x in users:
		if iemail == x.email and ipass == x.password:
			print("you are logged in as " + x.name)
			user0 = x
			registerd= True
			break
	if registerd == False:	
		print("you are not a registerd user")
		quit()
if start_menu == "2":
	aname = input("enter your name: \n ||")
	aemail = input("enter your email: \n ||")
	apass = input("create a password: \n ||")
	user0 = User(aname,aemail,apass)
	print("you are logged in as " + aname)



def menu2():
	activity_menu=""
	while 1==1:
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		activity_menu = input(" POST ---------- PRESS 1 \n COMMENT ------- PRESS 2 \n ADD LIKE ------ PRESS 3 \n ADD FRIEND ---- PRESS 4 \n REMOVE FRIEND - PRESS 5 \n SURF ---------- PRESS 6 \n QUIT ---------- PRESS 7 \n||")
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
			post=input("enter post title: ")
			for x in posts:
				if post == x.title:
					lk=x
					lk.add_like()
					break
		elif activity_menu == "4":
			friend=input("enter friend's email: ")
			user0.add_friend(friend)
		elif activity_menu == "5":
			friend=input("enter friend's email: ")
			user0.remove_friend(friend)
		elif activity_menu == "6":
			#menu3()
			break
		elif activity_menu == "7":
			print("you are logged out, \n good bye.")
			quit()
		else:
			print("you entered an invalid input")

menu2()


surf_menu=""
while 1==1:
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	surf_menu = input(" SEE ALL USERS - PRESS 1 \n SEE ALL POSTS - PRESS 2 \n SEE ALL COMMENTS ------ PRESS 3 \n EXIT ---- PRESS 4 \n||")
	if surf_menu == "1":
		print("USERS:\n")
		for t in users:
			t.get_userInfo()
	elif surf_menu == "2":
		sposts=[]
		print("POSTS:\n")
		for d in posts:
			sposts.append(d.title)
		print(str(sposts))
	elif surf_menu == "3":
		scomments=[]
		print("COMMENTS:\n")
		for s in comments:
			scomments.append(s.text)
			print(str(scomments))
	elif surf_menu == "4":
		menu2()
	else:
		print("you entered an invalid input")