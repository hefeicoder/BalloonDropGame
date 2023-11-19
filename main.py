import pygame
import sys
from balloon import Balloon
from sound import SoundManager, SOUND_CORRECT, SOUND_WRONG, SOUND_GREAT, SOUND_OHNO
from question_set import question_multiplication_single_digit, question_addition_within_twenty
from arrow import Arrow

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 1024

starting_x = WINDOW_WIDTH // 2  # Half of the screen width
starting_y = WINDOW_HEIGHT  # Bottom of the screen

BALLOON_NUM = 2

def arrow_reaches_balloon(arrow, balloon):
    # Define the 'radius' or size for the arrow and balloon for collision detection
    # These values should be adjusted based on the actual size of your arrow and balloon images
    arrow_size = 15  # Half the width or height of the arrow image, assuming a square bounding box
    balloon_size = 50  # Half the width or height of the balloon image, assuming a square bounding box

    # Calculate the distance between the arrow and the balloon
    dx = arrow.x - balloon.x
    dy = arrow.y - balloon.y
    distance = (dx ** 2 + dy ** 2) ** 0.5  # Pythagorean theorem

    # Check if the distance is less than the sum of the 'sizes' (indicating a collision)
    return distance < (arrow_size + balloon_size)


def run_game():
    pygame.init()
    SoundManager.init()

    # Load the background image
    background_image = pygame.image.load('resource/background.png')
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))  # Resize to fit your window

    # Constants for the game
    SCREEN_WIDTH, SCREEN_HEIGHT = WINDOW_WIDTH, WINDOW_HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Math Balloon Pop Game')

    gen_func = question_multiplication_single_digit


    # Create a list of balloons
    balloons = [Balloon(gen_func) for _ in range(BALLOON_NUM)]
    user_answer = ""  # To store user's current input
    score = 0  # Player's score
    missed = 0

    arrows = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    # Check user's answer and pop balloon if correct
                    isAnyCorrect = False
                    for balloon in balloons:
                        if balloon.check_answer(int(user_answer)):
                            score += 1
                            arrows.append(Arrow(starting_x, starting_y, balloon.x, balloon.y))
                            if score % 5 == 0:
                                SoundManager.play_sound(SOUND_GREAT)
                            else:
                                SoundManager.play_sound(SOUND_CORRECT)
                            isAnyCorrect = True
                            break
                    user_answer = ""
                    if not isAnyCorrect:
                        missed += 1  # Increment the missed counter
                        SoundManager.play_sound(SOUND_WRONG)
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    user_answer += event.unicode


        # Update balloons
        for balloon in balloons:
            balloon.update()
            # Check if any balloon has reached the bottom
            if balloon.y > SCREEN_HEIGHT:
                SoundManager.play_sound(SOUND_OHNO)
                balloons.remove(balloon)
                balloons.append(Balloon(gen_func))  # Add a new balloon

        screen.blit(background_image, (0, 0))

        # Update arrows
        for arrow in arrows:
            # Check for collision with the balloon
            for balloon in balloons:
                if arrow_reaches_balloon(arrow, balloon):  # Implement this function
                    # Handle balloon popping
                    balloons.remove(balloon)
                    balloons.append(Balloon(gen_func))
                    arrows.remove(arrow)  # Remove the arrow
                    break

        # Draw balloons
        for balloon in balloons:
            balloon.draw(screen)

        # Draw arrows
        for arrow in arrows:
            arrow.move()
            arrow.draw(screen)

        # Display user answer and score
        font = pygame.font.Font(None, 36)
        answer_surf = font.render(user_answer, True, (0, 0, 0))
        score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
        missed_surf = font.render(f"Missed: {missed}", True, (0, 0, 0))
        screen.blit(answer_surf, (20, SCREEN_HEIGHT - 40))
        screen.blit(score_surf, (SCREEN_WIDTH - 120, 20))
        screen.blit(missed_surf, (SCREEN_WIDTH - 120, 60))

        pygame.display.flip()

if __name__ == "__main__":
    run_game()


