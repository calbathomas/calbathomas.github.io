import turtle
turtle.tracer(0,0)            # accélération du tracé
turtle.screensize(2000,2000)  # taille fenêtre graphique
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):
    """ réalise une représentation graphique d'une courbe donnée par des chaines de caractères """
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)


def regleSierpinski(chaine):
    nouvelleChaine = ''    # on crée une nouvelle chaine de caractères VIDE
    for lettre in chaine:  # on épelle la chaine de caractères donnée en paramètres
        if lettre == 'F':  # si dans l'ancienne chaine, il y a un 'F'
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  # alors, on écrit F-G+F+G-F dans la nouvelle chaine
        elif lettre== 'G':
            nouvelleChaine = nouvelleChaine + 'GG'  # alors, on écrit GG dans la nouvelle chaine
        else :
            nouvelleChaine = nouvelleChaine + lettre  # sinon, on reporte la lettre telle quelle
    return nouvelleChaine


def courbeSierpinski(motifInitial, niter):
    """   appelle niter fois regleSierpinski pour créer la courbe de Sierpinski """
    courbe = motifInitial # on part du motif initial donné par l'utilisateur en paramètres
    for i in range(niter):
        nouveauMotif = regleSierpinski(courbe)  # on trouve le nouveau Motif à partir du motif de départ
        courbe = nouveauMotif # on dit que le nouveau Motif est maintenant le motif de départ
    return courbe



def triangleSierpinski(motifInitial, niter):   #dessin du triangle de Sierpinski
    """   dessin du triangle de Sierpinski """
    courbe = courbeSierpinski(motifInitial, niter)
    triangleSierpinski = ''
    for _ in range(1):
        triangleSierpinski += courbe
        triangleSierpinski += '--'
    return triangleSierpinski

longueur = 10
angle = 120
niter = 2
dessiner(triangleSierpinski('F-G-G', niter), longueur, angle) #on appelle le dessin de triangle de Sierpinski avec les parametres initiaux


turtle.update()      # accélération du tracé
turtle.exitonclick() # permet la fermeture de la fenêtre graphique