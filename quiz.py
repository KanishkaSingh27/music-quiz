import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Quiz")

# Colors
BLUE = (93, 200, 246)
WHITE = (255, 245, 248)
BLACK = (32, 32, 32)
GREEN = (198, 255, 198)

# Fonts
FONT = pygame.font.Font(None, 30)

# Questions and answers
questions = [
    {"question": "Which singer is known as the 'Nightingale of India'?", "options": ["Alka Yagnik", "Shreya Ghoshal", "Lata Mangeshkar", "Asha Bhosle"], "answer": 2},
    {"question": "The title of Prabh Deep’s debut album that explores life in Delhi?", "options": ["Insaan", "Class-sikh", "Shakti", "Kohinoor"], "answer": 1},
    {"question": "Which singer won the National Award for the song Sandese Aate Hain?", "options": ["Sonu Nigam", "Udit Narayan", "Mika Singh", "Hariharan"], "answer": 3},
    {"question": "Which 2001 movie featured the song Mitwa sung by Shankar Mahadevan?","options":["Kal ho na ho","Kabhi khushi kabhi gham","Dil chahta hai","Lagaan"],"answer": 2},
    {"question": "Which Michael Jackson hit from Thriller features iconic dance moves?","options":["Billie Jean","Thriller","Beat It","Wanna be startin Somethin"],"answer":0},
    {"question": "Which Queen song is known for its anthemic chorus at sports events?","options":["Bohemian Rhaspody","We are the champions","We will rock you","Don't stop me now"],"answer":1}
]

# Shuffle questions and options
random.shuffle(questions)
for question in questions:
    options = question["options"]
    question["answer"] = options.index(options[question["answer"]])
    random.shuffle(options)

# Game variables
score = 0
current_question = 0
game_over = False

# Button dimensions
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 50
BUTTON_Y_START = 150
BUTTON_SPACING = 20

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = event.pos
            if game_over:
                restart_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 40), (BUTTON_WIDTH, BUTTON_HEIGHT))
                if restart_button_rect.collidepoint(mouse_x, mouse_y):
                    pygame.time.delay(600) 
                    score = 0
                    current_question = 0
                    game_over = False
                    random.shuffle(questions)
                    for question in questions:
                        options = question["options"]
                        question["answer"] = options.index(options[question["answer"]])
                        random.shuffle(options)
            else:
                for i in range(4):
                    button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_SPACING)), (BUTTON_WIDTH, BUTTON_HEIGHT))
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        if i == questions[current_question]["answer"]:
                            score += 1
                        current_question += 1
                        if current_question >= len(questions):
                            game_over = True
                        pygame.time.delay(500)  # Delay before showing the next question

    # Drawing
    screen.fill(BLACK)

    if game_over:
        # Game over screen
        game_over_text = FONT.render(f"Game Over! Your score: {score}", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 20))

        # Draw Restart button
        restart_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 40), (BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(screen, GREEN, restart_button_rect)
        restart_button_label = FONT.render("Restart", True, BLACK)
        
        screen.blit(restart_button_label, (restart_button_rect.x + BUTTON_WIDTH // 2 - restart_button_label.get_width() // 2, restart_button_rect.y + BUTTON_HEIGHT // 2 - restart_button_label.get_height() // 2))
      
    else:
        # Display current question
        question_text = FONT.render(questions[current_question]["question"], True, WHITE)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, 50))

        # Display options as buttons
        for i, option in enumerate(questions[current_question]["options"]):
            button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_SPACING)), (BUTTON_WIDTH, BUTTON_HEIGHT))
            pygame.draw.rect(screen, BLUE, button_rect)
            option_text = FONT.render(option, True, BLACK)
            screen.blit(option_text, (button_rect.x + BUTTON_WIDTH // 2 - option_text.get_width() // 2, button_rect.y + BUTTON_HEIGHT // 2 - option_text.get_height() // 2))

    pygame.display.flip()
