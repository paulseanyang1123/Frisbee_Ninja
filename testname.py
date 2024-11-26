import sys
import pygame
from setting import Settings
from  pygame.sprite import Sprite
import game_function as gf
from dog import Dog_Liz
from frisbee import Frisbee
from time import sleep
from pygame.sprite import Group
import pandas as pd
import xlsxwriter as xw
from csv import writer

'''
we can also write excel,below is some test.

'''

# newline='', this is used to avoid avery other line problem.
# Pass this file object to csv.writer()
# and get a writer object
# df = pd.read_excel(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\exel file for 777.xlsx')
#
# print(df)
# print(df.iloc[0,:])
# print(df.iloc[1,:])
# # workbook = xw.WorkBook(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\excel-file-for-777.xlsx')
# # worksheet=workbook.add_worksheet('sheet1')
# # worksheet.activate()
#     # writer_object = writer(f_target)
# # title=['Name','Sex']  # sheet first line  表头
# #     # Pass the list as an argument into
# #     # the writerow()

# # worksheet.write_row(list3)  # this is the key step #####
# #     # f_target.write_row(list3)  # this is the key step #####
# #     # # Close the file object
# # workbook.close()
# dfData = {
#     'name': player,
#     'sex': gender,
#     't1': t1,
#     't2': t2,
#     'angle': angle
#
# }
# dfData = pd.DataFrame(dfData, index=['0'],columns=['name','sex','t1','t2','angle'])
# dfData.to_excel(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\exel file for 777.xlsx')# , index='False'
'''
below is the test of using  csv file.


'''
player = input('Please enter the name of the player: ')
gender = input('Please enter the gender of the player: ')
t1 = input('Please enter the time of t1: ')
t2 = input('Please enter the time of t2: ')
angle = input('Please enter the orientation angle: ')

list3 = [player, gender,t1,t2,angle]
with open(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\csv-file-for-777.csv', 'a',
      newline='') as f_target:

    writer_object = writer(f_target)
    writer_object.writerow(list3)  # this is the key step #####
    f_target.close()