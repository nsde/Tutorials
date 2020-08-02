# GUIs (Graphical User Interface, dt. Grafische Benutzeroberfläche) mit TKINTER!

import tkinter

win = tkinter.Tk() # Fenster definieren
win.title('Mein Fenster') # Das Fenster benennen
win.geometry('300x300') # Fenstergröße in Pixel

text = tkinter.Label(win, text='Hallo!') # Text-Element definieren
text.pack() # Text erstellen

win.mainloop() # Fenster "erstellen" (ganz am Schluss schreiben!)
# Es ist etwas komplizierter, in einfach: hier sagen wir dem Programm, dass das Fenster "läuft" oder "aktiv" ist...
