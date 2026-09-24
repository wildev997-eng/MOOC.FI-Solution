import pygame
from random import randint, random

class Invader:
    def __init__(self):
        pygame.init()
        self.load_images()
        self.x = 0
        self.y = 0
        self.window = pygame.display.set_mode((640, 480))
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.game_over_font = pygame.font.SysFont("Arial", 48)
        self.coin = []
        self.monster = []
        self.clock = pygame.time.Clock()
        self.main_loop()

    def load_images(self):
        self.images = {}
        for name in ["coin", "robot", "monster"]:
            image = pygame.image.load(f"{name}.png")
            self.images[name] = {
                "image": image,
                "width": image.get_width(),
                "height": image.get_height()
            }


    def main_loop(self):
        velocity = 1
        spawn_chance = 0.01
        score = 0
        life = 5
        game_over = False
        finished = False

        while True:
            self.check_events()

            if game_over:
                self.draw_game_over(score)
                self.clock.tick(60)
                continue
            
            if finished:
                self.draw_finished(score)
                self.clock.tick(60)
                continue

            rect_robot = self.images["robot"]["image"].get_rect(topleft=(self.x, 480 - self.images["robot"]["height"]))

            if random() < spawn_chance:
                new_x = randint(1, 640 - self.images["coin"]["width"])
                
                too_close = any(
                    abs(new_x - bot["x"]) < self.images["coin"]["width"]
                    for bot in self.coin + self.monster
                    if bot["state"] == "falling"
                )
                
                if not too_close:
                    self.coin.append({"x": new_x, "y": -100, "state": "falling"})

            if random() < spawn_chance:
                new_x = randint(1, 640 - self.images["monster"]["width"])
                
                too_close = any(
                    abs(new_x - bot["x"]) < self.images["monster"]["width"]
                    for bot in self.coin + self.monster
                    if bot["state"] == "falling"
                )
                
                if not too_close:
                    self.monster.append({"x": new_x, "y": -100, "state": "falling"})

            for bot in self.coin:
                if bot["state"] == "falling":
                    bot["y"] += velocity
                    if bot["y"] + self.images["coin"]["height"] >= 480:
                        score = 0
                        self.coin = []
                        break

                rect_coin = self.images["coin"]["image"].get_rect(topleft=(bot["x"], bot["y"]))
                if rect_coin.colliderect(rect_robot):
                    score += 1
                    bot["state"] = "hit"

            for bot in self.monster:
                if bot["state"] == "falling":
                    bot["y"] += velocity
                    if bot["y"] + self.images["monster"]["height"] >= 480:
                        bot["state"] = "hit"

                rect_monster = self.images["monster"]["image"].get_rect(topleft=(bot["x"], bot["y"]))
                if rect_monster.colliderect(rect_robot):
                    life -= 1
                    bot["state"] = "hit"
            
            if score == 20:
                finished = True
            
            if life == 0:
                game_over = True

            self.coin = [bot for bot in self.coin if bot["state"] != "hit"]
            self.monster = [bot for bot in self.monster if bot["state"] != "hit"]

            text = self.game_font.render(f"Points: {score}", True, (255, 0, 0))
            text_life = self.game_font.render(f"heart: {life}", True, (255, 0, 0))
            text_objt = self.game_font.render("Reach 20 score!", True, (255, 0, 0))

            self.window.fill((255, 255, 255))
            for bot in self.coin:
                self.window.blit(self.images["coin"]["image"], (bot["x"], bot["y"]))
            for bot in self.monster:
                self.window.blit(self.images["monster"]["image"], (bot["x"], bot["y"]))
            self.window.blit(self.images["robot"]["image"], (self.x, 480 - self.images["robot"]["height"]))
            self.window.blit(text, (500, 0))
            self.window.blit(text_objt, (0, 0))
            self.window.blit(text_life , (200,0))
            pygame.display.flip()

            self.clock.tick(60)

    def draw_game_over(self, score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
                    Invader()
            self.window.fill((0, 0, 0))
            text = self.game_over_font.render("GAME OVER", True, (255, 0, 0))
            score_text = self.game_font.render(f"Final score: {score}", True, (255, 255, 255))
            cont = self.game_font.render("Press F12 to continue", True, (255, 255, 255))
            self.window.blit(text, (640 // 2 - text.get_width() // 2, 200))
            self.window.blit(score_text, (640 // 2 - score_text.get_width() // 2, 260))
            self.window.blit(cont, (640 // 2 - cont.get_width() // 2, 360))
            pygame.display.flip()
    
    def draw_finished(self, score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
                    Invader()
            self.window.fill((0, 0, 0))
            text = self.game_over_font.render("FINISHED", True, (255, 0, 0))
            score_text = self.game_font.render(f"Final score: {score}", True, (255, 255, 255))
            cont = self.game_font.render("Press F12 to play again", True, (255, 255, 255))
            self.window.blit(text, (640 // 2 - text.get_width() // 2, 200))
            self.window.blit(score_text, (640 // 2 - score_text.get_width() // 2, 260))
            self.window.blit(cont, (640 // 2 - cont.get_width() // 2, 360))
            pygame.display.flip()


    def check_events(self):
        to_right = False
        to_left = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True

        if to_right and self.x + self.images["robot"]["width"] < 640:
            self.x += 45
        if to_left and self.x > 0:
            self.x -= 45


if __name__ == "__main__":
    Invader()