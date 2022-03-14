from math import gcd


class Cesar:

    def __init__(self, message:str, decalage:int):
        self.message = message #str
        self.decalage = decalage #int
        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def position_alphabet(self, lettre:str)->int:
        """Retourne le numéro de la lettre dans l'alphabet."""
        return self.ALPHABET.find(lettre)

    def encrypt(self)->str:
        """Crypte un message en César."""
        resultat = ''
        for lettre in self.message :
            if lettre in self.ALPHABET :
                indice = (self.position_alphabet(lettre) + self.decalage)%26
                resultat = resultat + self.ALPHABET[indice]
            else:
                resultat = resultat + lettre
        return resultat

    def decrypt(self)->str:
        """Décrypte un message en César."""
        return(self.encrypt(self.message, 26-self.decalage))


class Vigenere:

    def __init__(self, message:str, cle:str):
        self.message = message #str
        self.cle = cle #str
        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def position_alphabet(self, lettre:str)->int:
        """Retourne le numéro de la lettre dans l'alphabet."""
        return self.ALPHABET.find(lettre)

    def encrypt(self)->str:
        """Crypte un message en Vigenère."""
        resultat = ''  
        for i in range(len(self.message)) :
            self.cle += self.cle[i]
            if self.message[i] in self.ALPHABET:
                indice = ( self.position_alphabet(self.message[i]) + self.position_alphabet(self.cle[i]))%26
                resultat += self.ALPHABET[indice]
            else :
                resultat = resultat + self.message[i]
        return resultat

    def decrypt(self)->str:
        """Décrypte un message en Vigenère."""
        resultat = ''
        for i in range(len(self.message)) :
            cle += cle[i]
            if self.message[i] in self.ALPHABET:
                indice = (self.position_alphabet(self.message[i]) - self.position_alphabet(cle[i]))%26
                resultat += self.ALPHABET[indice]
            else :
                resultat = resultat + self.message[i]
        return resultat


class Hill:
    
    def __init__(self, message:str, matrice_cle:list):
        self.message = message #str
        self.matrice_cle = matrice_cle #list
        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def position_alphabet(self, lettre:str)->int:
        """Retourne le numéro de la lettre dans l'alphabet."""
        return self.ALPHABET.find(lettre)

    def calcul_matrice(self, A:list, B:list)->list:
        """Retourne le produit matriciel de A et B."""
        mat_resultat=[]
        mat_resultat.append((A[0][0]*B[0] + A[0][1]*B[1])%26)
        mat_resultat.append((A[1][0]*B[0] + A[1][1]*B[1])%26)
        return mat_resultat

    def encrypt(self)->str:
        """Crypte un message en Hill."""
        matrice_message=[]
        tab1=[]
        tab2=[]
        resultat=''
        for lettre in self.message:
            matrice_message.append(self.position_alphabet(lettre))
        for i in range(0,len(matrice_message),2):
            tab1.append(matrice_message[i:i+2])
        for i in range(len(tab1)):
            tab2.append(self.calcul_matrice(self.matrice_cle,tab1[i]))
        for mat in tab2:
            for elt in mat:
                resultat += self.ALPHABET[elt]
        return resultat
