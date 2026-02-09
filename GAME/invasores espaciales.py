import random
import pygame
from pygame import mixer

pygame.init()
mixer.init()

# ---------------- CONFIGURACIÓN ----------------
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Invasión Espacial")

BLANCO = (255, 255, 255)
ROJO = (255, 60, 60)

fuente = pygame.font.SysFont("Arial", 28)
fuente_grande = pygame.font.SysFont("Arial", 64)

reloj = pygame.time.Clock()

# ---------------- ASSETS ----------------
fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

jugador_img = pygame.transform.scale(
    pygame.image.load("cohete.png").convert_alpha(), (64, 64)
)

enemigo_img = pygame.transform.scale(
    pygame.image.load("enemigo.png").convert_alpha(), (64, 64)
)

bala_img = pygame.transform.scale(
    pygame.image.load("bala.png").convert_alpha(), (16, 32)
)

sonido_bala = mixer.Sound("disparo.mp3")

# ---------------- JUGADOR ----------------
jugador_x, jugador_y = 368, 500
vel_jugador = 4
vidas = 3

# ---------------- ENEMIGOS ----------------
cantidad_enemigos = 6
enemigos = []

def crear_enemigo():
    return {
        "x": random.randint(0, 736),
        "y": random.randint(50, 150),
        "vx": random.choice([-1, 1]),
        "vy": 20
    }

for _ in range(cantidad_enemigos):
    enemigos.append(crear_enemigo())

# ---------------- BALA ----------------
bala_x, bala_y = 0, 0
bala_vel = 22          # 🚀 DISPARO ULTRA RÁPIDO
bala_visible = False

# ---------------- JUEGO ----------------
puntaje = 0
estado = "MENU"

# ---------------- FUNCIONES ----------------
def texto(txt, fuente, color, x, y):
    img = fuente.render(txt, True, color)
    pantalla.blit(img, (x, y))

def hay_colision(ex, ey, bx, by):
    return ((ex - bx) ** 2 + (ey - by) ** 2) ** 0.5 < 30

# ---------------- LOOP PRINCIPAL ----------------
ejecutando = True
while ejecutando:
    reloj.tick(60)
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if estado == "MENU" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                estado = "JUGANDO"
                puntaje = 0
                vidas = 3
                enemigos = [crear_enemigo() for _ in range(cantidad_enemigos)]

        if estado == "GAME_OVER" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                estado = "MENU"

        if estado == "JUGANDO" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not bala_visible:
                sonido_bala.play()
                bala_x = jugador_x + 24   # centro de la nave
                bala_y = jugador_y
                bala_visible = True

    teclas = pygame.key.get_pressed()

    # ---------------- MENU ----------------
    if estado == "MENU":
        texto("INVASIÓN ESPACIAL", fuente_grande, BLANCO, 140, 200)
        texto("Presiona ENTER para comenzar", fuente, BLANCO, 220, 300)

    # ---------------- JUGANDO ----------------
    elif estado == "JUGANDO":

        # Movimiento libre del jugador
        if teclas[pygame.K_LEFT]:
            jugador_x -= vel_jugador
        if teclas[pygame.K_RIGHT]:
            jugador_x += vel_jugador
        if teclas[pygame.K_UP]:
            jugador_y -= vel_jugador
        if teclas[pygame.K_DOWN]:
            jugador_y += vel_jugador

        jugador_x = max(0, min(jugador_x, 736))
        jugador_y = max(0, min(jugador_y, 536))

        # Enemigos
        for e in enemigos:
            e["x"] += e["vx"]

            if e["x"] <= 0 or e["x"] >= 736:
                e["vx"] *= -1
                e["y"] += e["vy"]

            if e["y"] > ALTO:
                vidas -= 1
                e.update(crear_enemigo())

            if bala_visible and hay_colision(e["x"], e["y"], bala_x, bala_y):
                puntaje += 10
                bala_visible = False
                bala_y = jugador_y
                e.update(crear_enemigo())

            pantalla.blit(enemigo_img, (e["x"], e["y"]))

        # Bala (respuesta inmediata)
        if bala_visible:
            bala_y -= bala_vel
            pantalla.blit(bala_img, (bala_x, bala_y))
            if bala_y < -32:
                bala_visible = False

        # HUD
        texto(f"Puntaje: {puntaje}", fuente, BLANCO, 10, 10)
        texto(f"Vidas: {vidas}", fuente, BLANCO, 650, 10)

        pantalla.blit(jugador_img, (jugador_x, jugador_y))

        if vidas <= 0:
            estado = "GAME_OVER"

    # ---------------- GAME OVER ----------------
    elif estado == "GAME_OVER":
        texto("GAME OVER", fuente_grande, ROJO, 230, 220)
        texto(f"Puntaje final: {puntaje}", fuente, BLANCO, 300, 300)
        texto("ENTER para volver al menú", fuente, BLANCO, 230, 350)

    pygame.display.update()

pygame.quit()
