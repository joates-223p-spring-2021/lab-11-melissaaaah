#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:42:30 2022

@author: melissahuynh
"""

class Settings:
    """A Class to store all settings for ALien Invasions"""
    
    def __init__(self):
        #Initialize game settings
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 1.5
        self.bg_color = (230,230,230)