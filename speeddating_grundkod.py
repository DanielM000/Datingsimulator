import tkinter as tk
import random
import time

# Karaktärer och deras namn
karaktarer = [
    {"namn": "Alex", "poang": 0, "intressen": "Sport"},
    {"namn": "Sam", "poang": 0, "intressen": "Natur"},
    {"namn": "Jamie", "poang": 0, "intressen": "TV-spel"}
]

# Globala variabler
index = 0
val_frame = None
t = 8

# Skapa huvudfönster
root = tk.Tk()
root.title("Speeddating Simulator")
root.geometry("330x600")

namn_label = tk.Label(root, text="", font=("Helvetica", 16))
namn_label.pack(pady=15)

intressen_label = tk.Label(root, text="", font=("Helvetica", 14))
intressen_label.pack(pady=10)

svar_label = tk.Label(root, text="", font=("Helvetica", 12))
svar_label.pack(pady=10)

label = tk.Label(root)
label.place(x=35, y=15)

# Funktion: Hantera val
def val1(): # Ge en komplimang
    if index == 0:
        karaktarer[index]["poang"] += 1
        svar_label.config(text="Bra val!")
    elif index == 1:
        karaktarer[index]["poang"] += 1
        svar_label.config(text="Bra val!")
    elif index == 2:
        karaktarer[index]["poang"] += 0
        svar_label.config(text="Hmm, inte imponerad...")

def val2(): # Fråga om väder
    if index == 0:
        karaktarer[index]["poang"] += 0
        svar_label.config(text="Hmm, inte imponerad...")
    elif index == 1:
        karaktarer[index]["poang"] += 1
        svar_label.config(text="Bra val!")
    elif index == 2:
        karaktarer[index]["poang"] -= 1
        svar_label.config(text="Det föll inte i smaken!")

def val3(): # Prata om dig själv
    if index == 0:
        karaktarer[index]["poang"] -= 1
        svar_label.config(text="Det föll inte i smaken!")
    elif index == 1:
        karaktarer[index]["poang"] -= 1
        svar_label.config(text="Det föll inte i smaken!")
    elif index == 2:
        karaktarer[index]["poang"] += 0
        svar_label.config(text="Hmm, inte imponerad...")

def val4(): # Prata om fotboll
    if index == 0:
        karaktarer[index]["poang"] += 1
        svar_label.config(text="Bra val!")
    elif index == 1:
        karaktarer[index]["poang"] += 0
        svar_label.config(text="Hmm, inte imponerad...")
    elif index == 2:
        karaktarer[index]["poang"] -= 1
        svar_label.config(text="Det föll inte i smaken!")

def countdown(count): 
    label['text'] = count
    if count > 0 and index < len(karaktarer):
        root.after(1000, countdown, count-1)
    elif count <= 0  and index < len(karaktarer):
        countdown(8)
    else:
        label.destroy()

# Funktion: Visa valknappar
def visa_val():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    tk.Button(val_frame, text="Ge en komplimang", command=val1).pack(pady=5)
    tk.Button(val_frame, text="Fråga om väder", command=val2).pack(pady=5)
    tk.Button(val_frame, text="Prata om dig själv", command=val3).pack(pady=5)
    tk.Button(val_frame, text="Prata om fotboll", command=val4).pack(pady=5)

# Funktion: Starta dejt
def starta_dejt():
    global index, val_frame
    if val_frame:
        val_frame.destroy()
        svar_label.config(text="")

    if index < len(karaktarer):
        person = karaktarer[index]
        namn_label.config(text=f"Du dejtar {person['namn']}")
        intressen_label.config(text=f"Intressen: {person['intressen']}")
        visa_val()
        root.after(8000, byt_dejt)  # 8 sekunder per dejt
    else:
        visa_resultat()
        intressen_label.destroy()

# Funktion: Byt till nästa dejt
def byt_dejt():
    global index
    index += 1
    starta_dejt()

# Funktion: Visa resultat
def visa_resultat():
    namn_label.config(text="Dejtingrundan är över!")
    if val_frame:
        val_frame.destroy()

    # Hitta bästa match
    bast = max(karaktarer, key=lambda p: p["poang"])
    svar_label.config(text=f"Bäst matchade du med {bast['namn']}! ({bast['poang']} poäng)")

# Starta första dejten
starta_dejt()

countdown(8)

# Starta loopen
root.mainloop()