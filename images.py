from pygame import image, transform

#Load images

#Image for icon/logo
iconImage = image.load("images/icon.png")

#Image for mouse
mouse = image.load("images/Mouse.png")
mouse_text = image.load("images/Mouse_Text.png")

#Images for navigation bar
multi_task = image.load("images/Multitask.png")
home = image.load("images/Home.png")
back_arrow = image.load("images/BackArrow.png")

#Images for status bar
battery = image.load("images/Battery.png")
signal = image.load("images/Signal.png")
wifi = image.load("images/WiFi.png")

#Images for tools
menu = image.load("images/Menu.png")
clear = image.load("images/Clear.png")
save = image.load("images/Save.png")
load_image = image.load("images/Plus.png")
undo = image.load("images/Undo.png")
redo = image.load("images/Redo.png")
pencil = image.load("images/Pencil.png")
eraser = image.load("images/Eraser.png")
bucket = image.load("images/Bucket.png")
brush = image.load("images/Brush.png")
rectangles_1 = image.load("images/rectangle_1.png")
rectangles_2 = image.load("images/rectangle_2.png")
rectangle_filled = image.load("images/Rectangle_Filled.png")
rectangle_unfilled = image.load("images/Rectangle_Unfilled.png")
ellipse_1 = image.load("images/ellipse_1.png")
ellipse_2 = image.load("images/ellipse_2.png")
ellipse_filled = image.load("images/Ellipse_Filled.png")
ellipse_unfilled = image.load("images/Ellipse_Unfilled.png")
line = image.load("images/Line.png")
eyedropper = image.load("images/EyeDropper.png")
marker = image.load("images/Marker.png")
pen = image.load("images/Pen.png")
text = image.load("images/Text.png")
spray_paint = image.load("images/SprayPaint.png")
magic_eraser = image.load("images/Magic_Eraser.png")
slide = image.load("images/Slide.png")

#Images for lockscreen
lockscreen_bg = image.load("images/LockScreenBG.jpg")
lockscreen_lock = image.load("images/LockIcon.png")
navigation_gradient = image.load("images/NavigationBarGradient.png")
notification_gradient = image.load("images/NotificationBarGradient.png")
arrow = image.load("images/Arrow.png")

#Images for color picker and stamps
color_picker = image.load("images/ColorPicker.png")
android_stamp = image.load("images/Android_Stamp.png")
android_lollipop_stamp = image.load("images/Android_Lollipop.png")
android_kitkat_stamp = image.load("images/Android_Kitkat.png")
android_jellybean_stamp = image.load("images/Android_Jellybean.png")
android_ics_stamp = image.load("images/Android_ICS.png")
droid_iron_stamp = image.load("images/droid_iron.png")
droid_frank_stamp = image.load("images/droid_frank.png")
droid_r2d2_stamp = image.load("images/droid_r2d2.png")
droid_hulk_stamp = image.load("images/droid_hulk.png")
droid_ninja_stamp = image.load("images/droid_ninja.png")

#Icons for menu
lock_menu = image.load("images/Lock Device.png")
reset_menu = image.load("images/Reset.png")
help_menu = image.load("images/Help.png")
about_menu = image.load("images/About.png")
shutdown_menu = image.load("images/Shutdown.png")

#Transform images
iconImage = transform.scale(iconImage, (52,52))
lockscreen_lock = transform.scale(lockscreen_lock, (80,80))
navigation_gradient = transform.scale(navigation_gradient, (500, 750))
notification_gradient = transform.scale(notification_gradient, (500, 750))
color_picker = transform.scale(color_picker, (370, 240))
android_stamp_icon = transform.scale(android_stamp, (85, 100))
android_lollipop_stamp_icon = transform.scale(android_lollipop_stamp, (71, 100))
android_kitkat_stamp_icon = transform.scale(android_kitkat_stamp, (70, 100))
android_jellybean_stamp_icon = transform.scale(android_jellybean_stamp, (66, 100))
android_ics_stamp_icon = transform.scale(android_ics_stamp, (123, 90))
droid_iron_stamp_icon = transform.scale(droid_iron_stamp, (100,100))
droid_frank_stamp_icon = transform.scale(droid_frank_stamp, (100,100))
droid_r2d2_stamp_icon = transform.scale(droid_r2d2_stamp, (100,100))
droid_hulk_stamp_icon = transform.scale(droid_hulk_stamp, (100,100))
droid_ninja_stamp_icon = transform.scale(droid_ninja_stamp, (100,100))