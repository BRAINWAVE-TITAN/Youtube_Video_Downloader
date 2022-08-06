import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def buttons():

	link = Label(root,text="YouTube link :",bg="red",pady=5,padx=5)
	link.grid(row=2,column=0,pady=20,padx=5)
 
	root.link = Entry(root,width=27,text=video_Link)
	root.link.grid(row=2,column=1,pady=5,padx=5)
 
	saveas = Label(root,text="Save As :",bg="green",pady=5,padx=9)
	saveas.grid(row=3,column=0,pady=5,padx=5)
 
	root.saveas = Entry(root,width=27,textvariable=Path)
	root.saveas.grid(row=3,column=1,pady=5,padx=5)
 
	browse = Button(root,text="Browse",command=Browse,width=6,relief=GROOVE)
	browse.grid(row=3,column=2,pady=1,padx=1)
 
	download = Button(root,text="Download Video",command=Download,width=20,pady=10,padx=15,relief=GROOVE)
	download.grid(row=4,column=1,pady=20,padx=20)


def Browse():

	Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
	Path.set(Directory)

def Download():
	Youtube_link = video_Link.get()
	Folder = Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.get_highest_resolution()
	videoStream.download(Folder)
	messagebox.showinfo("Download Successfully","Saved At\n"+ Folder)

root = tk.Tk()

root.geometry("520x200")
root.resizable(False, False)
root.title("YouTube Downloader")
root.config(background="PaleGreen")

video_Link = StringVar()
Path = StringVar()

buttons()

root.mainloop()
