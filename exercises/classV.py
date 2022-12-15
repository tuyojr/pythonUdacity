from classIV import PartyAnimal

class Football(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 3
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = Football("Jim")
j.party()
j.six()
# print(dir(j))

# Code: http://www.py4e.com/code3/party6.py
# Or select Download from this trinket's left-hand menu