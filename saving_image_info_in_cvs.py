#ek img ko copy karna r isko flat from mai lana r csv file mai likhna
import sys
import os
import numpy as np
from PIL import Image
import csv

#first we fetch the info of directory
fileslist = []
#use module of os, csv ki directory root directory h, pehly root phr directory phir files,
#walk ka funt ye sari info check kry ga
for root, dirs, files in os.walk('C:/Users/hp/AppData/Local/Programs/Python/Python36/face/', topdown=False):
    for name in files:
    print(name)
    if name.endswith('.jpg'):
        complete_name = os.path.join(root, name)
            print(complete_name)
            fileslist.append(complete_name)
