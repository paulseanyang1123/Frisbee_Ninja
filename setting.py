# import pyautogui
# #this tool let you acquire  current screen automatically. ****  自动获得当前屏幕大小
# screen_width, screen_height = pyautogui.size()
# print("Screen width: ", screen_width)
# print("Screen height: ", screen_height)
'''
Screen width:  1920
Screen height:  1080
'''

class Settings():
    def __init__(self):
        self.screen_width=1600
        self.screen_height=900

        a_r=0
        b_g=100
        c_b=0
        self.bg_color = (a_r, b_g, c_b)
        # self.location = (0,0)
