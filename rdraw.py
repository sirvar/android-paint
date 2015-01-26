#Custom drawing module using Pygame

from pygame import *
from random import *
from math import hypot


def pencil(surface, color, x, y, ox, oy, size):
    #Pencil function to draw lines
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    draw.circle(surface, color, (x, y), size // 2)      #Draw connected circles to form lines
    for i in range(dist):
        draw.circle(surface, color, (int(x + (i * sx) / dist), int(y + (i * sy) / dist)), size // 2)


def eraser(surface, x, y, ox, oy, size):
    #Eraser function to draw white circles
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    draw.circle(surface, (255,255,255), (x,y), size * 6)        #Draw connected circles to form eraser
    for i in range(dist):
        draw.circle(surface, (255,255,255), (int(x + (i * sx) / dist), int(y + (i * sy) / dist)), size * 6)


def brush(surface, color, x, y, ox, oy, size):
    #Brush function to draw alpha brush
    brush_surface = Surface((size * 6, size * 6), SRCALPHA)
    r = color[0]
    g = color[1]
    b = color[2]
    draw.circle(brush_surface, (r,g,b,4), (size * 3, size * 3), (size * 3))
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    surface.blit(brush_surface, (x - (size * 3), y - (size * 3)))       #Draw connected surfaces with alpha value to form brush
    for i in range(dist):
        surface.blit(brush_surface, (int(x + (i * sx) / dist) - (size * 3), int(y + (i * sy) / dist) - (size * 3)))


def rectangle_filled(surface, color, x1, y1, x2, y2):
    #Filled rectangle function
    draw.rect(surface, color, (x1, y1, x2 - x1, y2 - y1))


def rectangle_unfilled(surface, color, top, bottom, width):
    #Custom function for drawing unfilled rectangle
    n = 0
    if width % 2 == 0: n = 1
    if top[0] < bottom[0]:
        draw.line(surface, color, (top[0]-(width//2)+n, top[1]), (bottom[0]+(width//2),top[1]), width)
        draw.line(surface, color, (top[0]-(width//2)+n, bottom[1]), (bottom[0]+(width//2), bottom[1]), width)
    else:
        draw.line(surface, color, (top[0]+(width//2), top[1]), (bottom[0]-(width//2)+n,top[1]), width)
        draw.line(surface, color, (top[0]+(width//2), bottom[1]), (bottom[0]-(width//2)+n, bottom[1]), width)

    #Side lines
    draw.line(surface, color, top, (top[0], bottom[1]), width)
    draw.line(surface, color, (bottom[0], top[1]), bottom, width)


def ellipse_filled(surface, color, x1, y1, x2, y2):
    #Filled ellipse function
    eRect = Rect(x1, y1, x2 - x1, y2 - y1)
    eRect.normalize()
    draw.ellipse(surface, color, eRect)


def ellipse_unfilled(surface, color, x1, y1, x2, y2, size):
    #Unfilled ellipse function
    eRect = Rect(x1, y1, x2 - x1, y2 - y1)
    eRect.normalize()
    if eRect.height < size * 2 or eRect.width < size * 2:
        draw.ellipse(surface, color, eRect)
    else:
        draw.ellipse(surface, color, eRect, size)


def line(surface, color, x1, y1, x2, y2, size):
    #Line function
    draw.line(surface, color, (x1, y1), (x2, y2), size)


def spray_paint(surface, color, x, y, ox, oy, size):
    #Spray paint effect funtion
    for i in range(size * 3):
            (px, py) = (randint(x - size * 4, x + size * 4), randint(y - size * 4, y + size * 4))
            dist = hypot(px - x, py - y)
            if dist <= size * 4:
                surface.set_at((px,py), color)


def flood_fill(surface, x, y, color_at, color_set, canvas):
    #Flood fill/bucket fill function
    flood_pos = [(x,y)]
    surface.set_clip(canvas)
    if color_at != color_set:
        while len(flood_pos) > 0:
            px, py = flood_pos.pop()
            if surface.get_at((px, py)) == color_at and canvas.collidepoint((px, py)):
                surface.set_at((px, py), color_set)
                flood_pos.append((px+1,py))
                flood_pos.append((px-1,py))
                flood_pos.append((px,py+1))
                flood_pos.append((px,py-1))


def magic_eraser(surface, x, y, color_at, color_set, canvas):
    #Magic eraser function (a.k.a. white flood fill)
    flood_pos = [(x,y)]
    surface.set_clip(canvas)
    if color_at != color_set:
        while len(flood_pos) > 0:
            px, py = flood_pos.pop()
            if surface.get_at((px, py)) == color_at and canvas.collidepoint((px, py)):
                surface.set_at((px, py), color_set)
                flood_pos.append((px+1,py))
                flood_pos.append((px-1,py))
                flood_pos.append((px,py+1))
                flood_pos.append((px,py-1))
                flood_pos.append((px+1,py+1))
                flood_pos.append((px+1,py-1))
                flood_pos.append((px-1,py+1))
                flood_pos.append((px-1,py-1))


def marker(surface, color, x, y, ox, oy, size):
    #Marker function
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    draw.rect(surface, color, ((x - size), (y - size * 2), size, size * 4))
    for i in range(dist):
        draw.rect(surface, color, ((int(x + (i * sx) / dist) - size),(int(y + (i * sy) / dist) - size * 2), size, size * 4))


def pen(surface, color, mx, my, ox, oy, size):
    #Calligraphy pen function
    sx = ox - mx
    sy = oy - my
    dist = int(max(abs(sx), abs(sy)))
    draw.line(surface, color, (mx - size, my - size), (mx + size, my + size), 2)
    for i in range(dist):
        x = int(mx + (i * sx) / dist)
        y = int(my + (i * sy) / dist)
        draw.line(surface, color, (x - size, y - size), (x + size, y + size), 2)


def text(surface, color, tx, ty, size, user_text):
    #Text tool function
    user_text_font = font.Font("fonts/Roboto-Regular.ttf",  (size * 10))
    user_text_font_text = user_text_font.render(user_text, True, color)
    surface.blit(user_text_font_text, (tx,ty - user_text_font_text.get_height()))