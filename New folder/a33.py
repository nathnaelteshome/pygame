import pygame

def main():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the canvas
    canvas_width = 500
    canvas_height = 400

    # Create the canvas
    canvas = pygame.display.set_mode((canvas_width, canvas_height))

    # Set the title of the canvas
    pygame.display.set_caption("Ethiopian Flag")

    # Ethiopian flag colors
    green = (0, 128, 0)
    yellow = (255, 255, 0)
    red = (178, 34, 34)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            # Check if the 'SPACE' key is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
            # Check if the 'QUIT' event is triggered
            elif event.type == pygame.QUIT:
                running = False

        # Fill the canvas with white color
        canvas.fill((255, 255, 255))

        # Draw the Ethiopian flag
        # Draw the green rectangle
        pygame.draw.rect(canvas, green, (50, 50, 400, 133))
        # Draw the yellow rectangle
        pygame.draw.rect(canvas, yellow, (50, 183, 400, 133))
        # Draw the red rectangle
        pygame.draw.rect(canvas, red, (50, 316, 400, 133))

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

# Call the main function
main()
