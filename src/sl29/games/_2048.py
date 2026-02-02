"""Module providing the logic of the 2048 game"""

import random
from typing import List, Tuple
import copy 

TAILLE:int = 4


# ==========================================================
# 🎯 FONCTION PUBLIQUE (API POUR L’INTERFACE)
# ==========================================================

def nouvelle_partie() -> Tuple[List[List[int]], int]:
    """
    Crée une nouvelle partie du jeu 2048.

    :return: Une grille TAILLExTAILLE initialisée avec deux tuiles, ainsi que le score à 0.
    :rtype: Tuple[List[List[int]], int]
    """
    grille=_creer_plateau_vide()
    grille=_ajouter_tuile(grille)
    grille=_ajouter_tuile(grille)
    score=0
    return (grille,score)


def jouer_coup(plateau: List[List[int]], direction: str) -> tuple[List[List[int]], int, bool]:
    """
    Effectuer un mouvement sur le plateau.

    :param plateau: Une grille TAILLExTAILLE du jeu.
    :type plateau: List[List[int]]
    :param direction: La direction du déplacement : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    :type direction: str
    :return: Retourne un tuple (nouveau_plateau, points, est_fini).
    :rtype: tuple[List[List[int]], int, bool]
    """
    
    if direction=='g':
        nouveau_plateau, points=_deplacer_gauche(plateau)
    elif direction=='d':
        nouveau_plateau, points=_deplacer_droite(plateau)
    elif direction=='h':
        nouveau_plateau, points=_deplacer_haut(plateau)
    elif direction=='b':
        nouveau_plateau, points=_deplacer_bas(plateau) 
    est_fini=_partie_terminee(plateau)
    
    if plateau==nouveau_plateau:
        return (nouveau_plateau, points, est_fini)
    else :
        return (_ajouter_tuile(nouveau_plateau), points, est_fini)

    raise NotImplementedError("Fonction jouer_coup non implémentée.")

# ==========================================================
# 🔒 FONCTIONS PRIVÉES (LOGIQUE INTERNE)
# ==========================================================

def _creer_plateau_vide() -> List[List[int]]:
    """
    Crée une grille TAILLExTAILLE remplie de zéros.
    :return: Une grille vide.
    :rtype: List[List[int]]
    """
    grille=[]

    for _ in range (TAILLE) :
        ligne = []
        for _ in range (TAILLE) :
            ligne.append(0) #je complète ma ligne
        grille.append(ligne) #j'ajoute  mes lignes
        
    return grille


