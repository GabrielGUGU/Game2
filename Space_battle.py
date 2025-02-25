import pgzrun
import random
WIDTH = 600
HEIGHT = 450

TITLE = "Viaje espacial"
FPS = 30

# Objetos y variables
nave1 = Actor('ship1',(100,200))
nave2 = Actor('ship2',(300,200))
nave3 = Actor('ship3',(500,200))
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
mode = 'menu'

balas = []

# Elaboración de la lista de enemigos
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)
    
# Lista de meteoritos
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

# Elaboración
def draw():
    # Pantalla del menú de inicio
    if mode =='menu':
        space.draw()
        screen.draw.text('elige tu nave',center=(300,100),color='white',fontsize = 36)
        nave1.draw()
        nave2.draw() 
        nave3.draw()
    # Modo de juego
    if mode == 'game':
        space.draw()
        planets[0].draw()
        # Atraer a los meteoritos
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        # Atraer a los enemigos
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(balas)):
            balas[i].draw()
    # Ventana de finalización del juego 
    elif mode == 'end':
        space.draw()
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
    
# Controles
def on_mouse_move(pos):
    ship.pos = pos

# Añadir nuevos enemigos a la lista
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Movimiento del enemigo
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

# Movimiento de los planetas
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

# Movimiento de los meteoritos
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

# Colisiones
def collisions():
    global mode
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for j in range(len(balas)):
            if balas[j].colliderect(enemies[i]):
                enemies.pop(i)
                balas.pop(j)
                new_enemy()
                break

def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        for i in range(len(balas)):
            if balas[i].y < 0:
                balas.pop(i)
                break
            else:
                balas[i].y = balas[i].y - 10 
def on_mouse_down(button,pos):
    global mode,ship
    if mode == 'menu' and nave1.collidepoint(pos):
        ship.image = 'ship1'
        mode = 'game'
    elif mode == 'menu' and nave2.collidepoint(pos):
        ship.image = 'ship2'
        mode = 'game'
    elif mode == 'menu' and nave3.collidepoint(pos):
        ship.image = 'ship3'
        mode = 'game'
    elif mode =='game'  and button == mouse.LEFT:
        bala = Actor('missiles')
        bala.pos = ship.pos
        balas.append(bala)
pgzrun.go()
