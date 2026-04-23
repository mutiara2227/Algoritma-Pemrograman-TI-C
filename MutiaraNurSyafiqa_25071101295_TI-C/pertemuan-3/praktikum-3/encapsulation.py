##INI AKAN ERROR
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error


##
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

p1 = Person('Mutiara')
p1.set_grade(100)
print(p1.get_salary())




##MANGLING NAME
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())


class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Tidak boleh pakai ini