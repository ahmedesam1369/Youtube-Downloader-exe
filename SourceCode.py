from os import stat
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from pytube import Playlist
hawa = Tk()
hawa.title("HAWA Downloader << Best Youtube download App in The World >>")
hawa.resizable(False, False)
hawa.geometry("800x600")
welcomelabel = Label(hawa,text="Welcome You In ESAM Youtube Downloader",height=3,font=('Arial',20),fg='#00aecd')
welcomelabel.pack()
number1label = Label(hawa,text="Enter Youtube Video Link",height=2,font=('Arial',15))
number1label.pack()
number1entry = Entry(hawa,width=88,font=("Arial",10))
number1entry.pack()
def finish():
    messagebox.showinfo("Alert",message="Download Complete")
    number1entry.delete(0, END)
    number2entry.delete(0, END)
    dl_label.pack_forget()
    dl_label2.pack_forget()
def getpath():
    file1 = filedialog.askdirectory()
    return file1
global al_label
al_label = Label(hawa,text= "Enter a valid URL in the appropriate field" ,height=2,font=('Arial',17),fg='red')
global dl_label
dl_label = Label(hawa,text= "Downloading.....wait until download complete" ,height=2,font=('Arial',17),fg='green')
def videodownload():
        video_link = number1entry.get()
        if  video_link =='' or video_link[0:29] != 'https://www.youtube.com/watch':
            al_label.pack()
            al_label2.pack_forget()
        else:
            dl_label.pack()
            al_label.pack_forget()
            al_label2.pack_forget()
            video = YouTube(video_link)
            x = getpath()
            if x== '':
                 messagebox.showinfo("Alert",message="Select a path to start download")
                 dl_label.pack_forget()
            else:
                video.streams.get_highest_resolution().download(output_path= x)
                video.register_on_complete_callback(finish())
but1 =  Button(text="Download Single Video",font=('Arial',15),height=2,bg="#dadce0",fg="#095efb",borderwidth=0,command=videodownload)
but1.pack()
orlabel = Label(hawa,text="OR",height=2,font=('Arial',17),fg='#0061ff')
orlabel.pack()
number2label = Label(hawa,text="Enter  Playlist Link",height=3,font=('Arial',15))
number2label.pack()
number2entry = Entry(hawa,width=88,font=("Arial",10))
number2entry.pack()
global al_label2
al_label2 = Label(hawa,text= "Enter a valid URL in the appropriate field" ,height=2,font=('Arial',17),fg='red')
global dl_label2
dl_label2 = Label(hawa,text= "Downloading.....wait until download complete" ,height=2,font=('Arial',17),fg='green')
def playlistdownload():
    playlist_link = number2entry.get()
    if  playlist_link =='' or playlist_link[0:23] != 'https://www.youtube.com':
        al_label2.pack()
        al_label.pack_forget()          
    else: 
        dl_label2.pack()
        al_label2.pack_forget()
        al_label.pack_forget()
        playlist = Playlist(playlist_link)
        x = getpath()
        if x== '':
            messagebox.showinfo("Alert",message="Select a path to start download")
            dl_label2.pack_forget()
        else:
            for video in playlist.videos:
                video.streams.get_highest_resolution().download(output_path= x)
            video.register_on_complete_callback(finish())
but2 =  Button(text="Download Whole Playlist",font=('Arial',15),height=2, bg="#dadce0",fg="#095efb",borderwidth=0,command=playlistdownload)
but2.pack()
hawa.mainloop()

