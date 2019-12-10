compteur = 0  
Moyenne = 0 #on lira c'est valeur dans le dico
somme= 0 #on lira c'est valeur dans le dico
nombre = input("combien de note avez vous?: ")#je ferai les note plus tard
nombre = int (nombre)
liste = [nombre]

while compteur < nombre:
    liste[compteur] = input("quelle est t'as note?:")
    compteur =+1

def Calcul(liste,nombre,Moyenne,somme):
    compteur = 0
    for compteur in liste:
        somme =+liste[compteur]
    Moyenne = somme/nombre
    return Moyenne

print("t'as moyenne est de %d" % (Moyenne))
input("appui sur une touche pour quitter")
