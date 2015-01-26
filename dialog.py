#Custon Android themed dialog box module

from pygame import *

import fonts

#Custom Android themed dialog box

def create(surface, title, body, height, option_nums, option_1, option_2, pos, sw=1045, sh=900):
    #Create initial dialog box
    overlay = Surface((sw, sh), SRCALPHA)
    draw.rect(overlay, (0,0,0,80), (0,0,1045, 900))
    surface.blit(overlay, (0,0))
    draw.rect(surface, (245,245,245), (372, 450 - height//2, 300, height))
    draw.line(surface, (51,181,229), (372,500 - height//2), (672,500 - height//2), 2)
    buttons(surface, option_nums, height, pos)
    font(surface, title, body, height, option_nums, option_1, option_2)
    return click(pos, option_nums, height)


def font(surface, title, body, height, n, opt_1, opt_2):
    #Function to add font
    surface.blit((fonts.dialog_title_font.render(title, True, (51,181,229))), (382, 465 - height//2))
    line_height = 0
    for b in body:
        surface.blit((fonts.dialog_body_font.render(b, True, (0,0,0))), (382, 520 - height//2 + line_height))
        line_height += 22
    if n == 1:
        button_text = fonts.dialog_button_font.render(opt_1, True, (0,0,0))
        surface.blit(button_text, (522 - button_text.get_width() // 2, 417 + height//2))
    elif n == 2:
        button_text2 = fonts.dialog_button_font.render(opt_2, True, (0,0,0))
        button_text1 = fonts.dialog_button_font.render(opt_1, True, (0,0,0))
        surface.blit(button_text2, (447 - button_text2.get_width() // 2, 417 + height//2))
        surface.blit(button_text1, (597 - button_text1.get_width() // 2, 417 + height//2))


def buttons(surface, n, height, pos):
    #Funtion to add buttons
    rect_list = []
    if n == 1:
        draw.line(surface, (222,222,222), (372,400 + height//2), (671,400 + height//2), 1)
        rect_list.append(Rect(372, 401 + height//2, 300, 50))

    elif n == 2:
        draw.line(surface, (222,222,222), (372,400 + height//2), (671,400 + height//2), 1)
        draw.line(surface, (222,222,222), (522,400 + height//2), (522,449 + height//2), 1)
        rect_list.append(Rect(372, 400 + height//2, 150, 50))
        rect_list.append(Rect(522,400 + height//2, 150, 50))

    hover(surface, rect_list, pos)


def hover(surface, button_list, pos):
    #Function to get buttons hover
    for button in button_list:
        if button.collidepoint(pos):
            draw.rect(surface, (227,227,227), button)


def click(pos, n, height):
    #Function to get button click
    if n == 1:
        button_rect = Rect(372, (401 + height//2), 300, 50)
        if button_rect.collidepoint(pos):
            return True
    elif n == 2:
        button_rect_1 = Rect(372, (401 + height//2), 150, 50)
        button_rect_2 = Rect(522, (401 + height//2), 150, 50)
        if button_rect_1.collidepoint(pos):
            return False
        elif button_rect_2.collidepoint(pos):
            return True