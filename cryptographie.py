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
        return(Cesar(self.message, 26-self.decalage).encrypt())


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
            self.cle += self.cle[i]
            if self.message[i] in self.ALPHABET:
                indice = (self.position_alphabet(self.message[i]) - self.position_alphabet(self.cle[i]))%26
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

    def verif_matrice_cle(self):
        a = self.matrice_cle[0][0]
        b = self.matrice_cle[0][1]
        c = self.matrice_cle[1][0]
        d = self.matrice_cle[1][1]
        determinant = a*d-b*c
        if type(a)!=int or type(b)!=int or type(c)!=int or type(d)!=int or a<0 or b<0 or c<0 or d<0:
            return False
        if gcd(determinant,26)!=1:
            return False
        inverse_det = None
        for i in range(1,26,2):
            if (determinant*i)%26 == 1:
                inverse_det = i
        if inverse_det == None:
            return False
        return(inverse_det)
  
    def encrypt(self)->str:
        """Crypte un message en Hill."""
        if self.verif_matrice_cle()==False:
            return("Matrice invalide")
        self.message.replace(" ","")
        matrice_message=[]
        tab1=[]
        tab2=[]
        resultat=''
        if len(self.message)%2 != 0:
            self.message += "A"
            
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

    def decrypt(self)->str:
        """Décrypte un message chiffré en Hill."""
        if self.verif_matrice_cle()==False:
            return("Matrice invalide")
        self.message.replace(" ","")
        inverse_det = self.verif_matrice_cle()
        a = (self.matrice_cle[1][1] * inverse_det)%26
        b = (-self.matrice_cle[0][1] * inverse_det)%26
        c = (-self.matrice_cle[1][0] * inverse_det)%26
        d = (self.matrice_cle[0][0] * inverse_det)%26
        matrice_decrypt = [[a,b],[c,d]]
        return(Hill(self.message,matrice_decrypt).encrypt())


class Morse:
    
    def __init__(self,message:str):
        self.message = message #str
        self.alphabet = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
        
    def encrypt(self)->str:
        """Crypte un message en Morse."""
        resultat = ""
        for elt in self.message:
            if elt == " ":
                resultat += "/ "
            for cle in self.alphabet.keys():
                if elt == cle:
                    resultat += self.alphabet[cle] + " "
        return resultat
                
    def decrypt(self)->str:
        """Decrypte un message en Morse."""
        tmp = ""
        resultat = ""
        for elt in self.message:
            if elt != " ":
                tmp += elt
            elif elt == " ":
                if tmp == "/":
                    resultat += " "
                    tmp = ""
                for cle in self.alphabet.keys():
                    if tmp == self.alphabet[cle]:
                        resultat += cle
                        tmp = ""
                if tmp != "":
                    return "Ceci n'est pas du morse !"
        return resultat
    

class XOR:
    
    def __init__(self,message,cle:str):
        self.message = message #str or list
        self.cle = cle #str
    
    def encrypt(self)->list:
        """Crypte un message en XOR."""
        c = []
        n = len(self.message)
        m = len(self.cle)
        j = 0
        for i in range(n):
            c.append(ord(self.message[i]) ^ ord(self.cle[j]))
            j = (j+1)%m
        return c

    def decrypt(self)->list:
        """Decrypte un message en XOR."""
        liste = [int(e) for e in self.message.split(' ')] # Transforme le message (str) en liste.
        c = []
        n = len(liste)
        m = len(self.cle)
        j = 0
        for i in range(n):
            c.append(liste[i] ^ ord(self.cle[j]))
            j = (j+1)%m
        code = ""
        for elt in c:
            code += chr(elt)
        return code
