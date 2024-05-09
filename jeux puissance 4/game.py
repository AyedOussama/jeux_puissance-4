import os
import sys

import pygame
global board
board = [ [ 0 for i in range(7)] for j in range(6) ]



class grille:
    case_libre = 0
    pion_noir_joueur1 = 1
    pion_blanc_joueur2 = 2

    def __init__(self):
        self.board =board

    def get_horizontal_piongagnante(self):
        piongagnante = ""
        ligne = 5
        sortir = False
      
        while ligne >= 0 and sortir == False:
            for colonne in range(4):  
                if self.board[ligne][colonne] == self.board[ligne][colonne + 1] == self.board[ligne][colonne + 2] == self.board[ligne][colonne + 3] == 1:  
                    piongagnante = "noir"
                    sortir = True
                if self.board[ligne][colonne] == self.board[ligne][colonne + 1] == self.board[ligne][colonne + 2] == self.board[ligne][colonne + 3] == 2:  
                    piongagnante = "blanc"
                    sortir = True
            
            ligne = ligne - 1
        
        return piongagnante

    def get_vertical_piongagnante(self):
        piongagnante = ""
        
        for colonne in range(7):
            for ligne in range(5, 2, -1):
                if self.board[ligne][colonne] == self.board[ligne - 1][colonne] == self.board[ligne - 2][colonne] == self.board[ligne - 3][colonne] == 1:
                    piongagnante = "noir"
                if self.board[ligne][colonne] == self.board[ligne - 1][colonne] == self.board[ligne - 2][colonne] ==  self.board[ligne - 3][colonne] == 2:
                    piongagnante = "blanc"
        return piongagnante

    def get_diagonals_piongagnante(self):
        piongagnante = ""
        for ligne in range(3):
            for colonne in range(4):
                if self.board[ligne][colonne] == self.board[ligne + 1][colonne + 1] == self.board[ligne + 2][colonne + 2] == self.board[ligne + 3][colonne + 3] == 1:
                    piongagnante = "noir"
                if self.board[ligne][colonne] == self.board[ligne + 1][colonne + 1] == self.board[ligne + 2][colonne + 2] == self.board[ligne + 3][colonne + 3] == 2:
                    piongagnante = "blanc"
        
        for ligne in range(3):   
            for colonne in range(3, 7):
                if self.board[ligne][colonne] == self.board[ligne + 1][colonne - 1] ==self.board[ligne + 2][colonne - 2] == self.board[ligne + 3][colonne - 3] == 1:
                    piongagnante = "noir"
                if self.board[ligne][colonne] == self.board[ligne + 1][colonne - 1] == self.board[ligne + 2][colonne - 2] == self.board[ligne + 3][colonne - 3] == 2:
                    piongagnante = "blanc"
        return piongagnante

    def get_piongagnante(self): 
        pion_couleur= self.get_horizontal_piongagnante()
        if pion_couleur != "":
            return pion_couleur
        pion_couleur = self.get_vertical_piongagnante()
        if pion_couleur != "":
            return pion_couleur
        pion_couleur = self.get_diagonals_piongagnante()
        if pion_couleur != "":
            return pion_couleur
           
    def ajouter_pion(self, colonne, joueur):
        ligne = 5  
        sortir = False
        while ligne >= 0 and sortir == False:
           
            if self.board[ligne][colonne] == 0:
                if joueur == 1:
                    self.board[ligne][colonne] = 1
                    sortir = True
                else:
                    self.board[ligne][colonne] = 2
                    sortir = True
           
            ligne = ligne - 1  

    
    def inverse_grille(self):
        grille_inverse = []
        for ligne in range(5, -1, -1):
            grille_inverse.append(self.board[ligne])
        return grille_inverse

    def affichage(self):
        print("\n")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()
        print("\n")

class interface:
    IMAGE_DIRECTORY = "image"

    def __init__(self):
        self.grille = grille()
        self.pyjeux = pygame

        pygame.init()
        pygame.display.set_caption('jeux puissance 4')
        
        self.board_picture = pygame.image.load(os.path.join(interface.IMAGE_DIRECTORY, "plateau .png"))
        taille_plateau_de_jeu = self.board_picture.get_size()
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()
        self.pionnoir = pygame.image.load(os.path.join(interface.IMAGE_DIRECTORY, "pion_noir.png"))
        self.pionblanc = pygame.image.load(os.path.join(interface.IMAGE_DIRECTORY, "pion_blanc.png"))
       

    def determine_colonne(self, x):
        colonne = x - 16
        colonne = colonne / 97
        if colonne in range(0, 7):
            if self.grille.board[5][int(colonne)] == 0:
                  status=False
        return int(colonne)

    def modifier(self):
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.board_picture, (0, 0))
        grille_enmodejeu = self.grille.inverse_grille()
        self.grille.affichage()

        for i in range(len(grille_enmodejeu)):
            for j in range(len(grille_enmodejeu[i])):
                
                if grille_enmodejeu[i][j] == 1:
                    self.screen.blit(self.pionnoir, (16 + 97 * j, 13 - 97.5 * i + 486))
                    pygame.display.flip()
                
                if grille_enmodejeu[i][j] ==2:
                    self.screen.blit(self.pionblanc, (16 + 97 * j, 13 - 97.5 * i + 486))
                    pygame.display.flip()
                
                
class partie:
    nb_jetons = 42

    def __init__(self):
        self.pion_jouee = 0
        self.couleur_gagne = False
        self.interface = interface()

    def get_joueur(self):
       
        if self.pion_jouee % 2 == 0:
            joueur_id = grille.pion_noir_joueur1
        else:
            joueur_id = grille.pion_blanc_joueur2
        return joueur_id
    def affiche_gagnant(self):
        if self.couleur_gagne == "" :
            return "pas de gagnant"
        elif self.couleur_gagne == "noir":
            return  "joueur 1  gagne"
        else:
           return  "joueur 2  gagne"  

    def jouer(self):
        while self.couleur_gagne != "noir" and self.couleur_gagne != "blanc" and self.pion_jouee < partie.nb_jetons:
           
            for event in self.interface.pyjeux.event.get():

                self.interface.grille.affichage()
                if event.type == self.interface.pyjeux.MOUSEBUTTONUP:
                    x, y = self.interface.pyjeux.mouse.get_pos()
                    joueur = self.get_joueur()
                    colonne = self.interface.determine_colonne(x)
                    self.interface.grille.ajouter_pion(colonne, joueur)
                    self.pion_jouee = self.pion_jouee + 1
                    self.couleur_gagne = self.interface.grille.get_piongagnante()
                    self.interface.modifier()
                    self.interface.pyjeux.display.flip()
                    print(f"{self.affiche_gagnant()} \n \t\t\t A bientot ")
                if event.type == self.interface.pyjeux.QUIT:
                    sys.exit(0)