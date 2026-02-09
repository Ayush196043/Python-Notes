#
class Person:
    name = "Ayush"
    occupation = "AIML Engineer"
    networth = 10

    def info(self):  # method
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.name = "Astha Pandey" # A ka naam change kiya ja rahahai.
a.occupation = "Docter" # A ka occupation chande kiya ja rahahai.
# print(a.name,a.occupation)
a.info()

# self :- self ka matlab yo object jis ke liye method call kiya ja raha hai
