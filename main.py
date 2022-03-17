import tkinter as tk
import tkinter.font as tkFont
import cryptographie as crypt

root = tk.Tk() # Création de la fenêtre
frame = tk.Frame(root)

# Configuration de la fenêtre
root.attributes('-fullscreen',True)
root.bind('<Escape>',lambda e:root.destroy())
root.title('Machine de cryptographie.')
root.config(bg='black')

# Police d'écriture
Title_font = tkFont.Font(family='Helvetica', size=36, weight='bold')
Desc_font = tkFont.Font(family='Helvetica', size=18)

# Affichage
def Affichage():
    """Affiche le titre et la description de la fenêtre."""
    Title = tk.Label(text = "Machine de cryptographie.", fg='white', bg='black', font=Title_font)
    Title.pack(pady=25)
    Desc = tk.Label(text = "Cette machine vous permet de crypter et décrypter des messages !", fg='white', bg='black', font=Desc_font)
    Desc.pack(pady=50)
    bt1 = tk.Button(root, text="Crypter César", command=lambda:Code_Cesar(bt1,bt2,bt3))
    bt1.pack(pady=25)
    bt2 = tk.Button(root, text="Crypter Vigenere", command=lambda:Code_Vigenere(bt1,bt2,bt3))
    bt2.pack(pady=25)
    bt3 = tk.Button(root, text="Crypter Hill", command=lambda:Code_Hill(bt1,bt2,bt3))
    bt3.pack(pady=25)

# Retour au début
def Retour():
    """Renvoie la fenêtre du départ."""
    for widget in root.winfo_children():
        widget.destroy()
    Affichage()

# César
def Code_Cesar(bt1,bt2,bt3):
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    Entre1 = tk.Entry()
    Entre1.insert(0,"Votre message")
    Entre1.pack()
    Entre2 = tk.Entry()
    Entre2.insert(0,"Votre décalage clé")
    Entre2.pack()  
    root.bind('<F1>',lambda e:Encrypt_Cesar(Entre1,Entre2,reponse))
    # root.bind('<F2>',lambda e:Decrypt_Cesar(Entre1,Entre2,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Cesar(Entre1,Entre2,reponse))
    bouton.pack(pady=25)
    reponse = tk.Label(text="Message codé en César ...", fg='white', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil", command=Retour)
    retour.pack(pady=25)
    
def Encrypt_Cesar(Entre1,Entre2,reponse):
    Message = Entre1.get()
    Cle = int(Entre2.get())
    reponse.config(text=crypt.Cesar(Message.upper(),Cle).encrypt())

# Vigenere
def Code_Vigenere(bt1,bt2,bt3):
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    Entre1 = tk.Entry()
    Entre1.insert(0,"Votre message")
    Entre1.pack()
    Entre2 = tk.Entry()
    Entre2.insert(0,"Votre message clé")
    Entre2.pack()
    root.bind('<F1>',lambda e:Encrypt_Vigenere(Entre1,Entre2,reponse))
    root.bind('<F2>',lambda e:Decrypt_Vigenere(Entre1,Entre2,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Vigenere(Entre1,Entre2,reponse))
    bouton.pack(pady=25)
    bouton1 = tk.Button(root, text="Décrypter [F2]", command=lambda:Decrypt_Vigenere(Entre1,Entre2,reponse))
    bouton1.pack()
    reponse = tk.Label(text="Message codé en Vigenère ...", fg='white', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil", command=Retour)
    retour.pack(pady=25)

def Encrypt_Vigenere(Entre1,Entre2,reponse):
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text=crypt.Vigenere(Message.upper(),Cle.upper()).encrypt())

def Decrypt_Vigenere(Entre1,Entre2,reponse):
    Message = Entre1.get()
    Cle = Entre2.get()
    reponse.config(text=crypt.Vigenere(Message.upper(),Cle.upper()).decrypt())

# Hill
  
def Code_Hill(bt1,bt2,bt3):
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    Entre1 = tk.Entry()
    Entre1.insert(0,"Votre message")
    Entre1.pack()
    Matrice = tk.Label(text = "Votre matrice :", fg='white', bg='black', font=Desc_font)
    Matrice.pack()
    zone = tk.Frame(root,bg='black')
    zone.pack(padx=10,pady=10)
    Entre2 = tk.Entry(zone, width=5)
    Entre2.grid(row=0,column=0,padx=10)
    Entre3 = tk.Entry(zone, width=5)
    Entre3.grid(row=0,column=1,padx=10)
    Entre4 = tk.Entry(zone, width=5)
    Entre4.grid(row=1,column=0,padx=10,pady=10)
    Entre5 = tk.Entry(zone, width=5)
    Entre5.grid(row=1,column=1,padx=10,pady=10)
    root.bind('<F1>',lambda e:Encrypt_Hill(Entre1,Entre2,reponse))
    # root.bind('<F2>',lambda e:Decrypt_Hill(Entre1,Entre2,reponse))
    bouton = tk.Button(root, text="Crypter [F1]", command=lambda:Encrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse))
    bouton.pack(pady=25)
    reponse = tk.Label(text="Message codé en Hill ...", fg='white', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil", command=Retour)
    retour.pack(pady=25)

def Encrypt_Hill(Entre1,Entre2,Entre3,Entre4,Entre5,reponse):
    Message = Entre1.get()
    Cle = [[int(Entre2.get()),int(Entre3.get())],[int(Entre4.get()),int(Entre5.get())]]
    reponse.config(text=crypt.Hill(Message.upper(),Cle).encrypt())

# Lancement de la fenêtre
Affichage()

root.mainloop()
