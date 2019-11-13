class Animal(object):
	def __init__ (self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummmy!!" + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self,times):
		print(self.sound * times)

class Person(object):
	def __init__ (self,name,age,city,gender,IQ):
		self.city = city
		self.name = name
		self.age = age
		self.gender = gender
		self.IQ = IQ
	def eating(self,breakfast):
		print(self.name + " is eating his favorite breakfast- " + breakfast)
	def description(self):
		print(self.name + " is a " + self.age + " years old " + self.gender + ", he lives in " + self.city + " and his IQ level is " + self.IQ)

class Bird(object):
	def __init__ (self,name,color,speed):
		self.color = color
		self.name = name
		self.speed = speed
	def get_speed(self):
		print(self.name + "'s speed is " + self.speed)
	def race(self,bird2):
		if self.speed > bird2.speed:
			print("you won!!!!")
		elif self.speed < bird2.speed:
			print("you lost....")
		elif self.speed == bird2.speed:
			print("it's a tie.")

lion = Animal("ROAR!", "Lion1" , "5" , "Red")
lion.eat("strawberries")
lion.description()
lion.make_sound(3)
person = Person("Mike", "2,844,538" , "blablabla city" , "male" , "2")
person.eating("YASA food")
person.description()
bird = Bird("yousef","rainbow",300)
bird2 = Bird("shir","red",900)
bird.race(bird2)
