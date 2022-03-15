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
Title = tk.Label(text = "Machine de cryptographie.", fg='white', bg='black', font=Title_font)
Title.pack(pady=25)
Desc = tk.Label(text = "Cette machine vous permet de crypter et décrypter des messages !", fg='white', bg='black', font=Desc_font)
Desc.pack(pady=50)

# Retour au début
def Retour():
    """Renvoie la fenêtre du départ."""
    pass

# Vigenere
def Code_Vigenere():
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    Crypt_Vigenere1 = tk.Entry()
    Crypt_Vigenere1.pack()
    Crypt_Vigenere2 = tk.Entry()
    Crypt_Vigenere2.pack()
    bouton = tk.Button(root, text="Crypter", command=lambda:Encrypt_Vigenere(Crypt_Vigenere1,Crypt_Vigenere2,reponse))
    bouton.pack(pady=25)
    reponse = tk.Label(text="Message codé en Vigenère ...", fg='white', bg='black', font=Desc_font)
    reponse.pack(pady=25)
    retour = tk.Button(root, text="Retour à l'accueil", command=Retour)
    retour.pack(pady=25)

def Encrypt_Vigenere(Crypt_Vigenere1,Crypt_Vigenere2,reponse):
    Message = Crypt_Vigenere1.get()
    Cle = Crypt_Vigenere2.get()
    reponse.config(text=crypt.Vigenere(Message.upper(),Cle.upper()).encrypt())

# Hill
  
def Code_Hill():
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    Crypt_Hill1 = tk.Entry()
    Crypt_Hill1.pack()
    Crypt_Hill2 = tk.Entry()
    Crypt_Hill2.pack()
    bouton = tk.Button(root, text="Crypter", command=lambda:Encrypt_Hill(Crypt_Hill1,Crypt_Hill2,reponse))
    bouton.pack(pady=25)
    reponse = tk.Label(text="Message codé en Hill ...", fg='white', bg='black', font=Desc_font)
    reponse.pack(pady=25)

def Encrypt_Hill(Crypt_Hill1,Crypt_Hill2,reponse):
    Message = Crypt_Hill1.get()
    Cle = Crypt_Hill2.get()
    reponse.config(text=crypt.Hill(Message.upper(),Cle).encrypt())

bt1 = tk.Button(root, text="Crypter César", command=Code_Vigenere)
bt1.pack(pady=25)
bt2 = tk.Button(root, text="Crypter Vigenere", command=Code_Vigenere)
bt2.pack(pady=25)
bt3 = tk.Button(root, text="Crypter Hill", command=Code_Hill)
bt3.pack(pady=25)

root.mainloop()
