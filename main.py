import tkinter as tk
import tkinter.font as tkFont
import cryptographie as crypt

root = tk.Tk() # Création de la fenêtre
frame = tk.Frame(root)

# Configuration de la fenêtre
root.attributes('-fullscreen',True)
root.bind('<Escape>',lambda e: Retour())
root.title('Machine de cryptographie')
root.config(bg='black')

# Polices d'écriture
Title_font = tkFont.Font(family='Helvetica', size=36, weight='bold')
Desc_font = tkFont.Font(family='Helvetica', size=18)

# Affichage
def Affichage():
    """Affiche le titre et la description de la fenêtre."""
    Title = tk.Label(text = "Machine de cryptographie", fg='white', bg='black', font=Title_font)
    Title.pack(pady=40)
    Desc = tk.Label(text = "Cette machine vous permet de crypter et décrypter des messages !", fg='white', bg='black', font=Desc_font)
    Desc.pack(pady=50)

def Bouton():
    """Affiche les boutons d'accueil."""
    root.bind('<F1>',lambda e:Code_Cesar())
    bt1 = tk.Button(root, text="Code de César [F1]", command=lambda:Code_Cesar())
    bt1.pack(pady=25)
    root.bind('<F2>',lambda e:Code_Vigenere())
    bt2 = tk.Button(root, text="Code Vigenère [F2]", command=lambda:Code_Vigenere())
    bt2.pack(pady=25)
    root.bind('<F3>',lambda e:Code_Hill())
    bt3 = tk.Button(root, text="Chiffre de Hill [F3]", command=lambda:Code_Hill())
    bt3.pack(pady=25)
    root.bind('<F4>',lambda e:Code_Morse())
    bt4 = tk.Button(root, text="Alphabet Morse [F4]", command=lambda:Code_Morse())
    bt4.pack(pady=25)
    root.bind('<F5>',lambda e:Code_XOR())
    bt5 = tk.Button(root, text="Cryptage XOR [F5]", command=lambda:Code_XOR())
    bt5.pack(pady=25)

# Retour
def Retour():
    """Renvoie la fenêtre du départ."""
    for widget in root.winfo_children():
        widget.destroy()
    root.unbind('<F1>')
    root.unbind('<F2>')
    root.unbind('<F3>')
    Affichage()
    Bouton()
    
def Reset():
    """Renvoie la fenêtre de base."""
    for widget in root.winfo_children():
        widget.destroy()
    root.unbind('<F1>')
    root.unbind('<F2>')
    root.unbind('<F3>')
    root.unbind('<F4>')
    Affichage()

# =============================================================================
# Cesar
# =============================================================================

