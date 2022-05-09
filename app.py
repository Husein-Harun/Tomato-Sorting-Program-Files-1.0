

import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
import model2
import camera
import serial
import numpy as np

arduinoData = serial.Serial('COM5', 9600)

class App:

    def __init__(self, window=tk.Tk(), window_title="Camera"):

        self.window = window
        self.window_title = window_title


        self.model = model2.Model()

        self.auto_predict = False

        self.camera = camera.Camera()

        self.init_gui()

        self.delay = 4000
        self.update()

        self.window.attributes("-topmost", True)
        self.window.mainloop()

    def init_gui(self):

        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(self.window, text="Auto Prediction", width=50, command=self.auto_predict_toggle)
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)

       

        self.btn_predict = tk.Button(self.window, text="Predict", width=50, command=self.predict)
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        
        


    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict





    def update(self):
        if self.auto_predict:
            self.predict()

        ret, frame = self.camera.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def predict(self):
        frame = self.camera.get_frame()
        prediction = self.model.predict(frame)


        if prediction == 0:
            print("No Tomato")
            #self.action("N")
        if prediction == 1:
            print("Small")
            ardData = 'S'
            arduinoData.write(ardData.encode())

            #self.action("S")
        if prediction == 2:
            print("Big")
            ardData = 'B'
            arduinoData.write(ardData.encode())
            #self.action("B")

       