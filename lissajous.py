import math

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (89,203,232)

class Lissajous:
    def __init__(self, side, num_of_curves, base_angle, thickness):
        self.side = side
        self.num_of_curves = num_of_curves
        self.radius = side / (2 * (num_of_curves+2))
        self.spacing = self.radius / num_of_curves

        self.thickness = thickness

        self.angles = [0 for _ in range(num_of_curves)]
        self.angles_vel = [(i+1) * base_angle for i in range(num_of_curves)]

        self.points = []

    def update(self):
        for i in range(self.num_of_curves):
            self.angles[i] += self.angles_vel[i]

    def render_points(self, pygame, screen):
        for point in self.points:
            pygame.draw.circle(screen, WHITE, point, self.thickness)

        if len(self.points) > 500:
            self.points.pop(0)

    def render_circles(self, pygame, screen):
        for i in range(self.num_of_curves):
            x = 2 * self.radius * (i + 1) + self.radius + (i+1) * self.spacing
            y = self.radius + self.spacing

            pygame.draw.circle(screen, RED, (x, y), self.radius, width=self.thickness)
            pygame.draw.circle(screen, RED, (y, x), self.radius, width=self.thickness)

    def render_points_lines(self, pygame, screen):
        for i in range(self.num_of_curves):
            x = 2 * self.radius * (i + 1) + self.radius + (i+1) * self.spacing
            y = self.radius + self.spacing
            x_to_point = self.radius * math.cos(self.angles[i])
            y_to_point = self.radius * math.sin(self.angles[i])

            pygame.draw.circle(screen, GREEN, (x + x_to_point, y + y_to_point), self.thickness+2)
            pygame.draw.line(screen, WHITE, (0, x + y_to_point), (self.side, x + y_to_point), self.thickness)

            pygame.draw.circle(screen, GREEN, (y + x_to_point, x + y_to_point), self.thickness+2)
            pygame.draw.line(screen, WHITE, (x + x_to_point, 0), (x + x_to_point, self.side), self.thickness)

            for j in range(self.num_of_curves):
                x_intersect = 2 * self.radius * (j + 1) + self.radius + self.radius * math.cos(self.angles[j]) + (j+1) * self.spacing
                y_intersect = 2 * self.radius * (i + 1) + self.radius + self.radius * math.sin(self.angles[i]) + (i+1) * self.spacing

                pygame.draw.circle(screen, BLUE, (x_intersect, y_intersect), self.thickness+3)
                self.points.append((x_intersect, y_intersect))

    def render(self, pygame, screen):
        # render the circles
        self.render_circles(pygame, screen)

        # render the points on the circle and lines
        self.render_points_lines(pygame, screen)

        # render stored points
        self.render_points(pygame, screen)






            
    