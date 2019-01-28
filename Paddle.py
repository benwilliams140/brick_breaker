class Paddle:
    def __init__(self, x, y, width, height, velocity, screenWidth):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.colour = (255, 255, 255)
        self.direction = "null"
        self.screenWidth = screenWidth
		
    def updatePosition(self):
        if self.direction == "left":
            self.x -= self.velocity
        elif self.direction == "right":
            self.x += self.velocity
			
        if self.x < 0: self.x = 0
        if self.x + self.width > self.screenWidth: self.x = self.screenWidth - self.width

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def setDirection(self, direction):
        self.direction = direction

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getVelocity(self):
        return self.velocity

    def getColour(self):
        return self.colour

    def getDirection(self):
        return self.direction