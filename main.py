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

def Code_Vigenere():
    Message = Crypt_Vigenere1.get()
    Cle = Crypt_Vigenere2.get()
    Vig1 = tk.Label(text=crypt.Vigenere(Message,Cle).encrypt(), fg='white', bg='black', font=Desc_font)
    Vig1.pack(pady=50)

Crypt_Vigenere1 = tk.Entry()
Crypt_Vigenere1.pack()
Crypt_Vigenere2 = tk.Entry()
Crypt_Vigenere2.pack()
bouton = tk.Button(root, text="Crypter Vigenere", command=Code_Vigenere)
bouton.pack()

Vig = tk.Label(text=crypt.Vigenere("CRYPTOGRAPHIE","MATHWEB").encrypt(), fg='white', bg='black', font=Desc_font)
Vig.pack(pady=50)
    

root.mainloop()
