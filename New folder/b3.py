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
    pygame.display.set_caption("My Canvas")

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            # Check if the 'A' key is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                running = False
            # Check if the 'QUIT' event is triggered
            elif event.type == pygame.QUIT:
                running = False

        # Fill the canvas with white color
        canvas.fill((255, 255, 255))

        # Draw a red line
        start_pos = (50, 50)
        end_pos = (50, 250)
        line_width = 3
        line_color = (255, 0, 0)
        pygame.draw.line(canvas, line_color, start_pos, end_pos, line_width)

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

# Call the main function
main()
