import math
import time


class ASCIIRenderer:
    # Basic character sets for different purposes
    SHADING_CHARS = " .:-=+*#%@"  # From lightest to darkest
    BOX_CHARS = {
        "horizontal": "─",
        "vertical": "│",
        "top_left": "┌",
        "top_right": "┐",
        "bottom_left": "└",
        "bottom_right": "┘",
    }

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[" " for _ in range(width)] for _ in range(height)]

    def clear(self):
        """Clear the buffer"""
        self.buffer = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def draw_pixel(self, x, y, char="█"):
        """Draw a single character at specified coordinates"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = char

    def draw_line(self, x1, y1, x2, y2, char="█"):
        """Draw a line using Bresenham's algorithm"""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        if dx > dy:
            err = dx / 2.0
            while x != x2:
                self.draw_pixel(x, y, char)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y2:
                self.draw_pixel(x, y, char)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.draw_pixel(x, y, char)

    def draw_box(self, x, y, width, height):
        """Draw a box using box-drawing characters"""
        # Draw corners
        self.draw_pixel(x, y, self.BOX_CHARS["top_left"])
        self.draw_pixel(x + width - 1, y, self.BOX_CHARS["top_right"])
        self.draw_pixel(x, y + height - 1, self.BOX_CHARS["bottom_left"])
        self.draw_pixel(x + width - 1, y + height - 1, self.BOX_CHARS["bottom_right"])

        # Draw edges
        for i in range(1, width - 1):
            self.draw_pixel(x + i, y, self.BOX_CHARS["horizontal"])
            self.draw_pixel(x + i, y + height - 1, self.BOX_CHARS["horizontal"])

        for i in range(1, height - 1):
            self.draw_pixel(x, y + i, self.BOX_CHARS["vertical"])
            self.draw_pixel(x + width - 1, y + i, self.BOX_CHARS["vertical"])

    def draw_circle(self, center_x, center_y, radius):
        """Draw a circle using midpoint circle algorithm"""
        x = radius
        y = 0
        err = 0

        while x >= y:
            self.draw_pixel(center_x + x, center_y + y)
            self.draw_pixel(center_x + y, center_y + x)
            self.draw_pixel(center_x - y, center_y + x)
            self.draw_pixel(center_x - x, center_y + y)
            self.draw_pixel(center_x - x, center_y - y)
            self.draw_pixel(center_x - y, center_y - x)
            self.draw_pixel(center_x + y, center_y - x)
            self.draw_pixel(center_x + x, center_y - y)

            y += 1
            err += 1 + 2 * y
            if 2 * (err - x) + 1 > 0:
                x -= 1
                err += 1 - 2 * x

    def shade_area(self, x1, y1, x2, y2, pattern=None):
        """Fill an area with a shading pattern"""
        if pattern is None:
            pattern = self.SHADING_CHARS[5]  # Medium shade

        for y in range(y1, y2):
            for x in range(x1, x2):
                self.draw_pixel(x, y, pattern)

    def render(self):
        """Render the buffer to string"""
        return "\n".join("".join(row) for row in self.buffer)


# Example usage
def main():
    # Create a renderer with 40x20 characters
    renderer = ASCIIRenderer(40, 20)

    # Draw some example shapes
    renderer.draw_box(5, 2, 30, 15)  # Box
    renderer.draw_circle(20, 10, 5)  # Circle
    renderer.draw_line(10, 5, 30, 15)  # Diagonal line
    renderer.shade_area(7, 4, 15, 8, "░")  # Shaded area

    # Print the result
    print(renderer.render())


if __name__ == "__main__":
    main()
