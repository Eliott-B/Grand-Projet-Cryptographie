import tkinter as tk
from tkinter import ttk
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
def General():
    """Affiche les éléments généraux de la fenêtre."""
    Title = tk.Label(text = "Machine de cryptographie", fg='white', bg='black', font=Title_font)
    Title.pack(pady=40)

def Accueil():
    """Affiche les boutons d'accueil et la description."""
    desc = tk.Label(text = "Cette machine vous permet de crypter et décrypter des messages !", fg='white', bg='black', font=Desc_font)
    desc.pack(pady=50)
    
    root.bind('<F1>',lambda e:Code_Cesar())
    bt1_icon = tk.PhotoImage(file='./assets/icons8-couronne-de-laurier-48.png')
    bt1 = ttk.Button(root, image=bt1_icon, text="Code César [F1]", compound=tk.TOP, command=lambda:Code_Cesar())
    bt1.pack(pady=20, ipadx=5, ipady=5)
    bt1.image = bt1_icon
    
    root.bind('<F2>',lambda e:Code_Vigenere())
    bt2_icon = tk.PhotoImage(file='./assets/icons8-pourcentage-2-60.png')
    bt2 = ttk.Button(root, image=bt2_icon, text="Code Vigenère [F2]", compound=tk.TOP, command=lambda:Code_Vigenere())
    bt2.pack(pady=20, ipadx=5, ipady=5)
    bt2.image = bt2_icon
    
    root.bind('<F3>',lambda e:Code_Hill())
    bt3_icon = tk.PhotoImage(file='./assets/icons8-matrix-60.png')
    bt3 = ttk.Button(root, image=bt3_icon, text="Chiffre de Hill [F3]", compound=tk.TOP, command=lambda:Code_Hill())
    bt3.pack(pady=20, ipadx=5, ipady=5)
    bt3.image = bt3_icon
    
    root.bind('<F4>',lambda e:Code_Morse())
    bt4_icon = tk.PhotoImage(file='./assets/icons8-morse-code-48.png')
    bt4 = ttk.Button(root, image=bt4_icon, text="Alphabet Morse [F4]", compound=tk.TOP, command=lambda:Code_Morse())
    bt4.pack(pady=20, ipadx=5, ipady=5)
    bt4.image = bt4_icon
    
    root.bind('<F5>',lambda e:Code_XOR())
    bt5_icon = tk.PhotoImage(file='./assets/icons8-binary-code-60.png')
    bt5 = ttk.Button(root, image=bt5_icon, text="Cryptage XOR [F5]", compound=tk.TOP, command=lambda:Code_XOR())
    bt5.pack(pady=20, ipadx=5, ipady=5)
    bt5.image = bt5_icon


# Retour
def Retour():
    """Renvoie la fenêtre du départ."""
    for widget in root.winfo_children():
        widget.destroy()
    root.unbind('<F1>')
    root.unbind('<F2>')
    root.unbind('<F3>')
    General()
    Accueil()
    
def Reset():
    """Renvoie la fenêtre de base."""
    for widget in root.winfo_children():
        widget.destroy()
    root.unbind('<F1>')
    root.unbind('<F2>')
    root.unbind('<F3>')
    root.unbind('<F4>')
    root.unbind('<F5>')
    General()

# =============================================================================
# Cesar
# =============================================================================

