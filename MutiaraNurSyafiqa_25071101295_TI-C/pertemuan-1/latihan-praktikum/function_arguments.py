#1 (nilai yang dikirim ke fungsi saat fungsi dipanggil)
def perkenalan(nama): #nama adalah parameter
    print("Halo nama saya", nama)
perkenalan('Mutiara') #Mutiara adalah argument

#2 (Number of Argument)
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Mutiara", "Nur")

#3 (Default Parameter Values)
def my_function(country = "Norway"):
  print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#4 (Keyword Argument)
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")

