import pygame
import random
from pygame import mixer
from question_set import question_addition_within_twenty

class Balloon:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = -50  # Start above the screen
        self.color = (255, 0, 0)  # Red color for the balloon
        self.font = pygame.font.Font(None, 30)
        self.question, self.answer = question_addition_within_twenty()
        self.speed = random.uniform(0.2, 1)  # Speed of the balloon's movement

    def generate_problem(self):
        """ Generates a simple addition problem. """
        return self.question

    def draw(self, screen):
        """ Draws the balloon with its math problem on the screen. """
        pygame.draw.circle(screen, self.color, (self.x, self.y), 30)
        problem_text = self.font.render(self.question, True, (0, 0, 0))
        text_rect = problem_text.get_rect(center=(self.x, self.y))
        screen.blit(problem_text, text_rect)

    def update(self):
        """ Updates the balloon's position. """
        self.y += self.speed

    def check_answer(self, user_answer):
        """ Checks if the user's answer matches the balloon's answer. """
        return user_answer == self.answer