def Code_Cesar():
    """Affiche la fenêtre du Cesar."""
    Reset()
    desc = tk.Label(text = "Le Code César est un chiffrement qui décale chaque lettre du message par le décalage donné.\n"
                    "La clé de décalage devrait être comprise entre 1 et 25.", fg='white', bg='black', font=Desc_font)
    desc.pack(pady=30)
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack()
    Entre2 = tk.Entry(width=50)
    Entre2.insert(0,"Votre décalage clé ...")
    Entre2.pack()  
    root.bind('<F1>',lambda e:Encrypt_Cesar(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_Cesar(Entre1,Entre2,reponse))
    
    bouton_icon = tk.PhotoImage(file='./assets/icons8-verrouiller-2-24.png')
    bouton = ttk.Button(root, image=bouton_icon, text="Crypter [F1]", compound=tk.LEFT, command=lambda:Encrypt_Cesar(Entre1,Entre2,reponse))
    bouton.pack(pady=25, ipadx=5, ipady=5)
    bouton.image = bouton_icon
    bouton1_icon = tk.PhotoImage(file='./assets/icons8-clés-2-24.png')
    bouton1 = ttk.Button(root, image=bouton1_icon, text="Décrypter [F2]", compound=tk.LEFT, command=lambda:Decrypt_Cesar(Entre1,Entre2,reponse))
    bouton1.pack(ipadx=5, ipady=5)
    bouton1.image = bouton1_icon
    
    reponse = tk.Label(text="Message codé en César...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour_icon = tk.PhotoImage(file='./assets/icons8-accueil-24.png')
    retour = ttk.Button(root, image=retour_icon, text="Retour à l'accueil [Esc]", compound=tk.LEFT, command=Retour)
    retour.pack(pady=25, ipadx=5, ipady=5)
    retour.image = retour_icon
    
    
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
    """Affiche la fenêtre du Vigenère."""
    Reset()
    desc = tk.Label(text = "Le Code Vigenère est un chiffrement qui décale chaque lettre du message grâce au message clé.\n"
                    "Le message clé ne doit pas être constitué d'espaces, de chiffres ou de caractères spéciaux.", fg='white', bg='black', font=Desc_font)
    desc.pack(pady=30)
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack()
    Entre2 = tk.Entry(width=50)
    Entre2.insert(0,"Votre message clé ...")
    Entre2.pack()
    root.bind('<F1>',lambda e:Encrypt_Vigenere(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_Vigenere(Entre1,Entre2,reponse))

    bouton_icon = tk.PhotoImage(file='./assets/icons8-verrouiller-2-24.png')
    bouton = ttk.Button(root, image=bouton_icon, text="Crypter [F1]", compound=tk.LEFT, command=lambda:Encrypt_Vigenere(Entre1,Entre2,reponse))
    bouton.pack(pady=25, ipadx=5, ipady=5)
    bouton.image = bouton_icon
    bouton1_icon = tk.PhotoImage(file='./assets/icons8-clés-2-24.png')
    bouton1 = ttk.Button(root, image=bouton1_icon, text="Décrypter [F2]", compound=tk.LEFT, command=lambda:Decrypt_Vigenere(Entre1,Entre2,reponse))
    bouton1.pack(ipadx=5, ipady=5)
    bouton1.image = bouton1_icon
    
    reponse = tk.Label(text="Message codé en Vigenère...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour_icon = tk.PhotoImage(file='./assets/icons8-accueil-24.png')
    retour = ttk.Button(root, image=retour_icon, text="Retour à l'accueil [Esc]", compound=tk.LEFT, command=Retour)
    retour.pack(pady=25, ipadx=5, ipady=5)
    retour.image = retour_icon


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
    desc = tk.Label(text = "Le Chiffre de Hill est un chiffrement qui crypte un message grâce à une matrice clé.\n\n"
                    "Cette matrice clé doit être composée exclusivement d'entiers positifs.\n"
                    "Son déterminant doit être premier avec 26 et doit permettre d'obtenir une matrice inversible.\n\n"
                    "Si le message à coder est une chaîne impaire de caractères, un A sera automatiquement ajouté à la fin", fg='white', bg='black', font=Desc_font)
    desc.pack(pady=30)
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
    
    bouton_icon = tk.PhotoImage(file='./assets/icons8-verrouiller-2-24.png')
    bouton = ttk.Button(root, image=bouton_icon, text="Crypter [F1]", compound=tk.LEFT, command=lambda:Encrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    bouton.pack(pady=25, ipadx=5, ipady=5)
    bouton.image = bouton_icon
    bouton1_icon = tk.PhotoImage(file='./assets/icons8-clés-2-24.png')
    bouton1 = ttk.Button(root, image=bouton1_icon, text="Décrypter [F2]", compound=tk.LEFT, command=lambda:Decrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    bouton1.pack(ipadx=5, ipady=5)
    bouton1.image = bouton1_icon
    
    reponse = tk.Label(text="Message codé en Hill...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour_icon = tk.PhotoImage(file='./assets/icons8-accueil-24.png')
    retour = ttk.Button(root, image=retour_icon, text="Retour à l'accueil [Esc]", compound=tk.LEFT, command=Retour)
    retour.pack(pady=25, ipadx=5, ipady=5)
    retour.image = retour_icon


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
    desc = tk.Label(text = "L'alphabet Morse transcrit un message en signaux courts et longs.\n"
                    "Signal court : .\nSignal long : -\nLes lettres sont séparées par des espaces et les mots par un slash.", fg='white', bg='black', font=Desc_font)
    desc.pack(pady=30)
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack() 
    root.bind('<F1>',lambda e:Encrypt_Morse(Entre1,reponse))
    root.bind('<F2>',lambda e:Decrypt_Morse(Entre1,reponse))
    root.bind('<F3>',lambda e:Read_Morse(Entre1,reponse))
    
    bouton_icon = tk.PhotoImage(file='./assets/icons8-verrouiller-2-24.png')
    bouton = ttk.Button(root, image=bouton_icon, text="Crypter [F1]", compound=tk.LEFT, command=lambda:Encrypt_Morse(Entre1,reponse))
    bouton.pack(pady=25, ipadx=5, ipady=5)
    bouton.image = bouton_icon
    bouton1_icon = tk.PhotoImage(file='./assets/icons8-clés-2-24.png')
    bouton1 = ttk.Button(root, image=bouton1_icon, text="Décrypter [F2]", compound=tk.LEFT, command=lambda:Decrypt_Morse(Entre1,reponse))
    bouton1.pack(ipadx=5, ipady=5)
    bouton1.image = bouton1_icon
    
    reponse = tk.Label(text='Message transcrit en Morse...', fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour_icon = tk.PhotoImage(file='./assets/icons8-accueil-24.png')
    retour = ttk.Button(root, image=retour_icon, text="Retour à l'accueil [Esc]", compound=tk.LEFT, command=Retour)
    retour.pack(pady=25, ipadx=5, ipady=5)
    retour.image = retour_icon
    
    
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
    desc = tk.Label(text = "Le cryptage XOR est un chiffrement qui réalise un OUX logique entre le message et le message clé.", fg='white', bg='black', font=Desc_font)
    desc.pack(pady=30)
    Entre1 = tk.Entry(width=50)
    Entre1.insert(0,"Votre message ...")
    Entre1.pack()
    Entre2 = tk.Entry(width=50)
    Entre2.insert(0,"Votre message clé ...")
    Entre2.pack()
    root.bind('<F1>',lambda e:Encrypt_XOR(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_XOR(Entre1,Entre2,reponse))
    
    bouton_icon = tk.PhotoImage(file='./assets/icons8-verrouiller-2-24.png')
    bouton = ttk.Button(root, image=bouton_icon, text="Crypter [F1]", compound=tk.LEFT, command=lambda:Encrypt_XOR(Entre1,Entre2,reponse))
    bouton.pack(pady=25, ipadx=5, ipady=5)
    bouton.image = bouton_icon
    bouton1_icon = tk.PhotoImage(file='./assets/icons8-clés-2-24.png')
    bouton1 = ttk.Button(root, image=bouton1_icon, text="Décrypter [F2]", compound=tk.LEFT, command=lambda:Decrypt_XOR(Entre1,Entre2,reponse))
    bouton1.pack(ipadx=5, ipady=5)
    bouton1.image = bouton1_icon
    
    reponse = tk.Label(text="Message codé en XOR ...", fg='yellow', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour_icon = tk.PhotoImage(file='./assets/icons8-accueil-24.png')
    retour = ttk.Button(root, image=retour_icon, text="Retour à l'accueil [Esc]", compound=tk.LEFT, command=Retour)
    retour.pack(pady=25, ipadx=5, ipady=5)
    retour.image = retour_icon


def Encrypt_XOR(Entre1,Entre2,reponse):
    """Appelle la fonction Encrypt de XOR."""
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text= crypt.XOR(Message,Cle).encrypt())

def Decrypt_XOR(Entre1,Entre2,reponse):
    """Appelle la fonction Decrypt de XOR."""
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text=crypt.XOR(Message,Cle).decrypt())


# Lancement de la fenêtre
Retour()

root.mainloop()


"""
Crédits icônes :
    
Icons8 : https://icons8.com/

https://icones8.fr/icon/81040/couronne-de-laurier : Couronne de laurier icon by Icons8
https://icones8.fr/icon/79195/pourcentage-2 : Pourcentage 2 icon by Icons8
https://icones8.fr/icon/c2r66dIcxZhq/matrix : Matrix icon by Icons8
https://icones8.fr/icon/DfKqJP7BNaht/morse-code : Morse Code icon by Icons8
https://icones8.fr/icon/tTDtwd7sCbQc/binary-code : Binary Code icon by Icons8

https://icones8.fr/icon/86120/verrouiller-2 : Verrouiller 2 icon by Icons8
https://icones8.fr/icon/101928/cl%C3%A9s-2 : Clés 2 icon by Icons8
https://icones8.fr/icon/86527/accueil : Accueil icon by Icons8
"""
