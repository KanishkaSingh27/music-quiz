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
RED = (255, 0, 0)
GREEEN=(0,255,13)

# Fonts
FONT = pygame.font.Font(None, 30)
LARGE_FONT = pygame.font.Font(None, 50)

# Questions and answers
questions = [
    {"question": "Which singer is known as the 'Nightingale of India'?",
     "options": ["Alka Yagnik", "Shreya Ghoshal", "Lata Mangeshkar", "Asha Bhosle"],
     "answer": "Lata Mangeshkar"},
    {"question": "The title of Prabh Deep’s debut album that explores life in Delhi?",
     "options": ["Insaan", "Class-sikh", "Shakti", "Kohinoor"],
     "answer": "Class-sikh"},
    {"question": "Which singer won the National Award for the song Sandese Aate Hain?",
     "options": ["Sonu Nigam", "Udit Narayan", "Mika Singh", "Hariharan"],
     "answer": "Sonu Nigam"},
    {"question": "Which 2001 movie featured the song Mitwa sung by Shankar Mahadevan?",
     "options": ["Kal ho na ho", "Kabhi alvida na kehna", "Dil chahta hai", "Lagaan"],
     "answer": "Kabhi alvida na kehna"},
    {"question": "Which Michael Jackson hit from Thriller features iconic 'moonwalk'?",
     "options": ["Billie Jean", "Thriller", "Beat It", "Wanna be startin Somethin"],
     "answer": "Billie Jean"},
    {"question": "Which Queen song is known for its anthemic chorus at sports events?",
     "options": ["Bohemian Rhapsody", "We are the champions", "We will rock you", "Don't stop me now"],
     "answer": "We will rock you"},
    {"question": "What is Djo’s real name, the singer of 'End of Beginning'?",
     "options": ["Finn Wolfhard", "David Harbour", "Daniel Radcliffe", "Joe Keery"],
     "answer": "Joe Keery"},
    {"question":"The album 'Revolver' was by which boy band?",
    "options": ["Backstreet Boys", "The Beatles", "Jonas Brothers","Radiohead"],
    "answer": "The Beatles"},
    {"question": "Which singer holds the record for the most Grammy awards won?",
    "options": ["Billie Eilish","Taylor Swift","Beyonce", "Honey Singh"],
    "answer":"Beyonce"},
     {"question": "Which classical composer became deaf but continued to compose music?",
     "options": ["Johann Sebastian Bach", "Ludwig van Beethoven", "Antonio Vivaldi", "Wolfgang Amadeus Mozart"],
     "answer": "Ludwig van Beethoven"},
       {"question": "Which band released the iconic album 'Dark Side of the Moon'?",
     "options": ["Pink Floyd", "Led Zeppelin", "The Who", "The Rolling Stones"],
     "answer": "Pink Floyd"},
     {"question": "Which artist is known as the 'Queen of Pop'?",
     "options": ["Britney Spears", "Madonna", "Janet Jackson", "Christina Aguilera"],
     "answer": "Madonna"},
      {"question": "The iconic song 'Ek Do Teen' was performed by which actress?",
     "options": ["Madhuri Dixit", "Sridevi", "Juhi Chawla", "Rekha"],
     "answer": "Madhuri Dixit"}

]

# Shuffle questions and options
for q in questions:
    random.shuffle(q["options"])
random.shuffle(questions)

# Game variables
score = 0
current_question = 0
game_over = False
start_game = False

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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            if not start_game:
                start_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2), (BUTTON_WIDTH, BUTTON_HEIGHT))
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    start_game = True
                    random.shuffle(questions)
                    pygame.time.delay(600)

            elif game_over:
                restart_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 40), (BUTTON_WIDTH, BUTTON_HEIGHT))
                if restart_button_rect.collidepoint(mouse_x, mouse_y):
                    pygame.time.delay(600)
                    score = 0
                    current_question = 0
                    game_over = False
                    random.shuffle(questions)

            else:
                for i in range(4):
                    button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_SPACING)),
                                               (BUTTON_WIDTH, BUTTON_HEIGHT))
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        selected_option = questions[current_question]["options"][i]
                        feedback_color = GREEEN if selected_option == questions[current_question]["answer"] else RED
                        pygame.draw.rect(screen, feedback_color, button_rect)
                        option_text = FONT.render(selected_option, True, BLACK)
                        screen.blit(option_text, (button_rect.x + BUTTON_WIDTH // 2 - option_text.get_width() // 2,
                                                  button_rect.y + BUTTON_HEIGHT // 2 - option_text.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.delay(500)

                        if feedback_color == GREEN:
                            score += 1
                        current_question += 1
                        if current_question >= len(questions):
                            game_over = True
                        break

    # Drawing
    screen.fill(BLACK)

    if not start_game:
        # Opening page
        title_text = LARGE_FONT.render("Welcome to Music Quiz!", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))

        start_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2), (BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(screen, GREEN, start_button_rect)
        start_button_label = FONT.render("Start Game", True, BLACK)
        screen.blit(start_button_label, (start_button_rect.x + BUTTON_WIDTH // 2 - start_button_label.get_width() // 2,
                                         start_button_rect.y + BUTTON_HEIGHT // 2 - start_button_label.get_height() // 2))
        
    elif game_over:
        # Game over screen
        game_over_text = FONT.render(f"Game Over! Your score: {score}", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 20))

        # Draw Restart button
        restart_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 40), (BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(screen, GREEN, restart_button_rect)
        restart_button_label = FONT.render("Restart", True, BLACK)
        screen.blit(restart_button_label, (restart_button_rect.x + BUTTON_WIDTH // 2 - restart_button_label.get_width() // 2,
                                           restart_button_rect.y + BUTTON_HEIGHT // 2 - restart_button_label.get_height() // 2))
    else:
        # Display current question
        question_text = FONT.render(questions[current_question]["question"], True, WHITE)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, 90))

        # Display score
        score_text = FONT.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH - score_text.get_width() - 40, 40))

        # Display options as buttons
        for i, option in enumerate(questions[current_question]["options"]):
            button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_SPACING)),
                                       (BUTTON_WIDTH, BUTTON_HEIGHT))
            pygame.draw.rect(screen, BLUE, button_rect)
            option_text = FONT.render(option, True, BLACK)
            screen.blit(option_text, (button_rect.x + BUTTON_WIDTH // 2 - option_text.get_width() // 2,
                                      button_rect.y + BUTTON_HEIGHT // 2 - option_text.get_height() // 2))

    pygame.display.flip()
