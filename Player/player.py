import pygame


class Player():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 40)
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .5, -.10
        self.position, self.velocity = pygame.math.Vector2(
            0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)

    def draw(self, display):
        pygame.draw.rect(display, (255, 0, 0), self.rect)

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)

    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .8
        elif self.RIGHT_KEY:
            self.acceleration.x += .8
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(20)
        self.position.x += self.velocity.x * dt + \
            (self.acceleration.x * .3) * (dt * dt)
        self.rect.x = self.position.x

    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 8:
            self.velocity.y = 8
        self.position.y += self.velocity.y * dt + \
            (self.acceleration.y * .10) * (dt * dt)

        # Constraint to Y > Alter for collision
        if self.position.y > 250:
            self.on_ground = True
            self.velocity.y = 0
            self.position.y = 250
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01:
            self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False
