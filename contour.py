# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:10:03 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('detecttest.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)