def _get_cases_vides(plateau: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Retourne les coordonnées des cases vides sous forme d'une liste de coordonnées

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une liste de coordonnées
    :rtype: List[Tuple[int, int]]
    """

    coordonnees =[]
    for ligne in range (len(plateau)):
        for valeur in range (len(plateau[ligne])):
            if plateau[ligne][valeur]==0:
                coordonnees.append((ligne,valeur))
    
    return coordonnees


def _ajouter_tuile(plateau: List[List[int]]) -> List[List[int]]:
    """
    Ajoute une tuile de valeur 2 sur une case vide.

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une nouvelle grille avec une tuile ajoutée.
    :rtype: List[List[int]]
    """
    grille=[]

    for i in range (TAILLE) :
        ligne = []
        for x in range (TAILLE) :
            ligne.append(plateau[i][x]) #je complète ma ligne
        grille.append(ligne) #j'ajoute  mes lignes

    liste=_get_cases_vides(grille)
    case=liste[random.randint(0,len(liste)-1)]

    ligne=case[0]
    colonne=case[1]

    grille[ligne][colonne]=2

    return grille

def _supprimer_zeros(ligne: List[int]) -> List[int]:
    """
    Supprime les zéros d'une ligne.

    :param ligne: Une ligne de la grille.
    :type ligne: List[int]
    :return: La ligne sans zéros.
    :rtype: List[int]
    """

    resultat = []
    for l in (ligne):
        if (l!=0):
            resultat.append(l)
    
    return resultat

def _fusionner(ligne: List[int]) -> Tuple[List[int], int]:
    """
    Fusionne les valeurs identiques consécutives d'une ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après fusion, les points gagnés
    :rtype: Tuple[List[int], int]
    """
    somme=0
    liste=[]
    i=0
    while (i<len(ligne)):
        if ((i+1) < len(ligne) and ligne[i]==ligne[i+1]):
            somme += ligne[i]+ligne[i+1]
            ajout=ligne[i]+ligne[i+1]
            liste.append(ajout)
            i+=2
        else: 
            liste.append(ligne[i])
            i+=1
    return (liste,somme)

    raise NotImplementedError("Fonction _fusionner non implémentée.")

def _completer_zeros(ligne: List[int]) -> List[int]: # ajouter les annotations de type
    """
    Rajoute les zéros pour compléter la ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après ajout des zéros
    :rtype: List[int]
    """
    while len(ligne)<4:
        ligne.append(0)
    return ligne
    raise NotImplementedError("Fonction _completer_zeros non implémentée.")

def _deplacer_gauche(plateau: List[List[int]]) -> Tuple[List[List[int]], int]: # ajouter les annotations de type
    """
    Permet de faire un mouvement à gauche

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Le plateau après mouvement, les points gagnés
    :rtype: Tuple[List[List[int]], int]
    """

    nouveau_plateau=[]
    nouveaux_points=0
    for ligne in (plateau):
        ligne_sans_zeros=_supprimer_zeros(ligne)
        ligne_fusionnee, point=_fusionner(ligne_sans_zeros)
        nouveaux_points+=point
        ligne_finale = _completer_zeros(ligne_fusionnee)
        nouveau_plateau.append(ligne_finale)
    return (nouveau_plateau, nouveaux_points)

    raise NotImplementedError("Fonction _deplacer_gauche non implémentée.")

def _inverser_lignes(plateau: List[List[int]]) ->List[List[int]] : # ajouter les annotations de type
    """
    Permet d'inverser le plateau pour préparer un déplacement à droite

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Le plateau après inversion des lignes
    :rtype: List[List[int]]
    """
    plateau_inverse=[]
    for i in range (TAILLE) :
        ligne = []
        for x in range (TAILLE-1,0-1,-1) :
            ligne.append(plateau[i][x]) #je complète ma ligne
        plateau_inverse.append(ligne) #j'ajoute  mes lignes
    return plateau_inverse

    raise NotImplementedError("Fonction _inverser_lignes non implémentée.")

def _deplacer_droite(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers la droite en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """

    plateau_inverse=_inverser_lignes(plateau)
    plateau_inverse2,point=_deplacer_gauche(plateau_inverse)
    plateau_resultat=_inverser_lignes(plateau_inverse2)
    return (plateau_resultat, point)

    raise NotImplementedError("Fonction _deplacer_droite non implémentée.")

def _transposer(plateau: List[List[int]]) ->List[List[int]] : # ajouter les annotations de type
    """
    Permet de transposer le plateau le plateau pour préparer un déplacement en haut

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Le plateau après transposition
    :rtype: List[List[int]]
    """
    plateau_inverse=[]
    for i in range (TAILLE) :
        ligne = []
        for x in range (TAILLE) :
            ligne.append(plateau[x][i]) #je complète ma ligne
        plateau_inverse.append(ligne) #j'ajoute  mes lignes
    return plateau_inverse

    raise NotImplementedError("Fonction _transposer non implémentée.")

def _deplacer_haut(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le haut en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """

    plateau_inverse=_transposer(plateau)
    plateau_inverse2,point=_deplacer_gauche(plateau_inverse)
    plateau_resultat=_transposer(plateau_inverse2)
    return (plateau_resultat, point)

    raise NotImplementedError("Fonction _deplacer_haut non implémentée.")


def _deplacer_bas(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le bas en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """
    
    plateau_inverse=_transposer(plateau)
    plateau_inverse2,point=_deplacer_droite(plateau_inverse)
    plateau_resultat=_transposer(plateau_inverse2)
    return (plateau_resultat, point)
    
    raise NotImplementedError("Fonction _deplacer_bas non implémentée.")

def _partie_terminee(plateau: List[List[int]]) -> bool:
    """
    Vérifier si la partie est finie

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un booléen contenant la réponse à la question
    :rtype: bool
    """
    # Partie non terminee si il y a des cases vides
    # Partie non terminee si il y a des fusions possibles (horizontale ou verticale)
    # Sinon c'est vrai
    case_vides=_get_cases_vides(plateau)
    
    plateau2=[]
    
    plateau3= []
    
    for ligne in plateau :
        plateau2.append(_supprimer_zeros(ligne))
        
    for ligne in _transposer(plateau) :
        plateau3.append(_supprimer_zeros(ligne))
    
    for ligne in plateau2 :
        ligne2, points= _fusionner(ligne)
        if points != 0 :
            return False
        
    for ligne in plateau3 :
        ligne2, points= _fusionner(ligne)
        if points != 0 :
            return False
    if len(case_vides)!=0:
        return False
    
    return True
        
    raise NotImplementedError("Fonction _partie_terminee non implémentée.")