import pygame, random

#Intialize pygame
pygame.init()

#Set Display Surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        #Set game values
        self.round_number = 1
        self.score = 0
        # TODO: set the player to self.player
        # TODO: repeat for alien_group, player_bullet_group, alien_bullet_group.  set all to a self. version.

        #Set sounds and music
        self.new_round_sound = pygame.mixer.Sound("./assets/audio/new_round.wav")
        #TODO: repeat for breach_sound (using self) breach.wav
        #TODO: (cont.) alien_hit_sound to alien_hit.wav
        #TODO: (cont.) player_hit_sound to player_hit.wav

        #Set font
        self.font = pygame.font.Font("./assets/fonts/Facon.ttf", 32)

    def update(self):
        """Update the game"""
        ... #TODO: we will do this one later.

    def draw(self):
        """Draw the HUD and other information to display"""
        ... #TODO: we will do this one later.

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""
        ... #TODO: we will do this one later.

    def check_collision(self):
        """Check for collisions"""
        ... #TODO: we will do this one later.

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        ... #TODO: we will do this one later.

    def start_new_round(self):
        """Start a new round"""
        ... #TODO: we will do this one later.

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        ... #TODO: we will do this one later.

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        ... #TODO: we will do this one later.

    def reset_game(self):
        """Reset the game"""
        ... #TODO: we will do this one later.


class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        ... #TODO: we will finish later

    def update(self):
        """Update the player"""
        ... #TODO: we will finish later

    def fire(self):
        """Fire a bullet"""
        ... #TODO: we will finish later

    def reset(self):
        """Reset the players position"""
        ... #TODO: we will finish later


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        #TODO: (3/11/25) assign to self.image and image loaded from alien.png
        #TODO: (3/11/25) assign self.rect

    def update(self):
        """Update the alien"""
       #TODO: add to self.rect.x the value of direction * Veolcity (Dont Forget Self)

    #randomly fire bullet
    if random.randint(0,100) > 999 and len(self.bullet_group) < 3:
        self.shoot_sound.play()
        self.fire()

    def fire(self):
        """Fire a bullet"""
        ... #TODO: we will do this later.

    def reset(self):
        """Reset the alien position"""
        ... #TODO: we will do this later.


class PlayerBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("./assets/image/red_laser.png")
        self.rect = self.image.get_rect()
        # TODO (3/11/25) assign x to self.rect.centerx
        # TODO (3/11/25) do the same for centery

        # TODO (3/11/25) assign 10 to self.velocity
        # TODO (3/11/25) Call bullet_group's add method and pass in self


    def update(self):
        """Update the bullet"""
        # TODO: (3/11/25) subtract self.velocity from self.rect.y:
        # TODO (3/11/25) check if self.rect.bottom is less than 0
        # TODO (3/11/25) the if blovk will then kill the sprite


class AlienBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("./assets/image/red_laser.png")
        self.rect = self.image.get_rect()
         #TODO (3/11/25) assign x to self.rect.centerx
        #TODO (3/11/25) do the same for centery

        #TODO (3/11/25) assign 10 to self.velocity
        #TODO (3/11/25) Call bullet_group's add method and pass in self

    def update(self):
        """Update the bullet"""
       #TODO: ( 3/11/25 ) add to self.velocity


#Create bullet groups
my_player_bullet_group = pygame.sprite.Group()
#TODO: repeat for my_alien_bullet_group

#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

#Create an alien group.  Will add Alien objects via the game's start new round method
#TODO: create my_alien_group

#Create the Game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
my_game.start_new_round()

#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #The player wants to fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()

    # Fill the display
    display_surface.fill((0, 0, 0))

    #Update and display all sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    #Update and draw Game object
    my_game.update()
    my_game.draw()

    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()