import random

class Game:
	def __init__(self):
		self.matrix_size = int(input("please Enter game size? "))
		self.matrix_level = input("please choose the level\
'E', 'M', 'H' for easy, meduim or hard ")
		self.bombs_coordinates = []
		self.player_moves = []
		self.num_of_bombs = 0
		self.matrix = self.matrix()
		self.zero_values = []
		self.checked_values =[]
		self.planting_bombs()
		self.updating_values()
		self.num_of_remains = (self.matrix_size**2)-self.num_of_bombs
		
	def matrix(self):
		matrix = [[None for i in range(self.matrix_size)]for i in range(self.matrix_size)]
		return matrix
		
	def printing(self):
		print(f"remainig {self.num_of_remains}\nNumber of bombs = {self.num_of_bombs}\n")
		v_matrix = [[None for i in range(self.matrix_size)]for i in range(self.matrix_size)]
		print("     ", end="")
		for i in range(self.matrix_size):
			print("    ",i, end="")
		print("\n","ـ"*10*self.matrix_size)
		for x in range(self.matrix_size):
			print(x," ||", end="")
			for y in range(self.matrix_size):
				if (x,y) in self.player_moves:
					print("    ", self.matrix[x][y] , end="")
				else:
					print("    ", "|" , end="")
			print("\n")
			
	def losing_print(self):
		print("     ")
		for i in range(self.matrix_size):
			print("    ",i, end="")
		print("\n","ـ"*10*self.matrix_size)
		for i in range(self.matrix_size):
			print(i," ||", end="")
			for item in self.matrix[i]:
				print("    ", item , end="")
			print("\n")
	
	def planting_bombs(self):
		level = {
		"e": int(.17 * self.matrix_size**2),
		"m": int(.34 * self.matrix_size**2),
		"h": int(.6 * self.matrix_size**2),
		}
		num_of_bombs = level[self.matrix_level.lower()]
		while len(self.bombs_coordinates) < num_of_bombs:
			x = random.randint(0, self.matrix_size-1)
			y = random.randint(0, self.matrix_size-1)
			bomb_coor = (x,y)
			if bomb_coor in self.bombs_coordinates:
				continue
			else:
				self.matrix[x][y] = "*"
				self.bombs_coordinates.append(bomb_coor)
				self.num_of_bombs += 1
			
	def updating_values(self):
		for row in self.matrix:
			for item in row:
				x = self.matrix.index(row)
				y = row.index(item)
				if item == "*":
					continue
				else:
						self.matrix[x][y] = 0
						#Check UP
						if x > 0 and self.matrix[x-1][y]=="*":
							self.matrix[x][y] += 1
						#Check Down
						if x < self.matrix_size - 1 and self.matrix[x+1][y]=="*":
							self.matrix[x][y] += 1
						# check Right
						if y < self.matrix_size - 1 and self.matrix[x][y+1]=="*":
							self.matrix[x][y] += 1
						# Check Left
						if y > 0 and self.matrix[x][y-1]=="*":
							self.matrix[x][y] += 1
						# chech UP Right
						if x > 0 and y < self.matrix_size - 1 and \
						self.matrix[x-1][y+1] =="*":
							self.matrix[x][y] += 1
						# Check UP Left
						if x > 0 and y > 0 and self.matrix[x-1][y-1]=="*":
							self.matrix[x][y] += 1
						# Check Down right
						if x < self.matrix_size - 1 and y < self.matrix_size - 1\
						and self.matrix[x+1][y+1]=="*":
							self.matrix[x][y] += 1
						# Check Down left
						if x < self.matrix_size - 1 and y > 0 and \
						self.matrix[x+1][y-1] =="*":
							self.matrix[x][y] += 1
	def check_zero(self,row,col):
		for x in range(max(0 , row-1), min(self.matrix_size-1, row+1)+1):
			for y in range(max(0 , col-1), min(self.matrix_size-1, col+1)+1):
				if (x,y) in self.player_moves:
					continue
				else:
					if self.matrix[x][y] == 0:
						self.player_moves.append((x,y))
						self.zero_values.append((x,y))
					else:
						continue
		
			
	def zero_value(self,x,y):
		if self.matrix[x][y] == 0:
			self.zero_values.append((x,y))
			for item in self.zero_values:
				xx = item[0]
				yy = item[1]
				self.check_zero(xx,yy)

def play():
	game = Game()
	game.printing()
	while True:
		player_move = input("please Enter the coordinates row tnen space then column ")
		player_move = player_move.split()
		x = int(player_move[0])
		y = int(player_move[1])
		if x > game.matrix_size - 1 or y > game.matrix_size - 1:
			print("Out of range coordinates")
			continue
		elif (x,y) in game.bombs_coordinates:
			print("Game Over")
			game.losing_print()
			break
		else:
			if (x,y) in game.player_moves:
				print("Coordiantes already been played")
				continue
			else:
				if game.matrix[x][y] > 0:
					game.player_moves.append((x,y))
				elif game.matrix[x][y] == 0:
					game.zero_value(x,y)
				game.num_of_remains = (game.matrix_size**2)-game.num_of_bombs - len(game.player_moves)
				if game.num_of_remains == 0:
					print("Congrats You've Won ")
					break
				game.printing()
				print(game.player_moves)
				
	
if __name__ == "__main__":
	play()

