#Developed by Rikin Katyal
#Made for grade 11 computer science project. 2015

from os import environ
from time import strftime, localtime
from math import hypot
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog

from pygame import *
from pygame import gfxdraw

import fonts
import images
import rects
import rdraw
import menu
import dialog

#TODO
#watermark
#ellipse and undo/redo and stamp
#remove lock in corner for mac


# Functions
def draw_tool(tool):
    #Function to draw on the screen with different tools
    global rx, ry,user_blit_count,current_color,mouse_color_at,color_pos
    if tool == 'pencil':
        rdraw.pencil(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'eraser':
        rdraw.eraser(main_copy, mx, my, ox, oy, size)
    if tool == 'bucket':
        mouse_color_at = main_copy.get_at((mx, my))
        rdraw.flood_fill(main_copy, mx, my, mouse_color_at, current_color, canvas)
    if tool == 'brush':
        rdraw.brush(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'rectangle_filled':
        rdraw.rectangle_filled(main, current_color, rx, ry, mx, my)
    if tool == 'rectangle_unfilled':
        rdraw.rectangle_unfilled(main, current_color, (rx, ry), (mx, my), size)
    if tool == 'ellipse_filled':
        rdraw.ellipse_filled(main, current_color, rx, ry, mx, my)
    if tool == 'ellipse_unfilled':
        rdraw.ellipse_unfilled(main, current_color, rx, ry, mx, my, size)
    if tool == "line":
        """
        if pressed[K_LSHIFT] or pressed[K_RSHIFT]:
            distx = abs(rx-mx)
            disty = abs(ry-my)
            rdraw.line(main, current_color, rx, ry, distx, disty, size)
        """
        rdraw.line(main, current_color, rx, ry, mx, my, size)
    if tool == 'eyedropper' and canvas.collidepoint(mpos):
        current_color = main.get_at(mpos)
        color_pos = (431,885)
    if tool == "marker":
        rdraw.marker(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'pen':
        rdraw.pen(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'text':
        global enable_text, tx, ty
        enable_text = True
        tx, ty = mx, my
    if tool == 'spray_paint':
        rdraw.spray_paint(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'magic_eraser':
        mouse_color_at = main_copy.get_at((mx, my))
        rdraw.magic_eraser (main_copy, mx, my, mouse_color_at, (255,255,255), canvas)
    if tool == 'android_stamp':
        android_stamp = transform.scale(images.android_stamp, (128 + (size - 1) * 9, 150 + (size - 1) * 10))
        main.blit(android_stamp, (mx - (128 + (size - 1) * 9) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_lollipop_stamp':
        android_lollipop_stamp = transform.scale(images.android_lollipop_stamp, (107 + (size - 1) * 7, 150 + (size - 1) * 10))
        main.blit(android_lollipop_stamp, (mx - (107 + (size - 1) * 7) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_kitkat_stamp':
        android_kitkat_stamp = transform.scale(images.android_kitkat_stamp, (105 + (size - 1) * 7, 150 + (size - 1) * 10))
        main.blit(android_kitkat_stamp, (mx - (105 + (size - 1) * 7) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_jellybean_stamp':
        android_jellybean_stamp =  transform.scale(images.android_jellybean_stamp, (99 + (size - 1) * 7, 150 + (size - 1) * 10))
        main.blit(android_jellybean_stamp, (mx - (99 + (size - 1) * 7) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_ics_stamp':
        android_ics_stamp = transform.scale(images.android_ics_stamp, (150 + (size - 1) * 7, 110 + (size - 1) * 10))
        main.blit(android_ics_stamp, (mx - (150 + (size - 1) * 7) // 2, my - (110 + (size - 1) * 10) // 2))
    if tool == 'user_image' and user_blit_count == 1:
        global current_image
        img_height = current_image.get_height()
        img_width = current_image.get_width()
        current_image = transform.scale(current_image, (img_width + (size - 1) * 10, img_height + (size - 1) * 10))
        main_copy.blit(current_image, (mx - img_width // 2, my - img_height // 2))
        user_blit_count = 0


def draw_rect_ellipse_line(tool):
    #Draw the rectangle and ellipse on the main_copy
    if tool == 'rectangle_filled':
        rdraw.rectangle_filled(main_copy, current_color, rx, ry, mx,my)
    if tool == 'rectangle_unfilled':
        rdraw.rectangle_unfilled(main_copy, current_color, (rx, ry), (mx, my), size)
    if tool == 'ellipse_filled':
        rdraw.ellipse_filled(main_copy, current_color, rx, ry, mx, my)
    if tool == 'ellipse_unfilled':
        rdraw.ellipse_unfilled(main_copy, current_color, rx, ry, mx, my, size)
    if tool == "line":
        rdraw.line(main_copy, current_color, rx, ry, mx, my, size)


def draw_stamp(tool):
    #Function to blit the stamps onto the screen
    if tool == 'android_stamp':
        android_stamp = transform.scale(images.android_stamp, (128 + (size - 1) * 9, 150 + (size - 1) * 10))
        main_copy.blit(android_stamp, (mx - (128 + (size - 1) * 9) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_lollipop_stamp':
        android_lollipop_stamp = transform.scale(images.android_lollipop_stamp, (107 + (size - 1) * 7, 150 + (size - 1) * 10))
        main_copy.blit(android_lollipop_stamp, (mx - (107 + (size - 1) * 7) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_kitkat_stamp':
        android_kitkat_stamp = transform.scale(images.android_kitkat_stamp, (105 + (size - 1) * 7, 150 + (size - 1) * 10))
        main_copy.blit(android_kitkat_stamp, (mx - (105 + (size - 1) * 7) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_jellybean_stamp':
        android_jellybean_stamp =  transform.scale(images.android_jellybean_stamp, (99 + (size - 1) * 7, 150 + (size - 1) * 10))
        main_copy.blit(android_jellybean_stamp, (mx - (99 + (size - 1) * 7) // 2, my - (150 + (size - 1) * 10) // 2))
    if tool == 'android_ics_stamp':
        android_ics_stamp = transform.scale(images.android_ics_stamp, (150 + (size - 1) * 7, 110 + (size - 1) * 10))
        main_copy.blit(android_ics_stamp, (mx - (150 + (size - 1) * 7) // 2, my - (110 + (size - 1) * 10) // 2))


def quit_program():
    #Function to ask before quitting the program
    global show_dialog, show_menu, current_dialog
    show_dialog = True
    show_menu = False
    current_dialog = 2


def save_work():
    #Function to ask to save work and save it to user directory
    global file_name
    global draw_canvas
    directory = filedialog.asksaveasfilename()
    directory_get_name = directory
    if len(directory) > 1:
        file_name = ''
        while '/' not in file_name:
            file_name += directory_get_name[-1]
            directory_get_name = directory_get_name[:-1]
        file_name = file_name[:-1][::-1]
        image.save(main_copy.subsurface(canvas), '%s.jpg' % directory)
        file_name += " - Android Paint"
        display.set_caption(file_name)
        draw_canvas = False


def filled_rects():
    #Draw all side bars and other rects

    # Header

    draw.rect(main, (221, 221, 221), (0, 25, 1000, 56))
    draw.rect(main, (210, 210, 210), (56, 81, 944, 5))

    # Navigation Bar

    draw.rect(main, (0, 0, 0), (1000, 0, 45, 208))
    draw.rect(main, (0, 0, 0), (1000, 208, 45, 209))
    draw.rect(main, (0, 0, 0), (1000, 417, 45, 208))

    # Status Bar

    draw.rect(main, (0, 0, 0), (0, 0, 1000, 25))

    # Color/Stamp Bar

    draw.rect(main, (221, 221, 221), (0, 625, 1045, 275))
    draw.rect(main, (210, 210, 210), (56, 625, 989, 5))

    # Side Tool Bar

    draw.rect(main, (221, 221, 221), (0, 81, 56, 544))
    draw.rect(main, (210, 210, 210), (56, 86, 5, 959))


def load_image():
    #Function to load user image and blit it on the screen
    global show_dialog, current_dialog
    user_file = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.jpeg;*.png;*.gif;*.bmp'), ('All files', '*.*')))
    user_file_name = str(user_file)
    correct_file_type = False
    for ext in image_ext:
        if ext in user_file_name:
            correct_file_type = True
    if correct_file_type:
        global current_image
        global current_tool
        current_image = image.load(user_file)
        current_tool = 'user_image'
    elif correct_file_type == False and len(user_file_name) > 1:
        current_dialog = 5
        show_dialog = True


def hover(tool):
    #Function to draw rect on tool hover
    draw.rect(main, (207, 207, 207), tool)


def size_font_text(color):
    #Function to change font color of text showing size based on background color
    r = color[0]
    g = color[1]
    b = color[2]
    text_color = (255, 255, 255)
    if r > 200 or g > 200 or b > 200:
        text_color = (0, 0, 0)
    return text_color


def color_picker():
    #Function to get color from color picker and set it as current color
    global current_color
    draw.rect(main, (255, 255, 255), (0, 625, 1045, 275))
    main.blit(images.color_picker, (15, 640))
    if mb[0] == 1 and rects.color_picker_rect.collidepoint(mpos):
        current_color = main.get_at(mpos)


def reset():
    #Function to reset all tools to the beginning
    global size, current_color, current_tool, current_tool_selected, show_menu
    size = 1
    current_color = (0, 0, 0)
    current_tool = 'pencil'
    current_tool_selected = rects.pencil_rect
    main_copy.fill((255,255,255))
    show_menu = False


def undo():
    #Function to undo
    pass


def redo():
    #Function to redo
    pass


# Setup program

file_name = 'Untitled - Android Paint'
display.set_icon(images.iconImage)
display.set_caption(file_name)
environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

# Set boolean values

running = True
lockscreen = True
drag_lock_icon = False
show_menu = False
draw_canvas = False
show_dialog = False
ask_save = False
click = False
drawing = False
show_rect = False
show_ellipse = False
enable_text = False

# Set starting variables

lock_count = 1
lock_icon_pos_x = 210
lock_icon_pos_y = 500
user_blit_count = 0

main_count = 1
size = 1
saves = 1
current_tool = 'pencil'
old_tool = current_tool
current_color = (0, 0, 0, 255)
current_tool_selected = rects.pencil_rect
(ox, oy) = mouse.get_pos()
tx, ty = mouse.get_pos()
canvas = Rect(61, 86, 939, 539)
background_color = (255, 255, 255, 255)
rect_ellipse_line_count = 0
stamp_count = 0
color_pos = (431,885)
current_index = -1
user_text = ''
about_text = ["Welcome to Android Paint. This is an", "Android themed paint program developed", "in Python and Pygame for a computer", "science project.", "", "Version: 0.1 BETA", "© 2015 Rikin Katyal"]
help_text = ["Welcome to Android Paint. You can use", "the tools on the left to draw on the", "canvas. You can use the color picker on", "the bottom to change the drawing color", "or use the Android stamps in your", "drawing. Use the tools at the top to", "save, clear, load, undo, and redo."]
load_success_text = ["Your selected image has been successfully",  "loaded. Click anywhere on the screen to", "place the image there. Note: Size 1 will", "be the original image size. Increasing the", "size will increase the width and height of", "the image by 10px."]
load_fail_text = ['Sorry, looks like you are trying to load', 'an unsupported image. Acceptable file', 'types are: JPG, PNG, GIF, and BMP']

# Image blit

img = [
    images.multi_task,
    images.home,
    images.back_arrow,
    images.battery,
    images.signal,
    images.wifi,
    images.menu,
    images.clear,
    images.save,
    images.pencil,
    images.eraser,
    images.bucket,
    images.load_image,
    images.brush,
    images.rectangles_1,
    images.rectangles_2,
    images.ellipse_1,
    images.ellipse_2,
    images.line,
    images.eyedropper,
    images.color_picker,
    images.slide,
    images.marker,
    images.pen,
    images.text,
    images.spray_paint,
    images.magic_eraser,
    images.redo,
    images.undo,
]

img_location = [
    (1000, 83),
    (1000, 291),
    (1000, 499),
    (918, 2),
    (890, 2),
    (860, 2),
    (948, 29),
    (892, 29),
    (836, 29),
    (4, 85),
    (4, 141),
    (4, 197),
    (780, 29),
    (4, 253),
    (18, 322),
    (4, 309),
    (18, 378),
    (4, 365),
    (4, 421),
    (4, 477),
    (61, 645),
    (-20, 35),
    (4, 531),
    (4, 589),
    (4, 645),
    (4, 701),
    (4, 757),
    (724,29),
    (668,29),
]

# Rects list

rects_list = [
    rects.pencil_rect,
    rects.eraser_rect,
    rects.bucket_rect,
    rects.brush_rect,
    rects.rectangle,
    rects.ellipse,
    rects.line_rect,
    rects.eyedropper_rect,
    rects.load_image_rect,
    rects.save_rect,
    rects.clear_rect,
    rects.menu_rect,
    rects.android_rect,
    rects.android_lollipop_rect,
    rects.android_kitkat_rect,
    rects.android_jellybean_rect,
    rects.android_ics_rect,
    rects.marker_rect,
    rects.pen_rect,
    rects.text_rect,
    rects.spray_paint_rect,
    rects.magic_eraser_rect,
    rects.redo_rect,
    rects.undo_rect,
]

# Stamp list

stamp_list = [images.android_stamp_icon,
              images.android_lollipop_stamp_icon,
              images.android_kitkat_stamp_icon,
              images.android_jellybean_stamp_icon,
              images.android_ics_stamp_icon]
stamp_location = [(480, 645), (580, 645), (680, 645), (780, 645), (880, 650)]

# Undo/redo list

undo_list = []
redo_list = []

# Image extension list

image_ext = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

# Dialog list

dialog_list = ["about", "help", "quit", "save", "load_fail"]

# Special charaters list

special_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "|", "]", "}", "{", "[", ";", ":", "'", '"', ",", "<", ">", ".", "?", "/"]

# Setup TKInter

app = Tk()
app.withdraw()

# Run program

while running:

    while lockscreen:

        # Initialize lockscreen

        if lock_count == 1:
            main = display.set_mode((500, 750))
            lock_count = 0
            mouse.set_visible(True)

        # Get mouse activity

        (mx, my) = mouse.get_pos()
        mb = mouse.get_pressed()
        mpos = mouse.get_pos()

        # Get keyboard activity

        pressed = key.get_pressed()
        ctrl_held = pressed[K_LCTRL] or pressed[K_RCTRL]

        # Blit background

        main.blit(images.lockscreen_bg, (0, 0))
        #main.blit(images.overlay, (0, 0))

        # Blit gradients

        main.blit(images.navigation_gradient, (0, 0))
        main.blit(images.notification_gradient, (0, 0))

        # Create lock icon

        lock_icon_rect = Rect(lock_icon_pos_x, lock_icon_pos_y, 80, 80)
        main.blit(images.lockscreen_lock, (lock_icon_pos_x, lock_icon_pos_y))

        # Lockscreen event loop

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_q and ctrl_held:
                    sys.exit()
                elif e.key == K_SPACE:
                    lockscreen = False

        # Check if lock icon should drag

        if mb[0] == 1 and lock_icon_rect.collidepoint(mpos):
            drag_lock_icon = True
        elif mb[1] == 0:
            drag_lock_icon = False

        # Drag lock icon

        if drag_lock_icon:
            gfxdraw.aacircle(main, 250, 540, 140, (255,255,255))
            lock_icon_pos_x = mx - 40
            lock_icon_pos_y = my - 40
            lock_icon_dist = hypot(mx - 250, my - 540)
            if abs(lock_icon_dist) >= 150:
                time.wait(150)
                lockscreen = False
        else:

            # Set normal lock icon

            lock_icon_pos_x = 210
            lock_icon_pos_y = 500

        # Lockscreen time text

        current_time = strftime('%I:%M')

        # Remove 0 if hour is less than 10

        if current_time[0] == '0':
            current_time = current_time[1:]

        # Lockscreen date text

        current_date = strftime('%a, %B ', localtime()).upper()
        if 'THU' in current_date:
            current_date = current_date.replace('THU', 'THUR')

        # Remove 0 if day is less than 10

        if strftime('%d', localtime())[0] == '0':
            current_date += strftime('%d', localtime())[1:]
        else:
            current_date += strftime('%d', localtime())

        # Render date/time and network text

        lockscreen_time_text = fonts.lockscreen_time_font.render(current_time, True, (255, 255, 255))
        lockscreen_date_text = fonts.lockscreen_date_font.render(current_date, True, (255, 255, 255))
        network_text = fonts.network_font.render("RIKIN", True, (255, 255, 255))

        # Blit text

        main.blit(lockscreen_time_text, (250 - lockscreen_time_text.get_width() // 2, 50))
        main.blit(lockscreen_date_text, (250 - lockscreen_date_text.get_width() // 2, 150))
        if not drag_lock_icon:
            main.blit(network_text, (250 - network_text.get_width() // 2, 625))

        #Blit arrow
        main.blit(images.arrow, (225, 690))

        display.flip()

    # Initialize main program

    if main_count == 1:
        main = display.set_mode((1045, 900))
        main.fill(background_color)
        main_count = 0
        main_copy = main.copy()
        reset()

    # Get mouse activity

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    mpos = mouse.get_pos()

    # Get keyboard activity

    pressed = key.get_pressed()
    ctrl_held = pressed[K_LCTRL] or pressed[K_RCTRL]

    # Main event loop
    #print(enable_text)
    for e in event.get():
        if e.type == QUIT:
            quit_program()

        if e.type == KEYDOWN and enable_text and not show_dialog and not show_menu:
            letter = e.unicode
            if e.key != 8 and not ctrl_held:
                user_text += letter
            if e.key == K_BACKSPACE:
                try:
                    user_text = user_text[:-1]
                except:
                    pass
            if e.key == K_SPACE:
                user_text += ' '
            if e.key == K_RETURN:
                rdraw.text(main_copy, current_color, tx, ty, size, user_text)
                enable_text = False
                user_text = ''
            if e.key == K_ESCAPE:
                user_text = ''
                enable_text = False

        elif e.type == KEYDOWN and not show_dialog:

            # Keyboard shortcuts

            if e.key == K_q and ctrl_held:
                quit_program()
            if e.key == K_s and ctrl_held:
                save_work()
            if e.key == K_r and ctrl_held:
                reset()
            if e.key == K_z and ctrl_held:
                undo()
            if e.key == K_y and ctrl_held:
                redo()
            if e.key == K_p:
                current_tool = "pencil"
                current_tool_selected = rects.pencil_rect
            if e.key == K_e:
                current_tool = "eraser"
                current_tool_selected = rects.eraser_rect
            if e.key == K_b:
                current_tool = "brush"
                current_tool_selected = rects.brush_rect
            if e.key == K_l:
                current_tool = "line"
                current_tool_selected = rects.line_rect
            if e.key == K_f:
                current_tool = "bucket"
                current_tool_selected = rects.bucket_rect
            if e.key == K_m:
                current_tool = "magic_eraser"
                current_tool_selected = rects.magic_eraser_rect
            if e.key == K_s:
                current_tool = "spray_paint"
                current_tool_selected = rects.spray_paint_rect
            if e.key == K_k:
                current_tool = "marker"
                current_tool_selected = rects.marker_rect
            if e.key == K_c:
                current_tool = "pen"
                current_tool_selected = rects.pen_rect
            if e.key == K_t:
                current_tool = "text"
                current_tool_selected = rects.text_rect
            if e.key == K_d:
                current_tool = "eyedropper"
                current_tool_selected = rects.eyedropper_rect

            # Size shortcut

            if e.key == K_1: size = 1
            if e.key == K_2: size = 2
            if e.key == K_3: size = 3
            if e.key == K_4: size = 4
            if e.key == K_5: size = 5
            if e.key == K_6: size = 6
            if e.key == K_7: size = 7
            if e.key == K_8: size = 8
            if e.key == K_9: size = 9
            if e.key == K_0: size = 10

        if e.type == MOUSEBUTTONDOWN and not canvas.collidepoint(mpos) and not rects.color_picker_rect.collidepoint(mpos):
            rdraw.text(main_copy, current_color, tx, ty, size, user_text)
            enable_text = False
            user_text = ''

        if e.type == MOUSEBUTTONDOWN and not show_dialog:
            if e.button == 5:
                size -= 1
            if e.button == 4:
                size += 1

        if e.type == MOUSEBUTTONDOWN and not show_dialog and e.button == 1:
            if rects.menu_rect.collidepoint(mpos):
                show_menu = not show_menu

            # Tools collidepoint

            if not show_dialog and not show_menu:
                if rects.clear_rect.collidepoint(mpos):
                    main_copy.fill((255, 255, 255))
                    draw_canvas = False
                    click = False
                if rects.save_rect.collidepoint(mpos):
                    save_work()
                    click = False
                if rects.load_image_rect.collidepoint(mpos):
                    load_image()
                    user_blit_count = 1
                    click = False
                if rects.pencil_rect.collidepoint(mpos):
                    current_tool = 'pencil'
                    current_tool_selected = rects.pencil_rect
                    click = False
                if rects.eraser_rect.collidepoint(mpos):
                    current_tool = 'eraser'
                    current_tool_selected = rects.eraser_rect
                    click = False
                if rects.bucket_rect.collidepoint(mpos):
                    current_tool = 'bucket'
                    current_tool_selected = rects.bucket_rect
                    click = False
                if rects.brush_rect.collidepoint(mpos):
                    current_tool = 'brush'
                    current_tool_selected = rects.brush_rect
                    click = False
                if rects.rectangle.collidepoint(mpos) and e.type == MOUSEBUTTONDOWN:
                    show_rect = not show_rect
                elif rects.ellipse.collidepoint(mpos) and e.type == MOUSEBUTTONDOWN:
                    show_ellipse = not show_ellipse
                if rects.line_rect.collidepoint(mpos):
                    current_tool = "line"
                    current_tool_selected = rects.line_rect
                    rect_ellipse_line_count = 1
                    click = False
                if rects.eyedropper_rect.collidepoint(mpos):
                    current_tool = 'eyedropper'
                    current_tool_selected = rects.eyedropper_rect
                    click = False
                if rects.pen_rect.collidepoint(mpos):
                    current_tool = "pen"
                    current_tool_selected = rects.pen_rect
                    click = False
                if rects.text_rect.collidepoint(mpos):
                    current_tool = "text"
                    current_tool_selected = rects.text_rect
                    user_text = ''
                    click = False
                    tx, ty = mx, my
                if rects.spray_paint_rect.collidepoint(mpos):
                    current_tool = "spray_paint"
                    current_tool_selected = rects.spray_paint_rect
                    click = False
                if rects.marker_rect.collidepoint(mpos):
                    current_tool = "marker"
                    current_tool_selected = rects.marker_rect
                    click = False
                if rects.magic_eraser_rect.collidepoint(mpos):
                    current_tool = "magic_eraser"
                    current_tool_selected = rects.magic_eraser_rect
                    click = False
                if rects.android_rect.collidepoint(mpos):
                    old_tool = current_tool
                    current_tool = 'android_stamp'
                    current_tool_selected = rects.android_rect
                    click = False
                if rects.android_lollipop_rect.collidepoint(mpos):
                    old_tool = current_tool
                    current_tool = 'android_lollipop_stamp'
                    current_tool_selected = rects.android_lollipop_rect
                    click = False
                if rects.android_kitkat_rect.collidepoint(mpos):
                    old_tool = current_tool
                    current_tool = 'android_kitkat_stamp'
                    current_tool_selected = rects.android_kitkat_rect
                    click = False
                if rects.android_jellybean_rect.collidepoint(mpos):
                    old_tool = current_tool
                    current_tool = 'android_jellybean_stamp'
                    current_tool_selected = rects.android_jellybean_rect
                    click = False
                if rects.android_ics_rect.collidepoint(mpos):
                    old_tool = current_tool
                    current_tool = "android_ics_stamp"
                    current_tool_selected = rects.android_ics_rect
                    click = False
                if rects.undo_rect.collidepoint(mpos):
                    undo()
                if rects.redo_rect.collidepoint(mpos):
                    redo()


                # Home button collidepoint

                if rects.home_rect.collidepoint(mpos) and not show_dialog:
                    quit_program()
                    click = False


        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            click = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            click = False
            undo_list.append(main_copy)
            redo_list.append(main_copy)


    if len(undo_list) > 20:
        undo_list = undo_list[1:]
    if len(redo_list) > 20:
        redo_list = redo_list[1:]

    # Set size

    if size > 10:
        size -= 1
    elif size < 1:
        size += 1

    main.blit(main_copy, (0, 0))

    # Eraser Outline

    if current_tool == "eraser" and canvas.collidepoint(mpos) and not show_menu and not show_dialog:
        draw.circle(main, background_color, (mx, my), size * 6)
        draw.circle(main, (0,0,0), (mx, my), size * 6, 1)

    # Brush Outline

    if current_tool == "brush" and canvas.collidepoint(mpos) and not show_menu and not show_dialog:
        draw.circle(main, (0,0,0), (mx, my), size * 3, 1)
        rdraw.brush(main, current_color, mx, my, ox, oy, size)

    # Marker Outline

    if current_tool == "marker" and canvas.collidepoint(mpos) and not show_dialog and not show_menu:
        draw.circle(main, current_color, (mx, my), size * 2)
        draw.circle(main, (0,0,0), (mx, my), size * 2, 1)

    # Text tool

    if enable_text:
        rdraw.text(main, current_color, tx, ty, size, user_text)

    # Draw with selected tool

    if mb[0] == 1 and not show_menu and canvas.collidepoint(mpos) and not show_dialog and not show_menu:
        if rect_ellipse_line_count == 1 and ('rectangle' in current_tool or 'ellipse' in current_tool or current_tool == "line"):
            rx, ry = mx, my
            rect_ellipse_line_count = 0
        if stamp_count == 1 and "stamp" in current_tool:
            rx,ry = mx, my
            stamp_count = 0
        draw_tool(current_tool)
        drawing = True
        draw_canvas = True
    elif mb[0] == 0:
        if rect_ellipse_line_count == 0 and ('rectangle' in current_tool or 'ellipse' in current_tool or current_tool == "line"):
            draw_rect_ellipse_line(current_tool)
            rect_ellipse_line_count = 1
        if stamp_count == 0 and "stamp" in current_tool and drawing:
            draw_stamp(current_tool)
            stamp_count = 1

        drawing = False


    # Call rect function

    filled_rects()


    # Show rectanlge or ellipse options

    if show_rect:
        draw.rect(main, (221,221,221), rects.rectangle_filled_rect)
        draw.rect(main, (221,221,221), rects.rectangle_unfilled_rect)
        if rects.rectangle_filled_rect.collidepoint(mpos):
            hover(rects.rectangle_filled_rect)
            if click:
                current_tool = 'rectangle_filled'
                current_tool_selected = rects.rectangle
                rect_ellipse_line_count = 1
                click = False
                show_rect = False

        if rects.rectangle_unfilled_rect.collidepoint(mpos):
            hover(rects.rectangle_unfilled_rect)
            if click:
                current_tool = 'rectangle_unfilled'
                current_tool_selected = rects.rectangle
                rect_ellipse_line_count = 1
                click = False
                show_rect = False
        main.blit(images.rectangle_filled, (60,309))
        main.blit(images.rectangle_unfilled, (60,365))
        if click and not rects.rectangle.collidepoint(mpos) and not rects.rectangle_filled_rect.collidepoint(mpos) and not rects.rectangle_unfilled_rect.collidepoint(mpos):
            show_rect = False
            click = False
    elif show_ellipse:
        draw.rect(main, (221,221,221), rects.ellipse_filled_rect)
        draw.rect(main, (221,221,221), rects.ellipse_unfilled_rect)
        if rects.ellipse_filled_rect.collidepoint(mpos):
            hover(rects.ellipse_filled_rect)
            if click:
                current_tool = 'ellipse_filled'
                current_tool_selected = rects.ellipse
                rect_ellipse_line_count = 1
                click = False
                show_ellipse = False

        if rects.ellipse_unfilled_rect.collidepoint(mpos):
            hover(rects.ellipse_unfilled_rect)
            if click:
                current_tool = 'ellipse_unfilled'
                current_tool_selected = rects.ellipse
                rect_ellipse_line_count = 1
                click = False
                show_ellipse = False
        main.blit(images.ellipse_filled, (60,365))
        main.blit(images.ellipse_unfilled, (60,421))
        if click and not rects.ellipse.collidepoint(mpos) and not rects.ellipse_filled_rect.collidepoint(mpos) and not rects.ellipse_unfilled_rect.collidepoint(mpos):
            show_ellipse = False
            click = False

    # Status bar time text

    current_time = strftime('%I:%M')

    # Remove 0 if hour is less than 10

    if current_time[0] == '0':
        current_time = current_time[1:]

    # Render time/project name text

    time_text = fonts.status_bar_time_font.render(current_time, True, (255, 255, 255))
    file_name_font = fonts.status_bar_project_name_font.render(file_name, True, (255, 255, 255))

    # Blit font

    main.blit(time_text, (945, 1))
    main.blit(file_name_font, (4, 4))

    # Tools hover

    for r in rects_list:
        if r.collidepoint(mpos) and not show_dialog:
            hover(r)
        else:
            hover(current_tool_selected)

    if show_menu:
        draw.rect(main, (207, 207, 207), rects.menu_rect)

    # Blit all images from list

    for blit_img in range(len(img)):
        main.blit(img[blit_img], img_location[blit_img])

    # Size and color icon

    draw.circle(main, current_color, (950, 595), 20)
    size_text_color = size_font_text(current_color)
    size_text = fonts.size_text_font.render(str(size), True, size_text_color)
    draw.circle(main, (0, 0, 0), (950, 595), 20, 2)
    if size < 10:
        main.blit(size_text, (945, 584))
    else:
        main.blit(size_text, (940, 584))

    # Color picker and stamps

    if rects.color_picker_rect.collidepoint(mpos) and mb[0] == 1 and not show_dialog and not drawing:
        current_color = main.get_at(mpos)
        color_pos = mpos
    for s in range(len(stamp_list)):
        main.blit(stamp_list[s], stamp_location[s])
    draw.circle(main, background_color, (color_pos), 3)
    draw.circle(main, (0,0,0), (color_pos), 3, 1)

    # Menu

    if show_menu and not show_dialog:
        item_click = menu.show(main, mpos)
        if click:
            if item_click == "lock":
                lockscreen = True
                show_menu = False
                lock_count = 1
                main_count = 1
            elif item_click == "reset":
                reset()
            elif item_click == "help":
                show_dialog = True
                current_dialog = 1
                show_menu = False
            elif item_click == "about":
                show_dialog = True
                current_dialog = 0
                show_menu = False
            elif item_click == "shutdown":
                show_menu = False
                quit_program()

    #Show custom dialog
    
    if show_dialog:
        if dialog_list[current_dialog] == "about":
            get_click = dialog.create(main, "About", about_text, 295, 1, "OK", None, mpos)
            if get_click and click:
                show_dialog = False
        elif dialog_list[current_dialog] == "help":
            get_click = dialog.create(main, "Help", help_text, 300, 1, "OK", None, mpos)
            if get_click and click:
                show_dialog = False
        elif dialog_list[current_dialog] == "quit":
            get_click = dialog.create(main, 'Quit?', ['Are you sure you want to quit?'], 150, 2, "Yes", "No", mpos)
            if get_click and click:
                if not draw_canvas: sys.exit()
                current_dialog = 3
                click = False
            elif get_click == False and click:
                show_dialog = False
                click = False
        elif dialog_list[current_dialog] == "save":
            get_click = dialog.create(main, 'Save?', ['Do you want to save your masterpiece?'], 150, 2, "Yes", "No", mpos)
            if get_click and click:
                save_work()
                sys.exit()
            elif get_click == False and click:
                sys.exit()
        elif dialog_list[current_dialog] == "load_fail":
            get_click = dialog.create(main, "Unsupported File", load_fail_text, 200, 1, "OK", None, mpos)
            if get_click and click:
                show_dialog = False

    # Set mouse to custom mouse

    if current_tool == "text" and canvas.collidepoint(mpos) and not show_dialog and not show_menu:
        mouse.set_visible(False)
        main.blit(images.mouse_text, (mx-16,my-16))
    elif canvas.collidepoint(mpos) and not show_dialog and not show_menu:
        mouse.set_visible(False)
        if not(current_tool == "eraser") and not(current_tool == "brush") and not(current_tool == "marker"):
            main.blit(images.mouse, (mx-16,my-16))
    else:
        mouse.set_visible(True)

    # Get mouse position and set it to old x,y

    ox, oy = mx, my

    display.flip()
quit()