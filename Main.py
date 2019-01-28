import pygame
import csv
import random
import time
import sys

from Brick import Brick
from Ball import Ball
from Paddle import Paddle

class Main:
	def __init__(self):
		pygame.init()
		#limits the speed of continuous key presses
		pygame.key.set_repeat(1, 1)
		random.seed()
		
		#initializes variables for game
		self.width = 800
		self.height = 800
		self.running = False
		self.level = "levels/level_test.csv"
		self.level_map = []
		
		#initializes variables for bricks
		self.bricks = []
		
		#initializes variables for paddle
		paddleWidth = 200
		paddleHeight = 20
		paddleX = self.width / 2 - paddleWidth / 2
		paddleY = self.height - paddleHeight - 10
		paddleVelocity = 8
		self.paddle = Paddle(paddleX, paddleY, paddleWidth, paddleHeight, paddleVelocity, self.width)
		
		#initializes variables for ball
		ballRadius = 15
		ballX = self.width / 2 - ballRadius
		ballY = paddleY - ballRadius * 2
		ballVelocityX = random.randint(3, 7)
		if random.randint(0, 2) == 0:
			ballVelocityX *= -1
		ballVelocityY = random.randint(3, 8) * -1
		self.ball = Ball(self.paddle, ballX, ballY, ballRadius, ballVelocityX, ballVelocityY, self.width, self.height)
		
		#initializes the screen
		self.screen = pygame.display.set_mode((self.width, self.height))

	def getInput(self):
		#loops through all of the events received
		events = pygame.event.get()
		for event in events:
			#quits the game if the 'X' button is clicked
			if event.type == pygame.QUIT:
				self.end()
				
			#tests which key on the keyboard is clicked
			if event.type == pygame.KEYDOWN:
				#updates paddle direction to left
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					self.paddle.setDirection("left")
				#updates paddle direction to right
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					self.paddle.setDirection("right")
				#quits the game if escape is clicked
				if event.key == pygame.K_ESCAPE:
					self.end()
	
	def loadLevel(self):
		#opens the csv file containing the level
		file = open(self.level)
		reader = csv.reader(file)
		
		self.level_map = []
		
		#loops through the file and adds each element to an array
		for row in reader:
			row_contents = []
			for col in row:
				row_contents.append(col)
			self.level_map.append(row_contents)
		
		#loops through the array and loads the level
		for i in range(len(self.level_map)):
			for j in range(len(self.level_map[i])):
				#creates a new Brick object for every brick in the level
				if self.level_map[i][j] == 'b':
					brickX = j * 100 + 5
					brickY = i * 50 + 5
					brickTier = 1
					self.bricks.append(Brick(brickX, brickY, brickTier))
		
	def update(self):
		#updates the paddle position
		self.paddle.updatePosition()
		self.ball.updatePosition()
		
		if self.ball.getRunning() == False:
			self.end()
		
		self.paddle.setDirection("null")
		
	def render(self):
		#creates a background for the game
		self.screen.fill((255, 255, 255))
		
		#loops through the bricks array and draws each brick to the screen
		for i in range(len(self.bricks)):
			pygame.draw.rect(self.screen, (200, 100, 100), (self.bricks[i].getX(), self.bricks[i].getY(), self.bricks[i].getWidth(), self.bricks[i].getHeight()))
		
		#draws the paddle to the screen
		pygame.draw.rect(self.screen, (0, 0, 0), (self.paddle.getX(), self.paddle.getY(), self.paddle.getWidth(), self.paddle.getHeight()))
		
		#draws the ball to the screen
		pygame.draw.circle(self.screen, (0, 0, 0), (int(self.ball.getX()), int(self.ball.getY())), self.ball.getRadius())
		
		#updates the screen
		pygame.display.update()
		
	def main(self):
		#loads the level and prints contents to the console
		self.loadLevel()
		print(self.level_map)
		print(self.bricks)
	
		#main game loop
		while self.running:
			self.getInput()
			self.update()
			self.render()
			#delays program
			time.sleep(0.01)
			
		#exits the program
		pygame.quit()
		sys.exit()
			
	def start(self):
		#starts the game
		self.running = True
		self.main()
		
	def end(self):
		#ends the game
		self.running = False
		
#initializes and starts the game
main = Main()
main.start()