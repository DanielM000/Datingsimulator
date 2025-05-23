import tkinter as tk
import random

# Ursprungliga karaktärer men nu med intressen och ointressen
karaktarer_ursprung = [
    {"namn": "Alex", "poang": 0, "intressen": ["Sport", "Resor"], "ointressen": ["TV-spel"]},
    {"namn": "Sam", "poang": 0, "intressen": ["Natur", "Matlagning"], "ointressen": ["Sport"]},
    {"namn": "Jamie", "poang": 0, "intressen": ["TV-spel", "Musik"], "ointressen": ["Natur"]},
    {"namn": "Taylor", "poang": 0, "intressen": ["Musik", "Resor"], "ointressen": ["Matlagning"]},
    {"namn": "Morgan", "poang": 0, "intressen": ["Matlagning", "Natur"], "ointressen": ["TV-spel"]},
    {"namn": "Jordan", "poang": 0, "intressen": ["Resor", "Sport"], "ointressen": ["Musik"]}
]

# Alla möjliga valalternativ och deras relaterade ämnen
val_dict = {
    "Ge en komplimang": ["Alla"],
    "Fråga om resor": ["Resor", "Natur"],
    "Prata om fotboll": ["Sport"],
    "Diskutera spelkonsoler": ["TV-spel"],
    "Prata om favoritartist": ["Musik"],
    "Dela recept": ["Matlagning"],
    "Prata om klimatet": ["Natur"],
    "Berätta om dig själv": [],
    "Fråga om favoritrestaurang": ["Matlagning", "Resor"],
    "Dela barndomsminne": [],
    "Fråga om sportintresse": ["Sport"],
    "Tipsa om Netflix-serier": ["Musik", "TV-spel"]
}

# Globala variabler
karaktarer = []
index = 0
val_frame = None
t = 12

# Skapa huvudfönster
root = tk.Tk()
root.title("Speeddating Simulator")
root.geometry("400x700")

# Etiketter för att visa info
namn_label = tk.Label(root, text="", font=("Helvetica", 16))
namn_label.pack(pady=15)

intressen_label = tk.Label(root, text="", font=("Helvetica", 12))
intressen_label.pack()

ointressen_label = tk.Label(root, text="", font=("Helvetica", 12))
ointressen_label.pack()

svar_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350)
svar_label.pack(pady=10)

label = tk.Label(root, font=("Helvetica", 12))
label.place(x=20, y=20)

# Funktion: Hantera val och poäng
def hantera_val(val):
    global index
    person = karaktarer[index]
    intressen = person["intressen"]
    ointressen = person["ointressen"]
    relaterade_amnen = val_dict[val]

    if "Alla" in relaterade_amnen or any(a in intressen for a in relaterade_amnen):
        person["poang"] += 1
        svar_label.config(text="Bra val!")
    elif any(a in ointressen for a in relaterade_amnen):
        person["poang"] -= 1
        svar_label.config(text="Det föll inte i smaken!")
    else:
        svar_label.config(text="Hmm, inte imponerad...")

# Funktion: Skapa valknappar
def visa_val():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    for val in val_dict:
        tk.Button(val_frame, text=val, width=45, command=lambda v=val: hantera_val(v)).pack(pady=2)

# Funktion: Timer för varje dejt
def countdown(count): 
    if index < len(karaktarer):
        label.config(text=f"🕒 {count} sek")
        if count > 0:
            root.after(1000, countdown, count - 1)
        else:
            byt_dejt()
    else:
        label.config(text="")

# Funktion: Starta dejt
def starta_dejt():
    global index, val_frame
    if val_frame:
        val_frame.destroy()
        svar_label.config(text="")

    if index < len(karaktarer):
        person = karaktarer[index]
        namn_label.config(text=f"Du dejtar {person['namn']}")
        intressen_label.config(text=f"Intressen: {', '.join(person['intressen'])}")
        ointressen_label.config(text=f"Ointresserad av: {', '.join(person['ointressen'])}")
        visa_val()
        countdown(t)
    else:
        visa_resultat()

# Funktion: Nästa dejt
def byt_dejt():
    global index
    index += 1
    starta_dejt()

# Funktion: Visa resultat
def visa_resultat():
    namn_label.config(text="Dejtingrundan är över!")
    intressen_label.config(text="")
    ointressen_label.config(text="")
    if val_frame:
        val_frame.destroy()

    bast = max(karaktarer, key=lambda p: p["poang"])
    poang_text = "\n".join([f"{p['namn']}: {p['poang']} poäng" for p in karaktarer])
    svar_label.config(text=f"Bäst matchade du med {bast['namn']}!\n\nPoäng:\n{poang_text}")

    # Skapa spela igen-knapp
    tk.Button(root, text="🔁 Spela igen", font=("Helvetica", 12, "bold"), bg="#ccf", command=spela_igen).pack(pady=20)

# Funktion: Återställ spelet
def spela_igen():
    global index, karaktarer
    index = 0
    karaktarer = [dict(p) for p in karaktarer_ursprung]
    for p in karaktarer:
        p["poang"] = 0
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget["text"] == "🔁 Spela igen":
            widget.destroy()
    starta_dejt()

# Starta spelet
spela_igen()

# Starta loopen
root.mainloop()