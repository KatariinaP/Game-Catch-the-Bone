import pygame
from gameAttributes import Dog, Collectable, Enemy

#define global variables
pygame.init()
display = pygame.display.set_mode((640, 480))
clock  = pygame.time.Clock()
pygame.display.set_caption("Catch the bone!")

#variables for in game-counter 
counter = 10
timer_event = pygame.USEREVENT
pygame.time.set_timer(timer_event, 500)
 
    #the game function
def game():

    #establish the player, collectable and enemies
    player = Dog()
    collectables = Collectable()
    ufo_moving = Enemy()
    ufo_following = Enemy()
    ufo_random = Enemy()

    #main game loop
    while True:

        #draw background, the player, collectable and enemies on display
        display.fill((0, 250, 250))
        collectables.draw_bone()
        ufo_moving.draw_enemy()
        ufo_following.draw_enemy()
        ufo_random.draw_enemy()
        player.draw_dog()

        #call functions to move player and the moving ufo
        player.move_dog()
        ufo_moving.enemy_move_in_circles()

        #the point counter text, could be put in a class but that would be unnecessarily complicated
        font = pygame.font.SysFont("consolas", 25)
        text = font.render(f"Player points: {str(player.points)}", True, (150, 50, 0))
        display.blit(text, (400, 30))

        for event in pygame.event.get():
            #in game counter, bone and ufo changes locations every 10 sec if the player does not hit them
            if event.type == timer_event:
                global counter
                counter -= 1
                if counter == 0 or player.hit == 1:
                    collectables.random_spawn()
                    ufo_random.random_spawn_enemy()
                    counter = 10
                    player.hit = False   

            #movement of the player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left = True
                if event.key == pygame.K_RIGHT:
                    player.go_rigth = True
                if event.key == pygame.K_UP:
                    player.go_up = True
                if event.key == pygame.K_DOWN:
                    player.go_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.go_left = False
                if event.key == pygame.K_RIGHT:
                    player.go_rigth = False
                if event.key == pygame.K_UP:
                    player.go_up = False
                if event.key == pygame.K_DOWN:
                    player.go_down = False

            # makes the enemy object to follow player
            if ufo_following.rect.x > player.rect.x:
                ufo_following.rect.x -= 10
            if ufo_following.rect.x < player.rect.x:
                ufo_following.rect.x += 10
            if ufo_following.rect.y > player.rect.y:
                ufo_following.rect.y -= 10
            if ufo_following.rect.y < player.rect.y:
                ufo_following.rect.y += 10

            #check collisions 
            player.checkInteraction(collectables.rect)
            player.checkInteraction_enemy(ufo_moving.rect)
            player.checkInteraction_enemy(ufo_following.rect)
            player.checkInteraction_enemy(ufo_random.rect)

            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()
        clock.tick(60)
game()