import math
import random
import pygame
import time
from implementation import *


# Class for the orange dude.


class Player(object):  # creates the player class.

    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)  # gives the player its current position and size.

    def __getitem__(self, key):
        return self.rect[key]

    def move(self, dx, dy):  # function for movement.

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                elif dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                elif dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                elif dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


# Nice class to hold a wall rect


class Wall(object):

    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)  # gives it's position and size.

    def __getitem__(self, key):
        return self.rect[key]


class Door(object):

    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)  # gives it's position and size.


class Enemy(Player):

    def enemyMove(self, dx, dy):  # function for movement.

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.rect.x += dx
        if dy != 0:
            self.rect.y += dy

    pass


def doorList(players, doors):  # Function takes the players list and doors list and checks which door was entered
    for player in players:  # Returning a value for each door to define which one it will go through
        if player.rect == doors[0].rect:
            return 3
        elif player.rect == doors[1].rect:
            return 2
        elif player.rect == doors[2].rect:
            return 1
        elif player.rect == doors[3].rect:
            return 0


def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if 0 <= neighbor[0] < 64 and 0 <= neighbor[1] < 120:
            result.append(neighbor)
    return result


def getWallCoords(walls, doors):
    level_walls = []
    for wall in walls:
        level_walls.append((int(wall.rect[0] / 16), int(wall.rect[1] / 16)))

    return level_walls


# Variables
spawned = 0

# Initialise pygame



def createLevel(doorEntered):  # This function compiles the many strings required to make a level.
    levels = []  # Creates the list for the strings to be stored in.

    levels.append(createTopOrBot())  # Adds the top line to the list.
    j = -1  # J is a variable for creating the middle lines, counts how many there are.
    while j < 64:
        j += 1

        if doorEntered == 0:
            levels.append(TOPcreateMidAreas(j))  # Adds the middle lines to the list.
        elif doorEntered == 1:
            levels.append(LEFTcreateMidAreas(j))
        elif doorEntered == 2:
            levels.append(RIGHTcreateMidAreas(j))
        elif doorEntered == 3:
            levels.append(BOTcreateMidAreas(j))
    levels.append(createTopOrBot())  # Adds the bottom line.
    return levels


def createTopOrBot():  # function for creating the top and bottom lines of the room.
    string = []  # String that stores the current line being created.
    i = 0  # I is my identifier for the x axis.
    T = 0  # T decides whether it is the top line or bottom line.
    while i < 120:  # The screen is 120 squares across so it needs to create 120.
        string.append(0)  # W is the identifier of a wall.
        i = i + 1
        if i == 60 and T == 0:  # If statement testing whether a door needs to be placed at the bottom.
            string += "T"
            T += 1
            i = i + 1
        elif i == 60 and T == 1:  # If statement testing whether a door needs to be placed at the bottom.
            string += "D"
            i = i + 1
    return string


def TOPcreateMidAreas(j):
    i = 0
    string = []
    while i <= 120:
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string += "L"
        if i == 117 and j == 34:
            string.append(1)
        if i == 117 and j == 34:
            string += "R"
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(1)
        if i == 117 and j == 0:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(0)
        if i == 117 and j == 64:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(0)
        if i == 59 and j == 0:
            string.append(1)
            string.append(1)
            string += "P"
        if i == 59 and j == 64:
            string.append(1)
            string.append(1)
            string.append(1)
        if i == 0 or i == 120:
            string.append(0)
        if 1 < i < 121:  # Creates each line that does not require extra treatment from door creation.
            string.append(wallOrNot())
        i = i + 1
    return string


def LEFTcreateMidAreas(j):
    i = 0
    string = []
    while i <= 120:
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string += "L"
        if i == 116 and j == 34:
            string.append(1)
        if i == 116 and j == 34:
            string += "R"
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(1)
        if i == 117 and j == 0:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(1)
        if i == 117 and j == 64:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(1)
        if i == 0 and j == 34:
            string += "P"
        if i == 59 and j == 0:
            string.append(1)
            string.append(1)
            string.append(1)
        if i == 59 and j == 64:
            string.append(1)
            string.append(1)
            string.append(1)
        if i == 0 or i == 120:
            string.append(0)
        if 1 < i < 121:  # Creates each line that does not require extra treatment from door creation.
            string.append(wallOrNot())
        i = i + 1
    return string


