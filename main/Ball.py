import pygame

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
		
	def render(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
		
	def reset(self, x, y, velocityX, velocityY):
		self.x = x
		self.y = y
		self.velocityX = velocityX
		self.velocityY = velocityY
		self.running = True
		
	def update(self):
		self.x += self.velocityX
		self.y += self.velocityY
		
		if self.x - self.radius < 0 or self.x + self.radius > self.screenWidth:
			self.velocityX *= -1
		if self.paddle.getX() < self.x < self.paddle.getX() + self.paddle.getWidth():
			if self.y + self.radius > self.paddle.getY():
				self.velocityY *= -1
				if self.x - self.paddle.getX() < 50:
					self.velocityX = -int(100 / (self.x - self.paddle.getX()))
				elif self.x - self.paddle.getX() > 150:
					self.velocityX = int((self.x - self.paddle.getX()) / 20)
		if self.y + self.radius > self.screenHeight:
			self.running = False
		if self.y - self.radius < 0:
			self.velocityY *= -1
			
	def flipDirectionX(self):
		self.velocityX *= -1
		
	def flipDirectionY(self):
		self.velocityY *= -1
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getRadius(self):
		return self.radius
		
	def getRunning(self):
		return self.running
