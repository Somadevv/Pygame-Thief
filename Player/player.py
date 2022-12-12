import pygame
import Helpers.drawText
drawText = Helpers.drawText.DrawText


class Player():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, surface):
        self.rect = pygame.Rect(0, 0, 20, 40)
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .5, -.10
        self.position, self.velocity = pygame.math.Vector2(
            0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        self.gold = 5000
        self.surface = surface

    def add_gold(self, amount):
        self.gold += amount

    def remove_gold(self, amount):
        print("amount", amount)
        # self.render_gold()
        self.gold -= amount
        print("Gold", self.gold)

    def reset_gold(self):
        self.gold = 0

    def render_gold(self):
        coinWidth = 20
        coinHeight = 20
        textSize = 16
        textColor = (255, 255, 255)
        coinXpos = 5
        coinYPos = 5
        coinIcon = pygame.image.load(
            "Assets/Images/Icons/coin.png").convert_alpha()
        coinImage = pygame.transform.scale(
            coinIcon, (coinWidth, coinHeight))

        self.surface.blit(coinImage, (coinXpos, coinYPos))
        drawText(self.surface, str(self.gold), textSize, textColor,
                 38, 17.75)

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

    def initialize(self, dt):
        self.render_gold()
        self.update(dt)
