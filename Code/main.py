import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

### Highest Score
points = 0 
highest_point = 0  
# Create Font Object
font = pygame.font.Font(None,36)

RUNNING = [pygame.image.load(os.path.join("Assets/Cat", "CatRun1.png")),
           pygame.image.load(os.path.join("Assets/Cat", "CatRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Cat", "CatJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Cat", "CatDuck1.png")),
           pygame.image.load(os.path.join("Assets/Cat", "CatDuck2.png"))]
# Add IMG
DEAD = [pygame.image.load(os.path.join("Assets/Cat", "CatDead.png"))]

END = [pygame.image.load(os.path.join("Assets/Cat", "CatEnd.png"))]
START = [pygame.image.load(os.path.join("Assets/Cat", "CatStart.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

# Add DOG obstacle IMG 4
DOG = [pygame.image.load(os.path.join("Assets/Dog", "DogRun1.png")),
       pygame.image.load(os.path.join("Assets/Dog", "DogRun2.png"))]

# Add BANANA obstacle IMG 3
BANANA = [pygame.image.load(os.path.join("Assets/Banana", "Banana1.png")),
          pygame.image.load(os.path.join("Assets/Banana", "Banana2.png")),
          pygame.image.load(os.path.join("Assets/Banana", "Banana3.png"))]
# Add CHASER IMG 2
CHASER =[pygame.image.load(os.path.join("Assets/Chaser", "Chaser1.png")),
         pygame.image.load(os.path.join("Assets/Chaser", "Chaser2.png"))]

# Add Churu Item IMG 2
CHURU = [pygame.image.load(os.path.join("Assets/Churu", "Churu1.png")),
           pygame.image.load(os.path.join("Assets/Churu", "Churu2.png"))]
# Add Star IMG 1
STAR = pygame.image.load(os.path.join("Assets/Other", "Star.png"))

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

# Add Item Churu
class Churu:
    def __init__(self):
        self.image = CHURU
        self.index = 0
        self.x = 80
        self.y = 430     # NEED TO CHANGE
        self.last_update = pygame.time.get_ticks()  # Add this line
        self.animation_interval = 150  # Add this line (500ms)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_interval:  # Check if it's time to update
            self.index = (self.index + 1) % 2  # Update index to be 0 or 1
            self.last_update = now  # Update the last update time

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.index], (self.x, self.y))  

        # # Draw Star When it Used 
        # if self.churu_active:
        #     SCREEN.blit(STAR, (10, SCREEN_HEIGHT - STAR.get_height() - 10))
# # Add Star IMG
# class Star():
#     def __init__(self, image):
#         self.type = 0
#         super().__init__(image, self.type)
#         self.x = 80
#         self.y = 50

class Cat:
    X_POS = 80
    Y_POS = 300
    Y_POS_DUCK = 330
    JUMP_VEL = 8.5

    def __init__(self):
        # Add init statement
        self.invincible = False 

        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        # Add Star IMG
        self.star_img = STAR

        self.Cat_duck = False
        self.Cat_run = True
        self.Cat_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.Cat_rect = self.image.get_rect()
        self.Cat_rect.x = self.X_POS
        self.Cat_rect.y = self.Y_POS

    def update(self, userInput):
        if self.Cat_duck:
            self.duck()
        if self.Cat_run:
            self.run()
        if self.Cat_jump:
            self.jump()
        if self.invincible:
            self.star()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.Cat_jump:
            self.Cat_duck = False
            self.Cat_run = False
            self.Cat_jump = True
            ### Add to Get star() if invinsible is True
            if self.invincible == True:
                self.invincible = True
        elif userInput[pygame.K_DOWN] and not self.Cat_jump:
            self.Cat_duck = True
            self.Cat_run = False
            self.Cat_jump = False
            ### Add to Get star() if invinsible is True
            if self.invincible == True:
                self.invincible = True
        elif not (self.Cat_jump or userInput[pygame.K_DOWN]):
            self.Cat_duck = False
            self.Cat_run = True
            self.Cat_jump = False
            ### Add to Get star() if invinsible is True
            if self.invincible == True:
                self.invincible = True

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.Cat_rect = self.image.get_rect()
        self.Cat_rect.x = self.X_POS
        self.Cat_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.Cat_rect = self.image.get_rect()
        self.Cat_rect.x = self.X_POS
        self.Cat_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.Cat_jump:
            self.Cat_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.Cat_jump = False
            self.jump_vel = self.JUMP_VEL

    def star(self, SCREEN):
        self.image = self.star_img
        self.x = 80
        self.y = 50

        if self.Cat_jump:
            self.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        # if self.jump_vel < - self.JUMP_VEL:
        #     self.Cat_jump = False
        #     self.jump_vel = self.JUMP_VEL
        if self.Cat_duck:
            self.y = self.Y_POS_DUCK
        
        # Draw on SCREEN
        SCREEN.blit(self.image, (self.x, self.y))


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.Cat_rect.x, self.Cat_rect.y))

    
# Add Chaser
class Chaser:
    def __init__(self):
        self.image = CHASER
        self.index = 0
        self.x = -20
        self.y = 230
        self.last_update = pygame.time.get_ticks()  # Add this line
        self.animation_interval = 150  # Add this line (500ms)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_interval:  # Check if it's time to update
            self.index = (self.index + 1) % 2  # Update index to be 0 or 1
            self.last_update = now  # Update the last update time


    def draw(self, SCREEN):
        # Use self.index to select image ANIMATION
        SCREEN.blit(self.image[self.index], (self.x, self.y))  

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