def RIGHTcreateMidAreas(j):
    i = 0
    string = []
    while i <= 120:
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string += "L"
        if i == 117 and j == 34:
            string += "P"
        if i == 117 and j == 34:
            string += "R"
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(1)
        if i == 117 and j == 0:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(0)
        if i == 117 and j == 64:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(0)
        if i == 59 and j == 0:
            string.append(1)
            string.append(1)
            string.append(1)
        if i == 59 and j == 64:
            string.append(1)
            string.append(1)
            string.append(1)
        if i == 0 or i == 120:
            string.append(0)
        if 1 < i < 121:  # Creates each line that does not require extra treatment from door creation.
            string.append(wallOrNot())
        i = i + 1
    return string


def BOTcreateMidAreas(j):
    i = 0
    string = []
    while i <= 120:
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string += "L"
        if i == 117 and j == 34:
            string.append(1)
        if i == 117 and j == 34:
            string += "R"
        if i == 0 and j == 34:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(1)
        if i == 117 and j == 0:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(0)
        if i == 117 and j == 64:  # Creating doors depending on values of variables j and i (x and y respectively).
            string.append(0)
        if i == 59 and j == 64:
            string.append(1)  #
            string.append(1)
            string += "P"
        if i == 59 and j == 0:
            string.append(1)
            string.append(1)
            string.append(1)
        if i == 0 or i == 120:
            string.append(0)
        if 1 < i < 121:  # Creates each line that does not require extra treatment from door creation.
            string.append(wallOrNot())
        i = i + 1
    return string


def resetEnemy():  # This resets the enemy spawning each time a level is generated.
    global spawned
    spawned = 0


def spawnedenemy():  # this is ran when the enemy is spawned to stop it spawning again.
    global spawned
    spawned += 1
    return spawned


def wallOrNot():
    global spawned
    chance = random.random()
    if chance > 0.7005:  # Has a 1 in 4 chance of creating a wall.
        return 0
    if spawned == 0:
        if 0.7005 > chance > 0.70:
            spawnedenemy()
            return "E"
    else:
        return 1
    if chance <= 0.70:
        return 1


def wallEnemyTest(dx, dy):
    for wall in walls:
        if enemies[0].rect.colliderect(wall.rect):
            if dx > 0:  # Moving right; Hit the left side of the wall
                enemies[0].rect.right = wall.rect.left
            elif dx < 0:  # Moving left; Hit the right side of the wall
                enemies[0].rect.left = wall.rect.right
            elif dy > 0:  # Moving down; Hit the top side of the wall
                enemies[0].rect.bottom = wall.rect.top
            elif dy < 0:  # Moving up; Hit the bottom side of the wall
                enemies[0].rect.top = wall.rect.bottom


def randomMove(path, x, y):
    global running
    try:
        if path[1][0] > path[0][0]:  # compares the x coordinates of the current path and the next one.
            del path[0]  # deletes the first item in the path.
            return 4, 0  # returns the direction.
        elif path[1][0] < path[0][0]:
            del path[0]
            return -4, 0
        elif path[1][1] > path[0][1]:
            del path[0]
            return 0, 4
        elif path[1][1] < path[0][1]:
            del path[0]
            return 0, -4
        else:  # if the path has no differences it returns the orginal direction.
            return x, y
    except:
        if players[0].rect.colliderect(enemies[0].rect):
            running = False
            return x, y
        else:
            came_from = a_star_search(g, start, goal)
            path = reconstruct_path(came_from, start, goal)
            return x, y



