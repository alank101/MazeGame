class GameCharacter:

    speed = 1.0

    def __init__ (self, name, health, x_pos, y_pos):
        self.name = name
        self.health = health
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move(self, by_x_amount=0, by_y_amount=0):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0: self.health = 0
    
    def check_is_dead(self):
        return self.health <= 0

blob = GameCharacter('Blob', 10, 50, 0)
wolf = GameCharacter('Wolf', 15, 75, 0)
goo = GameCharacter('Goo', 20, 100, 0)
mastermind = GameCharacter('Mastermind', 50, 150, 0)

class PlayerCharacter(GameCharacter):
    def __init__(self, name, health, num_lives, x_pos, y_pos):
        super().__init__(name, health, x_pos, y_pos)
        self.num_lives = num_lives
        self.max_health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.num_lives -= 1
        self.check_is_dead()

    def check_is_dead(self):
        if self.health <= 0 and self.num_lives <= 0:
            print("Game Over!")
        elif self.health <= 0 and self.num_lives > 0:
            print(f'Lives left: {self.num_lives}')
            self.health = self.max_health
        else:
            print(f'Remaining health: {self.health} and Remaining lives: {self.num_lives}')

pc = PlayerCharacter("Alan", 100, 3, 0, 0)