# Add Obstacle Dog
class Dog(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 330
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
# Add Obstacle Banana
class Banana(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 350

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, highest_point, churu_score, highest_point_save
    run = True
    clock = pygame.time.Clock()
    player = Cat()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    # Save Hightes Points
    higehst_point_save = 0

    # Chaser System
    chaser = Chaser()
    chaser_start_time = None
    chaser_hit_count = 0
    chaser_active = False

    # Churu System
    churu = Churu()
    churu_value = 0
    churu_start_time = None
    churu_score = 500

    # Add Churu score higher when it go Faster
    # if (game_speed % 1000) - 1 == 0:
    #     churu_score += 500
    ################ IT DOESN'T WROK?!################


    def score():
        global points, game_speed, highest_point, churu_score
        points += 1
        if points % 100 == 0:
            game_speed += 1

        # Update HIGHTEST pts
        if points > highest_point:
            highest_point = points
            
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT:
                # Invincible Statement False
                player.invincible = False 

        userInput = pygame.key.get_pressed()

        # Press Q or ENTER to end
        if userInput[pygame.K_q] or userInput[pygame.K_RETURN]:
            pygame.quit()
            quit()

        SCREEN.fill((255, 255, 255))    # This line Location important
            
        # Draw Churu on SCREEN
        if churu_value == 2:
            churu.draw(SCREEN)
            churu.update()
    
        ## Give Churu when pts get 500 (100 in test)
        # Make it not work when points == 0
        # Make player get only 1 churu in item
        if points % churu_score == 0 and points != 0:
            churu_value = 2
        
        ## Press C to use Item
        if userInput[pygame.K_c] and churu_value > 0:
            churu_start_time = pygame.time.get_ticks()
            player.invincible = True
            churu_value = 1

        # Churu Timer
        if churu_start_time is not None and pygame.time.get_ticks() - churu_start_time > 3000:  # 3 secs timer
            player.invincible = False
            churu_start_time = None
            churu_value = 0

        player.draw(SCREEN)
        player.update(userInput)
        
        # Render 'Highest Points:' Text
        highest_point_text = font.render("Highest Points: " + str(higehst_point_save), True, (125, 125, 125))
        SCREEN.blit(highest_point_text, (873, 55))  # Location

        if len(obstacles) == 0:
            obstacle_type = random.randint(0, 4)  
            if obstacle_type == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_type == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_type == 2:
                obstacles.append(Bird(BIRD))
            elif obstacle_type == 3:
                obstacles.append(Dog(DOG))
            elif obstacle_type == 4:
                obstacles.append(Banana(BANANA))

        for obstacle in obstacles:
            
            obstacle.draw(SCREEN)
            obstacle.update()

            if player.Cat_rect.colliderect(obstacle.rect):
                
                if player.invincible == True:
                    continue
                
                if isinstance(obstacle, Dog):  # Check if the obstacle is a Dog
                    points -= 200  # Lose 100 pts
                    highest_point -= 200
                    obstacles.remove(obstacle)  # Remove the dog after

                if isinstance(obstacle, Banana):
                    chaser_hit_count += 1
                    obstacles.remove(obstacle)  # Remove the Banana after
                    
                    chaser_active = True
                    if chaser_start_time is None:
                        chaser_start_time = pygame.time.get_ticks()

                else:
                    pygame.time.delay(800)
                    death_count += 1
                    menu(death_count)

        if chaser_active:
            chaser.update()
            chaser.draw(SCREEN)

            if pygame.time.get_ticks() - chaser_start_time > 5000:
                chaser_active = False
                chaser_start_time = None
                chaser_hit_count = 0

            if chaser_hit_count == 2:
                pygame.time.delay(800)
                death_count += 1
                highest_point = highest_point_save
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            # Add START IMG
            SCREEN.blit(START[0], (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 160))
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            # Add END IMG
            SCREEN.blit(END[0], (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 230))
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            # Render 'Highest Points:' Text
            highest_point_text = font.render("Highest Points: " + str(highest_point), True, (125, 125, 125))
            SCREEN.blit(highest_point_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 80))  # Set Location
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)