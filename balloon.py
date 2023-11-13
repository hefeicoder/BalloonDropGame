import pygame
import random
from question_set import question_addition_within_twenty

class Balloon:
    BALLOON_SIZE = 100
    # Load the balloon image as a class variable (adjust the file path as needed)
    balloon_image = pygame.image.load('resource/balloon_t2.png')
    balloon_image = pygame.transform.scale(balloon_image, (BALLOON_SIZE, BALLOON_SIZE))  # Resize as needed

    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = -Balloon.BALLOON_SIZE  # Start above the screen
        self.color = (255, 0, 0)  # Red color for the balloon
        self.font = pygame.font.Font(None, 30)
        self.question, self.answer = question_addition_within_twenty()
        self.speed = random.uniform(0.2, 1)  # Speed of the balloon's movement

    def generate_problem(self):
        """ Generates a simple addition problem. """
        return self.question

    def draw(self, screen):
        """ Draws the balloon with its math problem on the screen. """
        screen.blit(Balloon.balloon_image, (self.x - Balloon.BALLOON_SIZE/2, self.y - Balloon.BALLOON_SIZE/2))  # Adjust position to center the balloon

        # pygame.draw.circle(screen, self.color, (self.x, self.y), 30)
        problem_text = self.font.render(self.question, True, (255, 255, 255))
        text_rect = problem_text.get_rect(center=(self.x, self.y))
        screen.blit(problem_text, text_rect)

    def update(self):
        """ Updates the balloon's position. """
        self.y += self.speed

    def check_answer(self, user_answer):
        """ Checks if the user's answer matches the balloon's answer. """
        return user_answer == self.answer
