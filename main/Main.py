import pygame
import csv
import random
import time
import sys

from Brick import Brick
from Ball import Ball
from Paddle import Paddle
from Button import Button

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
		
		#state of the game
		self.game_state = "MENU"
		
		self.menu_objects = {}
		self.menu_objects["playButton"] = Button(self.width / 2 - 75, self.height - 255, 150, 50, "Play Game")
		self.menu_objects["selectLevelButton"] = Button(self.width / 2 - 75, self.height - 200, 150, 50, "Select Level")
		self.menu_objects["instructionsButton"] = Button(self.width / 2 - 75, self.height - 145, 150, 50, "Instructions")
		self.menu_objects["backButton"] = Button(5, self.height - 55, 150, 50, "Back")
		
		#initializes variables for bricks
		self.bricks = []
		
		self.initPaddle()
		self.initBall()
		
		self.paddle = Paddle(self.paddleX, self.paddleY, self.paddleWidth, self.paddleHeight, self.paddleVelocity, self.width)
		self.ball = Ball(self.paddle, self.ballX, self.ballY, self.ballRadius, self.ballVelocityX, self.ballVelocityY, self.width, self.height)
		
		#initializes the screen
		self.screen = pygame.display.set_mode((self.width, self.height))

	def initPaddle(self):
		#initializes variables for paddle
		self.paddleWidth = 200
		self.paddleHeight = 20
		self.paddleX = self.width / 2 - self.paddleWidth / 2
		self.paddleY = self.height - self.paddleHeight - 10
		self.paddleVelocity = 4
		
	def initBall(self):
		#initializes variables for ball
		self.ballRadius = 15
		self.ballX = self.width / 2 - self.ballRadius
		self.ballY = self.paddleY - self.ballRadius * 2
		self.ballVelocityX = random.randint(4, 7)
		if random.randint(0, 1) == 0:
			self.ballVelocityX *= -1
		self.ballVelocityY = random.randint(5, 7) * -1
		
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
		#tests which game state the game is in
		if self.game_state == "PLAYING":
			#updates the paddle position
			self.paddle.update()
			self.ball.update()
		
			if self.ball.getRunning() == False:
				self.game_state = "MENU"
				self.reset()
				
			for brick in self.bricks:
				if brick.isColliding(self.ball):
					self.bricks.remove(brick)
		
			self.paddle.setDirection("null")
		elif self.game_state == "MENU":
			#tests if buttons are clicked
			if self.menu_objects["playButton"].isClicked():
				self.game_state = "PLAYING"
			elif self.menu_objects["selectLevelButton"].isClicked():
				self.game_state = "SELECT LEVEL"
			elif self.menu_objects["instructionsButton"].isClicked():
				self.game_state = "INSTRUCTIONS"
		elif self.game_state == "INSTRUCTIONS" or self.game_state == "SELECT LEVEL":
			if self.menu_objects["backButton"].isClicked():
				self.game_state = "MENU"
		
	def render(self):
		#creates a background for the game
		self.screen.fill((0, 0, 0))
	
		#tests which game state the game is in
		if self.game_state == "PLAYING":
			#loops through the bricks array and draws each brick to the screen
			for i in range(len(self.bricks)):
				pygame.draw.rect(self.screen, (200, 100, 100), (self.bricks[i].getX(), self.bricks[i].getY(), self.bricks[i].getWidth(), self.bricks[i].getHeight()))
		
			#draws the paddle to the screen
			self.paddle.render(self.screen)
			
			#draws the ball to the screen
			self.ball.render(self.screen)
		elif self.game_state == "MENU":
			#draws the menu elements to the screen
			self.menu_objects["playButton"].render(self.screen)
			self.menu_objects["selectLevelButton"].render(self.screen)
			self.menu_objects["instructionsButton"].render(self.screen)
		elif self.game_state == "INSTRUCTIONS":
			self.menu_objects["backButton"].render(self.screen)
		elif self.game_state == "SELECT LEVEL":
			self.menu_objects["backButton"].render(self.screen)
		
		#updates the screen
		pygame.display.update()
	
	def reset(self):
		self.loadLevel()
		
		self.initBall()
		self.initPaddle()
		
		self.ball.reset(self.ballX, self.ballY, self.ballVelocityX, self.ballVelocityY)
		self.paddle.reset(self.paddleX)
	
	def main(self):
		#loads the level and prints contents to the console
		self.loadLevel()
	
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
