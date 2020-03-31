#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:27:43 2020

@author: buitrago
"""

import serial
import mysql.connector as mq

puerto = serial.Serial('/dev/ttyUSB0', 115200)
while True:
    data = puerto.readline()
    limpios = int(data)
    print(int(data))
    db = mq.connect(host="localhost", user="root", password="passtoor", db="ESP")
    cursor = db.cursor()
    sql = "insert into Datos (nivelhumo) values (%s)"
    cursor.execute(sql, (limpios,))
    db.commit()
    
