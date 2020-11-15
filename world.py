import collision


class World:
    def __init__(self, screen_length, screen_width):
        self.things = {}
        self.thing_index = 0
        self.screen_length = screen_length
        self.screen_width = screen_width
        self.background_color = (0, 0, 0)

    def add_ball(self, ball):
        self.things[self.thing_index] = ball
        self.thing_index += 1

    def check_for_collision(self):
        for i in range(self.thing_index):
            b1 = self.things[i]

            for j in range(i):
                b2 = self.things[j]

                if collision.peer_contact(b1, b2):
                    collision.peer_collision(b1, b2)

            collision.manage_wall_contact(b1)

    def update(self, time_passed):
        for key in self.things.keys():
            self.things[key].update(time_passed)

        self.check_for_collision()

    def render(self, screen):
        screen.fill(self.background_color)

        for key in self.things.keys():
            self.things[key].render(screen)
