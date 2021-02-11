import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import webbrowser
from selenium import webdriver
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv

class Application(ttk.Frame):

	def __init__(self, master):
	   
		ttk.Frame.__init__(self, master)

		website_list =     sorted({"https://www.google.com",  # stored list of websites in menu
							   "https://www.mkdynamics.net",
							   "https://www.uccs.edu",
							   "https://www.yahoo.com",
							   "https://www.duckduckgo.com"})

		pavgr_list =     sorted({50,  # stored list of websites in menu
							   60,
							   70,})

		self.pack()
		self.variable = StringVar(self)
		self.variable2 = StringVar(self)
		self.point = pavgr_list[0]
		self.variable.set(website_list[0])
		self.variable2.set(pavgr_list[0])
		self.url_label = ttk.Label(self, text = "Select a Website")
		self.option_menu = ttk.OptionMenu(self, self.variable, *website_list, command=self.select_url)
		self.Button1 = ttk.Button(self, text="Open Website", command=self.open_browser) # allows selection from website menu
		self.location_chooser = ttk.Button(self, text="Choose File to Be Processed", command=self.select_file)
		self.open_button = ttk.Button(self, text="Open File", command=self.run_program)
		self.avgr_label = ttk.Label(self, text = "Point Averager")
		self.option_menu2 = ttk.OptionMenu(self, self.variable2, *pavgr_list, command=self.select_point)

		for each in self.children:
			self.children[each].pack()
		self.location_entry = Entry(self)

	def select_file(self):
		my_filetypes = [('all files', '.*'), ('Comma Separated Value', '.csv')]
		self.location = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(),title="Please select a folder:")

	def select_url(self, event):    # obtains chosen url from the drop-down list
		self.url = event
		display = Label(self).pack() # displays the webpage

	def open_browser(self):     
		browser = "Firefox"
		location = "/bin/firefox"

		webbrowser.register(browser,None, webbrowser.BackgroundBrowser(location))
		webbrowser.get(browser).open(self.url)

	def select_point(self, event):    # obtains point-averager from the drop-down list
		self.point = event
		print(self.point)

	def run_program(self):
		def dothework(self):

			sine = []
			reader = csv.reader(csvfile)   # read content of file
			for row in reader:
				data = row
				sine.append(data)
				
			sine = np.concatenate(sine)  
			sine = np.array(sine).astype(np.float)    # convert to numpy array for processing
			xnew = np.linspace(sine.min(), sine.max(), len(sine))   # set axes
			
			fig, ax = plt.subplots()     # normalize display axes
			newax = ax.twiny()
				
			fig.subplots_adjust(bottom=0.20)

			newax.set_frame_on(True)
			newax.patch.set_visible(False)
			newax.xaxis.set_ticks_position('bottom')
			newax.xaxis.set_label_position('bottom')
			newax.spines['bottom'].set_position(('outward', 40))

			def point_averager(self, x, y):    # average points with selected averager
				N = self.point
				avgy = np.convolve(x, np.ones(N)/N, mode='valid')
				avgx = np.convolve(y, np.ones(N)/N, mode='valid')
				return avgx, avgy

			avgx, avgy = point_averager(self,xnew, sine)

			ax.plot(xnew, sine, 'r-')
			newax.plot(avgy, avgx, 'g-')

			ax.set_xlabel('Original Data')
			newax.set_xlabel('With N-Point Averager')

			plt.show()
		

		if str(self.location_entry.get()) is '': 
			with open(self.location, newline='') as csvfile:
				dothework(self)
		else:
			with open(str(self.location_entry.get()), newline='') as csvfile:
				dothework(self)

root = tk.Tk()
root.attributes('-topmost', 'true')
app = Application(root)
root.mainloop()


