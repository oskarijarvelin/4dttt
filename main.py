class Square:
	
	def __init__(self, coords):
		pass
		
	def add_mark(self, player):
		pass
	
class Line:
	
	def __init__(self, params):
		pass
		
	def squares(self):
		pass
	
	def win(self):
		pass
		
	def not_winnable(self):
		pass
	

class TTT_Table:
	
	def __init__(self, base, power, players):
		self.base = base
		self.power = power
		self.squares = {}
		self.add_squares_recursive(self.power - 1, [])
		self.players = players
		self.turn = self.players[0]
		
	def add_squares_recursive(self, powerleft, list):
		for i in range(0, self.power):
			if powerleft == 0:
				self.squares[''.join(list + [str(i)])] = Square(list + [i])
			else:
				self.add_squares_recursive(powerleft - 1, list + [str(i)])
		
	def list_lines(self):
		pass
	
	def win(self):
		pass
		
	def add_mark(self, player):
		pass
	
class Player:
	
	def __init__(self, name, mark):
		self.name = name
		self.mark = mark
	
table = TTT_Table(4, 4, [1])
print(table.squares)