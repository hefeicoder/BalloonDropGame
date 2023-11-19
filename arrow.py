import pygame

ARROW_WIDTH = 80
ARROW_HEIGHT = 80

class Arrow:
    def __init__(self, start_x, start_y, target_x, target_y):
        self.image = pygame.image.load('resource/arrow.png')
        self.image = pygame.transform.scale(self.image, (ARROW_WIDTH, ARROW_HEIGHT))
        self.x = start_x
        self.y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 15  # Adjust as necessary

    def move(self):
        # Calculate the direction vector (dx, dy) towards the target
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Normalize the direction vector
        if distance != 0:
            dx /= distance
            dy /= distance

        # Move the arrow by its speed along the normalized direction vector
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
