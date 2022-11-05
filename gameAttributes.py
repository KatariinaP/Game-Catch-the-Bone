import random
import math
import pygame

display = pygame.display.set_mode((640, 480))

class Interaction():
    """ Interactions class to check for collisions and point count """

    def __init__(self):
        self.__positionDog = pygame.Rect(50, 50, 0, 0)
        self.__points = 0
        self.__hit = False

    # For a small game like this, to keep the code simple it is maybe not so necessary
    # to encapsulate the attributes and access them using getters and setters.
    # BUT for the sake of learning good programming conventions it is done like this here.

    # Getter and setter to check hit
    @property
    def hit(self):
        return self.__hit

    @hit.setter
    def hit(self, hit):
        self.__hit = hit

    # Getter and setter to get the position of the dog
    @property
    def positionDog(self):
        return self.__positionDog

    @positionDog.setter
    def positionDog(self, positionDog):
        self.__positionDog = positionDog

    # Getter and setter to get the points
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points
        

    # checks collision between dog and collectable, and adds points
    def checkInteraction(self, other: pygame.Rect):
        if self.positionDog.colliderect(other) and not self.hit:
            self.points += 1
            self.hit = True

    # checks collision between dog and enemies, and reduces points
    def checkInteraction_enemy(self, other: pygame.Rect):
        if self.positionDog.colliderect(other) and not self.hit and self.points > 0:
            self.points -= 1
            self.hit = True


class Dog(Interaction):
    """ Dog defines the player attributes and methods. Inherits Interaction class. """

    def __init__(self):
        super().__init__()
        self.dog = pygame.image.load("images/dog.png")
        self.__rect = self.dog.get_rect()
        self.__rect.x = 300
        self.__rect.y = 240
        self.__go_rigth = False
        self.__go_left = False
        self.__go_up = False
        self.__go_down = False

    # Getter and setter to get the position of the dog
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    # Getters and setters for the movement of the dog
    @property
    def go_rigth(self):
        return self.__go_rigth

    @go_rigth.setter
    def go_rigth(self, go_rigth):
        self.__go_rigth = go_rigth

    @property
    def go_left(self):
        return self.__go_left

    @go_left.setter
    def go_left(self, go_left):
        self.__go_left = go_left

    @property
    def go_up(self):
        return self.__go_up

    @go_up.setter
    def go_up(self, go_up):
        self.__go_up = go_up

    @property
    def go_down(self):
        return self.__go_down

    @go_down.setter
    def go_down(self, go_down):
        self.__go_down = go_down

    #method to show dog in the display
    def draw_dog(self):
       display.blit(self.dog, self.rect)

    #method to move the dog within the display frame
    def move_dog(self):
        if self.go_rigth and self.rect.x + self.dog.get_width() < 640: 
            self.rect.x += 3
        if self.go_left and self.rect.x > 0:
            self.rect.x -= 3
        if self.go_up and self.rect.y > 0:
            self.rect.y -= 3
        if self.go_down and self.rect.y + self.dog.get_height() < 480:
            self.rect.y += 3      
        
        self.positionDog =  self.rect 

class Collectable(Interaction):
    """ Collectable defines the attributes and methods of the collectable bone. Inherits Interactions class. """

    def __init__(self):
        super().__init__()
        self.bone = pygame.image.load("images/dog-treat.png")
        self.__rect = self.bone.get_rect()
        self.__rect.x = 600
        self.__rect.y = 450

    # Getter and setter to get the position of the bone
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    def draw_bone(self):
        display.blit( self.bone, self.rect)

    #method to appear into random locations on the display
    def random_spawn(self):
        self.rect.x = random.randint(0,640 - self.bone.get_width())
        self.rect.y = random.randint(0,480 - self.bone.get_height())

class Enemy(Interaction):
    """ Enemies defines the attributes and methods of the enemies to avoid. Inherits Interactions class. """

    def __init__(self):
        super().__init__()
        self.angle = 0   #variable to determine angle for circulating objects
        self.enemy = pygame.image.load("images/ufo.png")
        self.__rect = self.enemy.get_rect()
        self.__rect.x = 100
        self.__rect.y = 100

    # Getter and setter to get the position of the enemy
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    #displays the object on display
    def draw_enemy(self):
        display.blit( self.enemy, self.rect)

    #moves the enemy in a circular motion
    def enemy_move_in_circles(self):
        self.angle
        self.rect.x = 290+math.cos(self.angle)*200
        self.rect.y = 220+math.sin(self.angle)*200
        self.angle += 0.03

    #method to appear into random locations on the display
    def random_spawn_enemy(self):
        self.rect.x = random.randint(0,640 - self.enemy.get_width())
        self.rect.y = random.randint(0,480 - self.enemy.get_height())