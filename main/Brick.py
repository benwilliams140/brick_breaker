class Brick:
	def __init__(self, x, y, teir):
		self.x = x
		self.y = y
		self.width = 90
		self.height = 40
		self.teir = teir
		
	def isColliding(self, ball):
		if self.x < ball.getX() + ball.getRadius() and self.x + self.width > ball.getX() - ball.getRadius():
			if self.y < ball.getY() + ball.getRadius() and self.y + self.height > ball.getY() - ball.getRadius():
				if self.y < ball.getY() < self.y + self.height:
					ball.flipDirectionX()
				else:
					ball.flipDirectionY()
				return True
		return False
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
	
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
		
	def getTeir(self):
		return self.teir
