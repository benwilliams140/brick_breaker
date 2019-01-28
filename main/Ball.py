class Ball:
	def __init__(self, paddle, x, y, radius, velocityX, velocityY, screenWidth, screenHeight):
		self.x = x
		self.y = y
		self.radius = radius
		self.velocityX = velocityX
		self.velocityY = velocityY
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight
		self.running = True
		self.paddle = paddle
		
	def updatePosition(self):
		self.x += self.velocityX
		self.y += self.velocityY
		
		if self.x - self.radius < 0 or self.x + self.radius > self.screenWidth:
			self.velocityX *= -1
		if self.paddle.getX() < self.x < self.paddle.getX() + self.paddle.getWidth():
			if self.y + self.radius > self.paddle.getY():
				self.velocityY *= -1
		if self.y + self.radius > self.screenHeight:
			self.running = False
		if self.y - self.radius < 0:
			self.velocityY *= -1
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getRadius(self):
		return self.radius
		
	def getRunning(self):
		return self.running
