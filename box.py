import pygame


class Box:
    def __init__(self, position, velocity, radius, mass, color):
        self.position = position
        self.velocity = velocity
        self.radius = radius / 2
        self.mass = mass
        self.color = color
        self.dampening = 1

    def set_velocity(self, new_velocity):
        self.velocity = new_velocity

    def set_position(self, new_position):
        self.position = new_position

    def get_velocity(self):
        return self.velocity

    def get_position(self):
        return self.position

    def update(self, seconds_passed):
        self.position += self.velocity * seconds_passed
        self.velocity *= self.dampening

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.position.x), int(self.position.y), self.radius * 3, self.radius * 3))
