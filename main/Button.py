import pygame

class Button:
	def __init__(self, x, y, width, height, text):
		pygame.init()
		pygame.font.init()
		
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.text = text

	def render(self, screen):		
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
		
		
		font = pygame.font.SysFont("Times New Roman", 24)
		(fontWidth, fontHeight) = font.size(self.text)

		fontX = self.x + self.width / 2 - fontWidth / 2
		fontY = self.y + self.height / 2 - fontHeight / 2
		
		textSurface = font.render(self.text, False, (0, 0, 0))
		
		screen.blit(textSurface, (fontX, fontY))
		
		
	def isClicked(self):
		(mouseX, mouseY) = pygame.mouse.get_pos()
		(mouseClicked, _, __) = pygame.mouse.get_pressed()
		
		if mouseClicked:
			if self.x <= mouseX <= self.x + self.width:
				if self.y <= mouseY <= self.y + self.height:
					return True
		
		return False