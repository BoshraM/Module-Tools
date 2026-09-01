class Parent:  
  def __init__(self, first_name: str, last_name: str): 
    self.first_name = first_name
    self.last_name = last_name

  def get_name(self) -> str:
    return f"{self.first_name} {self.last_name}"


class Child(Parent):
  def __init__(self, first_name: str, last_name: str):
    super().__init__(first_name, last_name)
    self.previous_last_names = []

  def change_last_name(self, last_name) -> None:
    self.previous_last_names.append(self.last_name)
    self.last_name = last_name

  def get_full_name(self) -> str:
    suffix = ""
    if len(self.previous_last_names) > 0:
      suffix = f" (née {self.previous_last_names[0]})"
    return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print("1",person1.get_name()) # It should print "Elizaveta Alekseeva"
print("2",person1.get_full_name()) # It should print "Elizaveta Alekseeva"
person1.change_last_name("Tyurina") # Changes the last name to "Tyurina"
print("3",person1.get_name())# It should print "Elizaveta Alekseeva" # I was wrong here because the child's last_name has been changed to "Tyurina".
print("4",person1.get_full_name())# I thought it would print "Elizaveta Alekseeva (née Tyurina)" 
# I was wrong here again because I misunderstood how last_name and previous_last_names work.

person2 = Parent("Elizaveta", "Alekseeva")
print("5",person2.get_name()) # It should print "Elizaveta Alekseeva"
print("6",person2.get_full_name())  # Returns an error because Parent doesn't have a get_full_name() method.
person2.change_last_name("Tyurina") # Returns an error because Parent doesn't have a change_last_name() method.
print("7",person2.get_name()) # It should print "Elizaveta Alekseeva"
print(person2.get_full_name()) # returns an error again because Parent doesn't have a get_full_name() method.