from pygame import *

import fonts
import images


def show(Surface, pos):
    #Rect is menu item, line is dividing menu items

    lock = draw.rect(Surface, (239,239,239), (825,86,165,50))
    draw.line(Surface, (215,215,215), (825, 136), (989, 136), 1)
    reset = draw.rect(Surface, (239,239,239), (825,137,165,50))
    draw.line(Surface, (215,215,215), (825, 187), (989, 187), 1)
    help = draw.rect(Surface, (239,239,239), (825,188,165,50))
    draw.line(Surface, (215,215,215), (825, 238), (989, 238), 1)
    about = draw.rect(Surface, (239,239,239), (825,239,165,50))
    draw.line(Surface, (215,215,215), (825, 289), (989, 289), 1)
    shutdown = draw.rect(Surface, (239,239,239), (825,290,165,50))
    item_list = [lock, reset, help, about, shutdown]
    hover(Surface, pos, item_list)
    font(Surface)
    icon_list = [images.lock_menu, images.reset_menu, images.help_menu, images.about_menu, images.shutdown_menu]
    icons(Surface, icon_list)
    return str(click(pos, item_list))


def hover(Surface, pos, item_list):
    for item in item_list:
        if item.collidepoint(pos):
            draw.rect(Surface, (210, 210, 210), item)


def font(Surface):
    font_list = ["Lock Device", "Reset", "Help", "About", "Shut Down"]
    font_location = [(835,101), (835,152), (835,203), (835,254), (835,305)]
    for i in range(5):
        Surface.blit((fonts.menu_item_font.render(font_list[i], True, (120,120,120))), font_location[i])


def click(pos, item_list):
    item_rect_list = [(825,86,165,50), (825,137,165,50), (825,188,165,50), (825,239,165,50), (825,290,165,50)]
    item_string_list = ["lock", "reset", "help", "about", "shutdown"]
    for item in item_list:
        if item.collidepoint(pos):
            return item_string_list[item_rect_list.index(item)]


def icons(Surface, icon_list):
    pos = 97
    for i in icon_list:
        Surface.blit(i, (949, pos))
        pos += 51