def Code_Cesar():
    """Affiche la fenêtre du Cesar."""
    Reset()
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack()
    Entre2 = tk.Entry(width=50)
    Entre2.insert(0,"Votre décalage clé ...")
    Entre2.pack()  
    root.bind('<F1>',lambda e:Encrypt_Cesar(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_Cesar(Entre1,Entre2,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Cesar(Entre1,Entre2,reponse))
    bouton.pack(pady=25)
    bouton1 = tk.Button(root, text="Décrypter [F2]", command=lambda:Decrypt_Cesar(Entre1,Entre2,reponse))
    bouton1.pack()
    reponse = tk.Label(text="Message codé en César...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil [Esc]", command=Retour)
    retour.pack(pady=25)
    
def Encrypt_Cesar(Entre1,Entre2,reponse):
    """Appelle la fonction Encrypt de Cesar."""
    Message = Entre1.get()
    Cle = int(Entre2.get())
    reponse.config(text=crypt.Cesar(Message.upper(),Cle).encrypt())

def Decrypt_Cesar(Entre1,Entre2,reponse):
    """Appelle la fonction Decrypt de Cesar."""
    Message = Entre1.get()
    Cle = int(Entre2.get())
    reponse.config(text=crypt.Cesar(Message.upper(),Cle).decrypt())

# =============================================================================
# Vigenere
# =============================================================================

def Code_Vigenere():
    """Affiche la fenêtre du Vigenere."""
    Reset()
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack()
    Entre2 = tk.Entry(width=50)
    Entre2.insert(0,"Votre message clé ...")
    Entre2.pack()
    root.bind('<F1>',lambda e:Encrypt_Vigenere(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_Vigenere(Entre1,Entre2,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Vigenere(Entre1,Entre2,reponse))
    bouton.pack(pady=25)
    bouton1 = tk.Button(root, text="Décrypter [F2]", command=lambda:Decrypt_Vigenere(Entre1,Entre2,reponse))
    bouton1.pack()
    reponse = tk.Label(text="Message codé en Vigenère...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil [Esc]", command=Retour)
    retour.pack(pady=25)

def Encrypt_Vigenere(Entre1,Entre2,reponse):
    """Appelle la fonction Encrypt de Vigenere."""
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text=crypt.Vigenere(Message.upper(),Cle.upper()).encrypt())

def Decrypt_Vigenere(Entre1,Entre2,reponse):
    """Appelle la fonction Decrypt de Vigenere."""
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text=crypt.Vigenere(Message.upper(),Cle.upper()).decrypt())

# =============================================================================
# Hill
# =============================================================================
  
def Code_Hill():
    """Affiche la fenêtre du Hill."""
    Reset()
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack(pady=10)
    Matrice = tk.Label(text = "Votre matrice clé :", fg='white', bg='black', font=Desc_font)
    Matrice.pack(padx=10, pady=5)
    zone = tk.Frame(root,bg='black')
    zone.pack(padx=10,pady=10)
    Entre2 = tk.Entry(zone, width=5, justify='center')
    Entre2.grid(row=0,column=0,padx=10,pady=10)
    Entre3 = tk.Entry(zone, width=5, justify='center')
    Entre3.grid(row=0,column=1,padx=10,pady=10)
    Entre4 = tk.Entry(zone, width=5, justify='center')
    Entre4.grid(row=1,column=0,padx=10,pady=10)
    Entre5 = tk.Entry(zone, width=5, justify='center')
    Entre5.grid(row=1,column=1,padx=10,pady=10)
    root.bind('<F1>',lambda e:Encrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    root.bind('<F2>',lambda e:Decrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    bouton.pack(pady=25)
    bouton1 = tk.Button(root, text="Décrypter [F2]", command=lambda:Decrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    bouton1.pack()
    reponse = tk.Label(text="Message codé en Hill...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil [Esc]", command=Retour)
    retour.pack(pady=25)

def Encrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse):
    """Appelle la fonction Encrypt de Hill."""
    Message = Entre1.get()
    Cle = [[int(Entre2.get()),int(Entre3.get())],[int(Entre4.get()),int(Entre5.get())]]
    reponse.config(text=crypt.Hill(Message.upper(),Cle).encrypt())
    
def Decrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse):
    """Appelle la fonction Decrypt de Hill."""
    Message = Entre1.get()
    Cle = [[int(Entre2.get()),int(Entre3.get())],[int(Entre4.get()),int(Entre5.get())]]
    reponse.config(text=crypt.Hill(Message.upper(),Cle).decrypt())

# =============================================================================
# MORSE
# =============================================================================

def Code_Morse():
    """Affiche la fenêtre du Morse."""
    Reset()
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack() 
    root.bind('<F1>',lambda e:Encrypt_Morse(Entre1,reponse))
    root.bind('<F2>',lambda e:Decrypt_Morse(Entre1,reponse))
    root.bind('<F3>',lambda e:Read_Morse(Entre1,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Morse(Entre1,reponse))
    bouton.pack(pady=10)
    bouton1 = tk.Button(root, text="Décrypter [F2]", command=lambda:Decrypt_Morse(Entre1,reponse))
    bouton1.pack(pady=10)
    bouton2 = tk.Button(root, text="Lire [F3]", command=lambda:Read_Morse(Entre1,reponse))
    bouton2.pack(pady=10)
    reponse = tk.Label(text='Message "codé" en Morse...', fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil [Esc]", command=Retour)
    retour.pack(pady=25)
    
def Encrypt_Morse(Entre1,reponse):
    """Appelle la fonction Encrypt de Morse."""
    Message = Entre1.get()
    reponse.config(text=crypt.Morse(Message.upper()).encrypt())

def Decrypt_Morse(Entre1,reponse):
    """Appelle la fonction Decrypt de Morse."""
    Message = Entre1.get() + " "
    reponse.config(text=crypt.Morse(Message).decrypt())
    
def Read_Morse(Entre1,reponse):
    """Appelle la fonction Play_sound de Morse."""
    Message = Entre1.get() + " "
    reponse.config(text=crypt.Morse(Message).Play_sound())
    
# =============================================================================
# XOR
# =============================================================================

def Code_XOR():
    """Affiche la fenêtre du XOR."""
    Reset()
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack()
    Entre2 = tk.Entry(width=50)
    Entre2.insert(0,"Votre message clé ...")
    Entre2.pack()
    root.bind('<F1>',lambda e:Encrypt_XOR(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_XOR(Entre1,Entre2,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_XOR(Entre1,Entre2,reponse))
    bouton.pack(pady=25)
    bouton1 = tk.Button(root, text="Décrypter [F2]", command=lambda:Decrypt_XOR(Entre1,Entre2,reponse))
    bouton1.pack()
    reponse = tk.Label(text="Message codé en XOR ...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil [Esc]", command=Retour)
    retour.pack(pady=25)

def Encrypt_XOR(Entre1,Entre2,reponse):
    """Appelle la fonction Encrypt de XOR."""
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text= crypt.XOR(Message,Cle.upper()).encrypt())

def Decrypt_XOR(Entre1,Entre2,reponse):
    """Appelle la fonction Decrypt de XOR."""
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text=crypt.XOR(Message,Cle.upper()).decrypt())


# Lancement de la fenêtre
Retour()

root.mainloop()
