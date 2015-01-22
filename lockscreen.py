from pygame import *
from math import hypot
from time import strftime, localtime


import images
import fonts

def run(Surface):
    global lock_count
    global lock_icon_pos_x
    global lock_icon_pos_y
    #Initialize lockscreen
    if lock_count == 1:
        display.set_mode((500, 750))
        lock_count = 0
    #Get mouse activity
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        mpos = mouse.get_pos()

        #Get keyboard activity
        pressed = key.get_pressed()
        ctrl_held = pressed[K_LCTRL] or pressed[K_RCTRL]

        #Blit background
        Surface.blit(images.lockscreen_bg, (0, 0))

        #Blit gradients
        Surface.blit(images.navigation_gradient, (0, 0))
        Surface.blit(images.notification_gradient, (0, 0))

        #Create lock icon
        lock_icon_rect = Rect(lock_icon_pos_x, lock_icon_pos_y, 80, 80)
        Surface.blit(images.lockscreen_lock, (lock_icon_pos_x, lock_icon_pos_y))

        #Lockscreen event loop
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_w and ctrl_held:
                    sys.exit()
                elif e.key == K_SPACE:
                    return

        #Check if lock icon should drag
        if mb[0] == 1 and lock_icon_rect.collidepoint(mpos):
            drag_lock_icon = True
        elif mb[1] == 0:
            drag_lock_icon = False

        #Drag lock icon
        if drag_lock_icon:
            draw.circle(Surface, (240, 240, 240), (250, 540), 150, 1)
            lock_icon_pos_x = mx - 40
            lock_icon_pos_y = my - 40
            lock_icon_dist = hypot(mx - 250, my - 540)
            if abs(lock_icon_dist) >= 150:
                time.wait(150)
                lockscreen = False

        #Set normal lock icon
        else:
            lock_icon_pos_x = 210
            lock_icon_pos_y = 500

        #Lockscreen time text
        current_time = strftime("%I:%M")

        #Remove 0 if hour is less than 10
        if current_time[0] == "0":
            current_time = current_time[1:]

        #Lockscreen date text
        current_date = strftime("%a, %B ", localtime()).upper()
        if "THU" in current_date:
            current_date = current_date.replace("THU", "THUR")

        #Remove 0 if day is less than 10
        if strftime("%d", localtime())[0] == "0":
            current_date += strftime("%d", localtime())[1:]
        else:
            current_date += strftime("%d", localtime())

        #Render date/time text
        lockscreen_time_text = fonts.lockscreen_time_font.render(current_time, True, (255, 255, 255))
        lockscreen_date_text = fonts.lockscreen_date_font.render(current_date, True, (255, 255, 255))

        #Blit text
        Surface.blit(lockscreen_time_text, (250 - lockscreen_time_text.get_width() // 2, 50))
        Surface.blit(lockscreen_date_text, (250 - lockscreen_date_text.get_width() // 2, 150))

        display.flip()
    
lock_count = 1
lock_icon_pos_x = 210
lock_icon_pos_y = 500