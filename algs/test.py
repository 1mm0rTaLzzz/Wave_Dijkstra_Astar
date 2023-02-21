import pygame

# Initialize Pygame
pygame.init()

# Define the screen dimensions
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the buttons
button_width = 100
button_height = 50
button1_pos = (50, 150)
button2_pos = (250, 150)
button_color = (0, 255, 0)  # Green color

# Main loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the buttons
    pygame.draw.rect(screen, button_color, (button1_pos[0], button1_pos[1], button_width, button_height))
    pygame.draw.rect(screen, button_color, (button2_pos[0], button2_pos[1], button_width, button_height))

    # Check if a button is clicked
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
        if button1_pos[0] < mouse_pos[0] < button1_pos[0] + button_width and button1_pos[1] < mouse_pos[1] < button1_pos[1] + button_height:
            print("Button 1 is clicked!")
        elif button2_pos[0] < mouse_pos[0] < button2_pos[0] + button_width and button2_pos[1] < mouse_pos[1] < button2_pos[1] + button_height:
            print("Button 2 is clicked!")

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
