import pygame
from NLGlite.NLGlite import NLGlite_ as nlg


def draw_text(text):
    font = pygame.font.SysFont(None, 32)  # Choose a font and size
    text_surface = font.render(text, True, (0, 0, 0))
    textbox_x = WIDTH // 2 - text_surface.get_width() // 2
    textbox_y = 40 + text_surface.get_height() // 2
    textbox_width, textbox_height = text_surface.get_size()
    pygame.draw.rect(screen, (125, 125, 125), (textbox_x - 5, textbox_y - 5,
                                               textbox_width + 10, textbox_height + 10))
    screen.blit(text_surface, (textbox_x, textbox_y))


model = nlg()
model.set_config_file_path(
    "C:/Users/Danbo/Documents/UoN_CompSci/Year 3/COMP3003/Project/NLGlite/src/data/config/books/pokemon.lcfg")

# Define some colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Define the screen size
WIDTH = 800
HEIGHT = 600

sentence = ""

SHOW_TEXTBOX = False

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Random NPC text demo")

game_map = pygame.image.load("./assets/map.png").convert()
player_sprite = pygame.transform.scale(pygame.image.load("./assets/player.png").convert_alpha(), (56, 64))
non_player_sprite = pygame.transform.scale(pygame.image.load("./assets/non_player.png").convert_alpha(), (56, 64))


# Define the player radius
player_radius = 20

# Define the player starting position
player_x = WIDTH // 2
player_y = HEIGHT // 2

# Create a clock to track time
clock = pygame.time.Clock()

flag = True

# Speed of player movement (adjust as needed)
player_speed = 56  # pixels per second

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Get the time elapsed since the last frame (in seconds)
    dt = clock.tick() / 1000  # convert milliseconds to seconds

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Move the player based on pressed keys (using dt for frame-rate independence)
    if keys[pygame.K_w] and player_y >= 183:
        player_y -= player_speed * dt  # Move up
        SHOW_TEXTBOX = False
    if keys[pygame.K_s]:
        player_y += player_speed * dt  # Move down
        SHOW_TEXTBOX = False
    if keys[pygame.K_a]:
        player_x -= player_speed * dt  # Move left
        SHOW_TEXTBOX = False
    if keys[pygame.K_d]:
        player_x += player_speed * dt  # Move right
        SHOW_TEXTBOX = False

    # Check for boundary collisions
    player_x = max(player_radius, min(player_x, WIDTH - player_radius))
    player_y = max(player_radius, min(player_y, HEIGHT - player_radius))

    # Fill the screen with white
    screen.blit(game_map, (0, 0))

    # Draw the player as a red circle
    screen.blit(player_sprite, (player_x - 28, player_y - 32))
    screen.blit(non_player_sprite, ((WIDTH // 2) - 28, (HEIGHT // 2) - 218))

    if player_y <= 300 and (WIDTH // 2 - 50) < player_x < (WIDTH // 2 + 50):
        if keys[pygame.K_e] and not SHOW_TEXTBOX:
            SHOW_TEXTBOX = True
            sentence = model.generate_sentences(1, False)

    if SHOW_TEXTBOX:
        draw_text(sentence)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
