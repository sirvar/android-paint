#Font module

from pygame import font

#Initialize fonts

font.init()

#Status Bar Fonts
status_bar_time_font = font.Font("fonts/Roboto-Regular.ttf", 20)
status_bar_project_name_font = font.Font("fonts/Roboto-Regular.ttf", 15)

#Lockscreen Fonts
lockscreen_time_font = font.Font("fonts/Roboto-Thin.ttf", 85)
lockscreen_date_font = font.Font("fonts/Roboto-Regular.ttf", 15)
network_font = font.Font("fonts/Roboto-Regular.ttf", 15)

#Size Text Font
size_text_font = font.Font("fonts/Roboto-Regular.ttf", 18)

#Menu Font
menu_item_font = font.Font("fonts/Roboto-Regular.ttf", 18)

#Dialog Fonts
dialog_title_font = font.Font("fonts/Roboto-Regular.ttf", 20)
dialog_body_font = font.Font("fonts/Roboto-Regular.ttf", 15)
dialog_button_font = font.Font("fonts/Roboto-Regular.ttf", 12)

#App Font
app_title_font = font.Font("fonts/Roboto-Regular.ttf", 22)