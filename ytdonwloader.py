from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ''


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        patherror.config(text=Folder_Name,fg="green")

    else:
        patherror.config(text="please select folder!!",fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytderror.config(text="")
        yt = YouTube(url)

        if (choice == choises [0]):
            select=yt.streams.filter(progressive = True).first()

        elif (choice == choises[1]):
            select = yt.streams.filter (progressive=True, file_extension='mp4').last

        elif (choice == choises [2]):
            select=yt.streams.filter (only_audio=True) . first ()

        else:
            ytderror.config (text="Paste Link again!!", fg="red")


    select.download(Folder_Name)
    ytderror.config(text="complete",fg="green")

root = Tk()
root.title("YT downloader")
root.geometry("350x400")
root.columnconfigure(0, weight = 1)

ytdlabel = Label(root, text="ENTER THE URL", font=(15))
ytdlabel.grid()


ytdentryvar = StringVar()
ytdEntry = Entry(root,width = 50,textvariable = ytdentryvar)
ytdEntry.grid()

ytderror = Label(root, text="error msg",fg = "red")
ytderror.grid()


ytdsafelabel = Label(root, text="Select Folder",font=(15))
ytdsafelabel.grid()


saveentry = Button(root, width = 10,bg = "red",fg = "white", text="choose folder",command = openLocation)
saveentry.grid()


patherror = Label(root, text="error path",fg = "red")
patherror.grid()


ytdvidquality = Label(root, text="Select Video Quality",font=(15))
ytdvidquality.grid()

choises = ["720p","144p","only audio"]
ytdchoices = ttk.Combobox(root, values=choises)
ytdchoices.grid()


downloadbtn = Button(root, width = 10,bg = "red",fg = "white", text="DOWNLOAD",command = DownloadVideo)
downloadbtn.grid()

creator = Label(root, text="NEXIAN32",font=(20),padx=10)
creator.grid()

root.mainloop()