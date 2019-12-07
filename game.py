# Brickbreaker as designed by Alex Poley (awp5ud) and Anusha Choudhary (ac7ncw)

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 400)
walls = []
sides = [
    gamebox.from_color(-170, 400, "blue", 400, 800),
    gamebox.from_color(400, 0, "blue", 800, 50),
    gamebox.from_color(970, 400, "blue", 400, 800),
]
ball = gamebox.from_color(400, 300, "orange", 10, 10)
platform = gamebox.from_color(400, 350, "blue", 200, 20)
start_movement = False
start = False
lost = False
screen = 0
counter = 0
lives = 3
health = 100
health_x = 620
health_color = "green"
health_bar = gamebox.from_color(health_x, 15, health_color, health, 10)
start_movement = False

ball_velocity = -3
ball.xspeed = ball_velocity
ball.yspeed = ball_velocity

camera.clear("black")
name_text = gamebox.from_text(400, 200, "Enter your name in the run window.", 50, "blue")
camera.draw(name_text)
camera.display()
name = ""
while name == "":
    name = input("What is your name? ")


def tick(keys):
    global start, screen, counter, start_movement, lives, health, health_x, health_color, lost, start_movement
    high_score = 0
    if counter // 30 > high_score:
        high_score = counter // 30
    camera.clear("black")
    for l in sides:
        camera.draw(l)
    if pygame.K_SPACE in keys:
        start = True
    if pygame.K_0 in keys:
        start = False
        screen = 0
        # Set ball stats temporarily to 0, allowing them to be reset later
    if pygame.K_1 in keys:
        start = False
        screen = 1
    if pygame.K_2 in keys:
        screen = 2

    if start is False and lost:
        camera.clear("black")
        game_over = gamebox.from_text(400, 200, "GAME OVER: PRESS SPACEBAR TO RESTART, 0 to EXIT", 30, "RED")
        camera.draw(game_over)
        if pygame.K_0 in keys:
            screen = 4
            lost = False
            health = 100
            health_x = 620
            health_color = "green"

    if start is False and (screen == 0 or screen == 4) and lost is False:
        welcome = gamebox.from_text(400, 60, (name + ", welcome to..."), 35, "orange")
        title = gamebox.from_text(400, 110, "Break the Rock", 75, "orange")
        authors = gamebox.from_text(400, 175, "By Alex Poley (awp5ud) and Anusha Choudhary (ac7ncw)", 35, "orange")
        start_bar = gamebox.from_color(200, 300, "orange", 200, 30)
        start_bar_text = gamebox.from_text(200, 300, "Press SPACE to start", 25, "blue")
        rules_bar = gamebox.from_color(600, 275, "orange", 220, 30)
        rules_bar_text = gamebox.from_text(600, 275, "Press 1 for rules and info", 25, "blue")
        high_score_bar = gamebox.from_color(600, 325, "orange", 220, 30)
        high_score_bar_text = gamebox.from_text(600, 325, "Press 2 for high scores", 25, "blue")

        camera.draw(welcome)
        camera.draw(title)
        camera.draw(authors)
        camera.draw(start_bar)
        camera.draw(start_bar_text)
        camera.draw(rules_bar)
        camera.draw(rules_bar_text)
        camera.draw(high_score_bar)
        camera.draw(high_score_bar_text)

    elif start is False and screen == 1:
        home1 = gamebox.from_text(90, 13, "Press 0 to return home.", 22, "orange")
        desc = gamebox.from_text(400, 40, "Background", 35, "orange")
        desc1 = gamebox.from_text(400, 70, "This game is based off of Brickbreaker, with a UVA football twist.", 25, "orange")
        desc2 = gamebox.from_text(400, 100, "When UVA prepares for a game, they have a patio paver with the opposing team logo.", 25, "orange")
        desc3 = gamebox.from_text(400, 130, "If UVA football wins the game, a player smashes the rock with a sledgehammer.", 25, "orange")
        desc4 = gamebox.from_text(400, 160, "Help UVA on its road to the ACC Championship!", 25, "orange")
        rules = gamebox.from_text(400, 200, "Rules and Objectives", 35, "orange")
        rules1 = gamebox.from_text(400, 230, "1.) The goal is to break all of the rocks by hitting them with the ball.", 25, "orange")
        rules2 = gamebox.from_text(400, 260, "2.) Use the arrow keys to move the platform to keep the ball in play.", 25, "orange")
        rules3 = gamebox.from_text(400, 290, "3.) The player gets 3 lives. A life is lost when the ball go out of play.", 25, "orange")
        rules4 = gamebox.from_text(400, 320, "4.) The ball moves faster as the levels go on.", 25, "orange")
        rules5 = gamebox.from_text(400, 350, "5.) There are 8 levels, one for each of UVA's ACC opponents this year. ", 25, "orange")
        rules6 = gamebox.from_text(400, 380, "6.) You get points based on how fast you beat the levels. The lower the score, the better.", 25, "orange")

        camera.draw(home1)
        camera.draw(desc)
        camera.draw(desc1)
        camera.draw(desc2)
        camera.draw(desc3)
        camera.draw(desc4)
        camera.draw(rules)
        camera.draw(rules1)
        camera.draw(rules2)
        camera.draw(rules3)
        camera.draw(rules4)
        camera.draw(rules5)
        camera.draw(rules6)

    elif start is False and screen == 2:
        home2 = gamebox.from_text(90, 13, "Press 0 to return home.", 22, "orange")
        high1 = gamebox.from_text(400, 40, "High Score", 35, "orange")
        high2 = gamebox.from_text(400, 70, "The high score is " + str(high_score), 35, "orange")

        camera.draw(home2)
        camera.draw(high1)
        camera.draw(high2)

    elif start:
        level = 1
        if level == 1:
            file_loc = "Pitt Logo Resized.png"
        if level == 2:
            file_loc = "Florida State Logo Resized.png"
        if level == 3:
            file_loc = "Miami Logo Resized.png"
        if level == 4:
            file_loc = "Duke Logo Resized.png"
        if level == 5:
            file_loc = "Louisville Logo Resized.png"
        if level == 6:
            file_loc = "UNC Logo Resized.png"
        if level == 7:
            file_loc = "Georgia Tech Logo Resized.png"
        if level == 8:
            file_loc = "Virginia Tech Logo Resized.png"
        if len(walls) == 0:
            for i in range(100, 750, 50):
                for j in range(150, 225, 25):
                    if j == 150 or j == 200:
                        walls.append(gamebox.from_image(i, j, file_loc))
                    elif j == 175:
                        walls.append(gamebox.from_image(i - 25, j, file_loc))
            level += 1
        if pygame.K_SPACE in keys:
            start_movement = True
            lives = 3

        if start_movement:
            health_bar = gamebox.from_color(health_x, 15, health_color, health, 10)
            camera.draw(health_bar)
            if ball.y > 400:
                lives -= 1
                health -= 40
                health_x -= 20
                if lives == 1:
                    health_color = "red"
                ball.x = 400
                ball.y = 300

            lives_display = gamebox.from_text(530, 15, "Health: ", 22, "orange")
            counter += 1
            ball.x += ball.xspeed
            ball.y += ball.yspeed

            if lives == 0:
                lost = True
                start = False

            time = str(counter // 30)
            time_tot = gamebox.from_text(700, 15, "Score: " + time, 22, "orange")

            if pygame.K_RIGHT in keys:
                platform.x += 10
            if pygame.K_LEFT in keys:
                platform.x -= 10

            if ball.top_touches(platform) or ball.bottom_touches(platform):
                ball.yspeed = -ball.yspeed
            elif ball.right_touches(platform) or ball.left_touches(platform):
                ball.xspeed = -ball.xspeed

            for k in walls:
                camera.draw(k)
                if ball.top_touches(k) or ball.bottom_touches(k):
                    walls.remove(k)
                    ball.yspeed = -ball.yspeed
                elif ball.right_touches(k) or ball.left_touches(k):
                    walls.remove(k)
                    ball.xspeed = -ball.xspeed

            a = 0
            while a < 3:
                if a == 0 or a == 2:
                    if ball.touches(sides[a]):
                        ball.xspeed = -ball.xspeed
                    if platform.touches(sides[a]):
                        platform.move_to_stop_overlapping(sides[a])
                elif a == 1 or a == 3:
                    if ball.touches(sides[a]):
                        ball.yspeed = -ball.yspeed
                camera.draw(sides[a])
                a += 1

                camera.draw(time_tot)
                camera.draw(platform)
                camera.draw(ball)
                camera.draw(lives_display)
                camera.draw(health_bar)

    camera.display()

    # Start window so that you press a key to start
    # Set up physics so that ball bounces at 90-angle
    # Set up so that ball removes brick when ball touches brick
    # Once bricks are gone, level should clear and restart with a faster-moving ball
    # Game will keep a timer for how long it takes for each level to be beat
    # Could also keep a high score doc and make as a menu option
    # Could make level codes that could also be a menu option to access levels you had reached prior
    # Or could instead make a user ID that allows you to save progress

tps = 30
gamebox.timer_loop(tps, tick)