def load_level(doorEntered):  # function creates the level and loads it onto the screen.
    walls = []
    players = []
    doors = []
    enemies = []
    resetEnemy()
    level = createLevel(doorEntered)


    # Parse the level string above
    x = y = 0
    for row in level:
        for col in row:
            if col == 0:  # Adds walls and the player to object lists.
                walls.append(Wall((x, y)))
            elif col == "P":
                players.append(Player((x, y)))
            elif col == "T" or col == "D" or col == "L" or col == "R":  # Adds doors to object list.
                doors.append(Door((x, y)))
            elif col == "E":
                enemies.append(Enemy((x, y)))
            x += 16  # Moves the axis across to create next areas.
        y += 16
        x = 0
    g = GridWithWeights(130, 70)  # this creates the graph.
    level_walls = getWallCoords(walls, doors)
    g.walls = level_walls  # this assigns the graphs walls
    g.weights = {loc: 1000 for loc in level_walls}  # this assigns weight to the walls to up the cost.

    return walls, players, doors, enemies, level, g


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printScoreboard():
    unsortedScoreboardList = []  # this is where the scoreboard is written to.
    sortedScores = []  # this holds all the scores in order.
    sortedScoreboardList = []  # this is where the sorted scoreboard is held.
    for line in open('score.txt'):  # this loop opens and writes the scoreboard to the list.
        lines = line.rstrip('\n')
        unsortedScoreboardList.append(lines)

    for lines in unsortedScoreboardList:  # this loop splits the list into each line.
        for s in lines.split():  # this loops splits each line into substrings.
            if s.isdigit():  # this checks if the substring is a digit.
                sortedScores.append(int(s))  # this adds the digits to the list to be sorted.
    insertionSort(sortedScores)  # sorts the list with the insertion sort.
    for i in sortedScores:  # this loop gets every score in the sorted list.
        for j in unsortedScoreboardList:  # this takes all the scores from the unsorted list.
            for k in j.split():  # this splits the the unsorted list into substrings.
                if str(i) == k:  # this tests the sorted score against the unsorted to find an order.
                    sortedScoreboardList.append(j)  # this adds the score to the sorted list.
                    q = unsortedScoreboardList.index(j)  # this finds the index of the score added to the sorted list.
                    del unsortedScoreboardList[q]  # this deletes the item from the unsorted to prevent duplicates.
    sortedScoreboardList.reverse()  # this reverses the scoreboard so it prints highest first.
    rewrite = 0
    current = 0
    f = open("score.txt", "a")
    f.truncate(0)
    for i in sortedScoreboardList:
        if rewrite <= 9 or rewrite >= len(sortedScoreboardList):
            if sortedScoreboardList[current] != sortedScoreboardList[current-1]:
                print(i)
                current += 1
                f.write(str(i))
                f.write("\n")
            rewrite += 1

    f.close()





startingDoor = 0
walls, players, doors, enemies, level, g = load_level(startingDoor)
running = True
enemymoved = 4
pathfinding = 25
currentSpeedX = 0
currentSpeedY = 0
score = 0

pygame.init()

name = input("Please enter your name: ")

choice = input("If you would like to see a leaderboard, type leaderboard, if not, do literally anything")

if choice.upper() == "LEADERBOARD":
    printScoreboard()




# Set up the display
pygame.display.set_caption("I struggle making things fullscreen")
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)



clock = pygame.time.Clock()


while running:  # Game loop.

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    playerx = int(players[0].rect[0] // 16)  # This creates the players x and y coords.
    playery = int(players[0].rect[1] // 16)
    try:
        enemyx = int(enemies[0].rect[0] // 16)  # This creates the enemy x and y coords.
    except:
        try:
            walls, players, doors, enemies, level, g = load_level(doorEntered)
        except:
            walls, players, doors, enemies, level, g = load_level(startingDoor)

    enemyy = int(enemies[0].rect[1] // 16)

    start, goal = (enemyx, enemyy), (playerx, playery)  # This assigns the player as end and enemy as the start.

    for door in doors:
        if players[0].rect == door.rect:
            doorEntered = doorList(players, doors)
            walls, players, doors, enemies, level, g = load_level(doorEntered)

    if pathfinding == 25:
        came_from = a_star_search(g, start, goal)
        try:
            path = reconstruct_path(came_from, start, goal)
        except:
            walls, players, doors, enemies, level, g = load_level(startingDoor)
        score += 10
        pathfinding = 0
    pathfinding += 1


    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    for enemy in enemies:
        if enemymoved == 4:
            currentSpeedX, currentSpeedY = randomMove(path, currentSpeedX, currentSpeedY)
            enemymoved = 0
        enemymoved += 1
        enemy.enemyMove(currentSpeedX, currentSpeedY)
        wallEnemyTest(currentSpeedX, currentSpeedY)

    # Just added this to make it slightly fun ;)


    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for player in players:
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
    for door in doors:
        pygame.draw.rect(screen, (0, 200, 0), door.rect)
    for enemy in enemies:
        pygame.draw.rect(screen, (220, 232, 62), enemy.rect)
    pygame.display.flip()

    # print(start, goal)
    # print(path)
    # draw_grid(g, width=1, point_to=came_from, start=start, goal=goal)


scoreboard = open("score.txt","a")
scoreboard.write("\n")
scoreboard.write(name)
scoreboard.write(" ")
scoreboard.write(str(score))
scoreboard.close()




you_lose = pygame.image.load('Untitled.png')
screen.fill((0, 0, 0))
screen.blit(you_lose, (0, 0))
pygame.display.flip()
time.sleep(5)
pygame.display.quit()

choice2 = input("would you like to view the leaderboard again? If so type Yes: ")

if choice2.upper() == "YES":
    printScoreboard()
