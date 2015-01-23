from pygame import *
from random import *
from math import hypot


def pencil(Surface, color, x, y, ox, oy, size):
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    draw.circle(Surface, color, (x, y), size // 2)
    for i in range(dist):
        draw.circle(Surface, color, (int(x + (i * sx) / dist), int(y + (i * sy) / dist)), size // 2)


def eraser(Surface, x, y, ox, oy, size):
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    draw.circle(Surface, (255,255,255), (x,y), size * 6)
    for i in range(dist):
        draw.circle(Surface, (255,255,255), (int(x + (i * sx) / dist), int(y + (i * sy) / dist)), size * 6)


def brush(surface, color, x, y, ox, oy, size):
    brush_surface = Surface((size * 6, size * 6), SRCALPHA)
    r = color[0]
    g = color[1]
    b = color[2]
    alpha_dict = {1:8,2:6,3:4}
    if size < 4:
        alpha_value = alpha_dict[size]
    else:
        alpha_value = 3
    draw.circle(brush_surface, (r,g,b,alpha_value), (size * 3, size * 3), (size * 3))
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    for i in range(dist):
        surface.blit(brush_surface, (int(x + (i * sx) / dist) - (size * 3), int(y + (i * sy) / dist) - (size * 3)))


def rectangle_filled(Surface, color, x1, y1, x2, y2):
    draw.rect(Surface, color, (x1, y1, x2 - x1, y2 - y1))


def rectangle_unfilled(Surface, color, top, bottom, width):
    #Custom function for drawing unfilled rectangle
    n = 0
    if width % 2 == 0: n = 1
    if top[0] < bottom[0]:
        draw.line(Surface, color, (top[0]-(width//2)+n, top[1]), (bottom[0]+(width//2),top[1]), width)
        draw.line(Surface, color, (top[0]-(width//2)+n, bottom[1]), (bottom[0]+(width//2), bottom[1]), width)
    else:
        draw.line(Surface, color, (top[0]+(width//2), top[1]), (bottom[0]-(width//2)+n,top[1]), width)
        draw.line(Surface, color, (top[0]+(width//2), bottom[1]), (bottom[0]-(width//2)+n, bottom[1]), width)

    #Side lines
    draw.line(Surface, color, top, (top[0], bottom[1]), width)
    draw.line(Surface, color, (bottom[0], top[1]), bottom, width)


def ellipse_filled(Surface, color, x1, y1, x2, y2):
    eRect = Rect(x1, y1, x2 - x1, y2 - y1)
    eRect.normalize()
    draw.ellipse(Surface, color, eRect)


def ellipse_unfilled(Surface, color, x1, y1, x2, y2, size):
    #eRect = Rect(x1, y1, x2 - x1, y2 - y1)
    #eRect = eRect.normalize()
    #draw.ellipse(Surface, color, eRect, size)
    pass


def line(Surface, color, x1, y1, x2, y2, size):
    draw.line(Surface, color, (x1, y1), (x2, y2), size)


def spray_paint(Surface, color, x, y, ox, oy, size):
    for i in range(size * 3):
            (px, py) = (randint(x - size * 4, x + size * 4), randint(y - size * 4, y + size * 4))
            dist = hypot(px - x, py - y)
            if dist <= size * 4:
                Surface.set_at((px,py), color)


def flood_fill(Surface, x, y, color_at, color_set, canvas):
    flood_pos = [(x,y)]
    Surface.set_clip(canvas)
    if color_at != color_set:
        while len(flood_pos) > 0:
            px, py = flood_pos.pop()
            if Surface.get_at((px, py)) == color_at and canvas.collidepoint((px, py)):
                Surface.set_at((px, py), color_set)
                flood_pos.append((px+1,py))
                flood_pos.append((px-1,py))
                flood_pos.append((px,py+1))
                flood_pos.append((px,py-1))


def magic_eraser(Surface, x, y, color_at, color_set, canvas):
    flood_pos = [(x,y)]
    Surface.set_clip(canvas)
    if color_at != color_set:
        while len(flood_pos) > 0:
            px, py = flood_pos.pop()
            if Surface.get_at((px, py)) == color_at and canvas.collidepoint((px, py)):
                Surface.set_at((px, py), color_set)
                flood_pos.append((px+1,py))
                flood_pos.append((px-1,py))
                flood_pos.append((px,py+1))
                flood_pos.append((px,py-1))
                flood_pos.append((px+1,py+1))
                flood_pos.append((px+1,py-1))
                flood_pos.append((px-1,py+1))
                flood_pos.append((px-1,py-1))


def marker(Surface, color, x, y, ox, oy, size):
    sx = ox - x
    sy = oy - y
    dist = int(max(abs(sx), abs(sy)))
    draw.rect(Surface, color, ((x - size), (y - size * 2), size, size * 4))
    for i in range(dist):
        draw.rect(Surface, color, ((int(x + (i * sx) / dist) - size),(int(y + (i * sy) / dist) - size * 2), size, size * 4))


def pen(Surface, color, mx, my, ox, oy, size):
    """
    dist = hypot(max(mx-ox,ox-mx), max(my-oy,oy-my))
    sx = ox - mx
    sy = oy - my
    dist = int(max(abs(sx), abs(sy)))
    draw.circle(Surface, color, (mx, my), int((200-dist)*0.028))
    for i in range(dist):
        draw.circle(Surface, color, (int(mx + (i * sx) / dist), int(my + (i * sy) / dist)), int((200 - dist) * 0.025))
    """
    sx = ox - mx
    sy = oy - my
    dist = int(max(abs(sx), abs(sy)))
    draw.line(Surface, color, (mx - size, my - size), (mx + size, my + size), 2)
    for i in range(dist):
        x = int(mx + (i * sx) / dist)
        y = int(my + (i * sy) / dist)
        draw.line(Surface, color, (x - size, y - size), (x + size, y + size), 2)


def text(Surface, color, tx, ty, size, user_text):
    user_text_font = font.Font("fonts/Roboto-Regular.ttf",  (size * 10))
    user_text_font_text = user_text_font.render(user_text, True, color)
    Surface.blit(user_text_font_text, (tx,ty))