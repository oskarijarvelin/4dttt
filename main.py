class Square:
	
	def __init__(self, coords):
		self.value = ""
        self.coords = coords
		
	def add_mark(self, player):		
        self.value = player.mark
	
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
		self.players = players
		self.turn = self.players[0]
		
	def add_squares_recursive(self):
		pass
		
	def list_lines(self):
		pass
	
	def win(self):
		pass
		
	def add_mark(self, player):
		pass
	
class Player:
	
	def __init__(self, name, mark)
		self.name = name
		self.mark = mark
	
