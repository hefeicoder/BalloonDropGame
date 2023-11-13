import pygame
import sys
from balloon import Balloon

def run_game():
    pygame.init()

    # Constants for the game
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOR = (255, 255, 255)  # White background

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Math Balloon Pop Game')

    # Create a list of balloons
    balloons = [Balloon() for _ in range(1)]
    user_answer = ""  # To store user's current input
    score = 0  # Player's score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check user's answer and pop balloon if correct
                    for balloon in balloons:
                        if balloon.check_answer(int(user_answer)):
                            balloons.remove(balloon)
                            balloons.append(Balloon())
                            score += 1
                            break
                    user_answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    user_answer += event.unicode

        # Update balloons
        for balloon in balloons:
            balloon.update()
            # Check if any balloon has reached the bottom
            if balloon.y > SCREEN_HEIGHT:
                pygame.quit()
                sys.exit()

        screen.fill(BG_COLOR)

        # Draw balloons
        for balloon in balloons:
            balloon.draw(screen)

        # Display user answer and score
        font = pygame.font.Font(None, 36)
        answer_surf = font.render(user_answer, True, (0, 0, 0))
        score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(answer_surf, (20, SCREEN_HEIGHT - 40))
        screen.blit(score_surf, (SCREEN_WIDTH - 120, 20))

        pygame.display.flip()

if __name__ == "__main__":
    run_game()
