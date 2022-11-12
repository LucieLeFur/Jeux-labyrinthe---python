#-------------------------------------------------------------------------------
# Nom du programme : LabyrintheLeFur.py
#
# Labyrinthe est un jeu qui permet au joueur de se déplacer dans un labyrinthe
# le joueur doit trouver la sortie mais la difficulté est qu'il a un minimum de
# temps pour sortir, en plus il existe des ennemis qui se promènent dans le labyrinthe !
# Il devra donc éviter ses ennemis et sortir en un minimum de temps !
# le joueur dispose de 3 vies, il pert une vie lorsqu'il rencontre un ennemi et reviendra au début
# il existe des sabliers dans le jeu qui lui permettront de lui rajouter du temps pour sortir
# si on appuie sur la touche Q on quitte le programme
#
# Auteur du programme : Lucie Le Fur
# Crée le : 03/10/2020
# Copyright : (c) lucie 2020
#-------------------------------------------------------------------------------

import pygame
import random
from pygame.locals import *

# Classe Labyrinthe
# Cette classe permet de gérer le labyrinthe
class Labyrinthe:
    
    # #############################################################################################
    # Contructeur de la classe
    # paramètres d'entrées : fenetre : objet pour la fenêtre pygame
    #                        nomFichierImgMur : nom du fichier de l'image pour afficher les murs du labyrinthe
    #                        nomFichierImgCouloir : nom du fichier de l'image pour afficher les couloirs du labyrinthe
    #                        nomFichierImgSablier : nom de fichier de l'image pour afficher les sabliers
    #                        nomFichierImgSortie : nom du fichier de l'image pour afficher la porte de sortie
    # ############################################################################################# 
    def __init__(self, fenetre, nomFichierImgMur, nomFichierImgCouloir, nomFichierImgSablier, nomFichierImgSortie):
        # Attribut fenetre pour le nom de l'objet pour la fenêtre pygame  
        self.fenetre = fenetre
        # Attribut nomFichierImgMur pour le nom du fichier image pour les murs du labyrinthe 
        self.nomFichierImgMur= nomFichierImgMur
        # Attribut nomFichierImgCouloir pour le nom du fichier image pour les couloirs        
        self.nomFichierImgCouloir= nomFichierImgCouloir        
        # Attribut nomFichierImgSortie pour le nom du fichier image pour la porte de sortie      
        self.nomFichierImgSortie = nomFichierImgSortie
        # Attribut nomFichierImgSablier pour le nom du fichier image pour les sabliers     
        self.nomFichierImgSablier = nomFichierImgSablier    
        # Attribut positionsBlocMurs pour les positions des murs du labyrinthe
        self.positionsBlocMurs = []
        # Attribut positionsSabliers pour les positions des sabliers dans le labyrinthe        
        self.positionsSabliers = []

    # #############################################################################################
    # Méthode de la classe - permet de générer le labyrinthe dans la fenêtre
    # paramètres d'entrées : tableauLabyrinthe : tableau contenant les éléments servant à générer le labyrinthe
    #                                 Le tableau contient toutes les lignes du labyrinthe
    #                                 Pour chaque ligne, la ligne contient un tableau pour les colonnes du labyrinthe
    #                                     Colonne = "COULOUR" : ça sera une image pour le couloir
    #                                     Colonne = "MUR" : ça sera une image pour un mur
    #                                     Colonne = "SORTIE" : ça sera une image pour la sortie
    #                                     Colonne = "SABLIER" : ça sera une image pour un sablier
    #                               Chaque image à une taille de 32*32 pixels
    # ############################################################################################# 
    def genererLabyrinthe(self, tableauLabyrinthe):
        # on commence à la position Y = 0
        posY = 0
        # on boucle sur toutes les lignes du labyrinthe
        for ligne in tableauLabyrinthe:
            # on commence au début de la ligne à la position X = 0        
            posX = 0
            # pour une ligne du labyrinthe on boucle sur toutes les colonnes
            for colonne in ligne:
                # si on doit afficher le couloir
                if (colonne == "COULOIR"):
                    # on charge l'image pour le couloir
                    couloirImage = pygame.image.load(self.nomFichierImgCouloir)
                    # on positionne l'image du couloir à la position posX, posY
                    self.fenetre.blit(couloirImage, (posX, posY)) 
                # si on doit afficher le mur  
                elif (colonne == "MUR"):
                    # on charge l'image pour le mur
                    murImage = pygame.image.load(self.nomFichierImgMur)
                    # on créé une zone (rectangle) encadrant l'image du mur (left, top, width, height) 
                    positionMur = murImage.get_rect()
                    # on renseigne la position ou sera le mur
                    positionMur.left = posX 
                    positionMur.top = posY
                    # on positionne l'image du mur à la position positionMur
                    self.fenetre.blit(murImage, positionMur)
                    # on ajoute la position du mur dans une liste
                    self.positionsBlocMurs.append(positionMur)
                # si on doit afficher la porte de sortie                   
                elif (colonne == "SORTIE"):
                    # on charge l'image pour la sortie                
                    sortieImage = pygame.image.load(self.nomFichierImgSortie)
                    # on créé une zone (rectangle) encadrant l'image de la sortie                    
                    self.positionSortie = sortieImage.get_rect()
                    # on renseigne la position ou sera la porte de sortie                    
                    self.positionSortie.left = posX 
                    self.positionSortie.top = posY
                    # on positionne l'image de la sortie à la position positionSortie                    
                    self.fenetre.blit(sortieImage, self.positionSortie)
                # si on doit afficher un sablier                           
                elif (colonne == "SABLIER"):
                    # on charge l'image pour le sablier                        
                    sablierImage = pygame.image.load(self.nomFichierImgSablier)
                    # on créé une zone (rectangle) encadrant l'image du sablier                           
                    positionSablier = sablierImage.get_rect()
                    # on renseigne la position ou sera le sablier                             
                    positionSablier.left = posX 
                    positionSablier.top = posY
                     # on positionne l'image du sablier à la position positionSablier    
                    self.fenetre.blit(sablierImage, positionSablier)
                    # on ajoute la position du sablier dans une liste                    
                    self.positionsSabliers.append(positionSablier)

                # on rajoute pour la position X de la prochaine image 32 pixels, ça correspond à la largeur d'une image (mur, couloir, sortie, sablier)
                posX = posX + 32
            # on rajoute pour la position Y de la prochaine image 32 pixels, ça correspond à la hauteur d'une image (mur, couloir, sortie, sablier)                
            posY = posY + 32
                  
    # #############################################################################################
    # Méthode de la classe - permet de savoir à partir d'une position d'une surface s'il existe une collision avec la sortie
    # paramètres d'entrées : ciblePosition : position de la zone avec laquelle on va vérifier si il y a collision avec la sortie
    # Retour : true si il y a collision avec la sortie, false si il y a pas collision avec la sortie
    # ############################################################################################# 
    def detecterCollisionSortie(self, ciblePosition):
        collisionSortie = self.positionSortie.colliderect(ciblePosition)
        return collisionSortie
        

    # #############################################################################################
    # Méthode de la classe - permet de savoir à partir d'une position d'une surface s'il existe une collision avec un des sabliers
    # paramètres d'entrées : ciblePosition : position de la zone avec laquelle on va vérifier si il y a collision avec un des sabliers
    # Retour : true si il y a collision avec un des sabliers, false si il y a pas collision avec un des sabliers
    # ############################################################################################# 
    def detecterCollisionSablier(self, ciblePosition):
        collisionSablier = False
        indiceSablier = 0
        # on boucle sur la table des positions des sabliers tant qu'il n'y a pas de collision avec un sablier
        while (collisionSablier == False and indiceSablier < len(self.positionsSabliers)):
          # si il y a collision avec la position du sablier, alors on indique qu'il y a collision
          if (ciblePosition.colliderect(self.positionsSabliers[indiceSablier]) == True):
              collisionSablier = True
          else:
              # si il y a pas collision on indique l'indice suivant pour la liste des positions des sabliers
              indiceSablier = indiceSablier + 1
              
        # si il y a eu collision avec un sablier, on efface le sablier pour mettre un couloir
        if (collisionSablier == True):
            # on charge l'image pour le couloir pour effacer le sabler
            couloirImage = pygame.image.load(self.nomFichierImgCouloir)
            # on positionne l'image du coulour à la position du sablier pour effacer le sablier        
            self.fenetre.blit(couloirImage, self.positionsSabliers[indiceSablier])
            # on supprime la position du sablier dans la liste des positions des sabliers            
            self.positionsSabliers.pop(indiceSablier)
            
        # on retourne si il y a eu collision ou non    
        return collisionSablier
      
# Classe Mechant
# Cette classe permet d'afficher un méchant dans le labyrinthe, de gérer son déplacement et vérifier si il y a collision avec ce méchant  
class Mechant:
    
    # #############################################################################################
    # Contructeur de la classe
    # paramètres d'entrées : fenetre : objet pour la fenêtre pygame
    #                        nomFichierImgMechant : nom du fichier de l'image pour afficher le méchant
    #                        ligne : ligne ou on affichera le méchant
    #                        colonne : colonne ou on affichera le méchant
    # #############################################################################################     
    def __init__(self, fenetre, nomFichierImgMechant, ligne, colonne):
        self.fenetre = fenetre
        # on charge l'image pour le méchant
        self.imageMechant = pygame.image.load(nomFichierImgMechant)
        # on créé une zone (rectangle) encadrant l'image du méchant                 
        self.positionMechant = self.imageMechant.get_rect()
        # on renseigne la position ou sera le méchant (on multiplie par 32 qui correspond à la taille d'une image)             
        self.positionMechant.left = colonne * 32
        self.positionMechant.top = ligne * 32
        # on positionne l'image de la sortie à la position positionSortie       
        fenetre.blit(self.imageMechant, self.positionMechant)
        # au début la position du méchant sera vers le bas
        self.directionMechant = "B"
        
    # #############################################################################################
    # Méthode de la classe - permet de savoir à partir d'une position d'une surface s'il existe une collision du méchant avec un des obstacles
    # paramètres d'entrées : tableauPositionsObstacles : liste des positions des obstacles
    #                        ciblePosition : position du méchant avec laquelle on va vérifier si il y a collision avec un des obstacles
    # Retour : true si il y a collision avec un des obstacles, false si il y a pas collision avec un des obstacles
    # ############################################################################################# 
    def collisionObstacle(self, tableauPositionsObstacles, positionMechant):
        collisionObstacle = False
        indiceObstacle = 0
        # on boucle sur la table des positions des obstacles tant qu'il n'y a pas de collision avec un obstacle        
        while (collisionObstacle == False and indiceObstacle < len(tableauPositionsObstacles)):
          
          # si il y a eu collision avec un sablier, on efface le sablier pour mettre un couloir
          if (positionMechant.colliderect(tableauPositionsObstacles[indiceObstacle]) == True):
              collisionObstacle = True
          indiceObstacle = indiceObstacle + 1

        # on retourne si il y a eu collision ou non    
        return collisionObstacle

    # #############################################################################################
    # Méthode de la classe - permet de connaitre le sens inverse d'une direction
    # paramètres d'entrées : direction : direction
    # Retour : direction inverse
    # ############################################################################################# 
    def sensInverseDirection(self, direction):
        # si à droite la position inverse sera la gauche
        if (direction == "D"):
            return "G"
        # si à gauche la position inverse sera la droite            
        elif (self.directionMechant == "G"):
            return "D"
        # si en haut la position inverse sera le bas                        
        elif (self.directionMechant == "H"):
            return "B"
        # si en base la position inverse sera le haut                 
        elif (self.directionMechant == "B"):
            return "H"

    # #############################################################################################
    # Méthode de la classe - permet de générer le déplacement du méchant par rapport à une liste de position d'obstacle
    # paramètres d'entrées : tableauPositionsObstacles : liste des positions des obstacles
    # ############################################################################################# 
    def gererDeplacement(self, tableauPositionsObstacles):
        # liste pour les directions possibles du méchant
        listeDirectionsPossibleMechant = []
        
        # on recherche toutes les directions ou le méchant peut aller
        # Droite
        # pour aller à droite, on recherche la nouvelle position du méchant pour un déplacement de 1 pixel
        positionDeplacementDroite = self.positionMechant.move(1, 0)
        # si on ne va pas vers la gauche (sens inverse) et si il y a pas collision avec la liste des obstacles, alors le choix vers la droite est possible
        if (self.directionMechant != "G" and self.collisionObstacle(tableauPositionsObstacles, positionDeplacementDroite) == False):
            listeDirectionsPossibleMechant.append("D")
        
        # Gauche
        # pour aller à gauche, on recherche la nouvelle position du méchant pour un déplacement de 1 pixel
        positionDeplacementGauche = self.positionMechant.move(-1, 0)
        # si on ne va pas vers la droite (sens inverse) et si il y a pas collision avec la liste des obstacles, alors le choix vers la gauche est possible        
        if (self.directionMechant != "D" and self.collisionObstacle(tableauPositionsObstacles, positionDeplacementGauche) == False):
            listeDirectionsPossibleMechant.append("G")
        
        # Haut
        # pour aller en haut, on recherche la nouvelle position du méchant pour un déplacement de 1 pixel        
        positionDeplacementHaut = self.positionMechant.move(0, -1)
        # si on ne va pas vers le bas (sens inverse) et si il y a pas collision avec la liste des obstacles, alors le choix vers le haut est possible               
        if (self.directionMechant != "B" and self.collisionObstacle(tableauPositionsObstacles, positionDeplacementHaut) == False):
            listeDirectionsPossibleMechant.append("H")
        
        # Bas
        # pour aller en bas, on recherche la nouvelle position du méchant pour un déplacement de 1 pixel                
        positionDeplacementBas = self.positionMechant.move(0, 1)
        # si on ne va pas vers le haut (sens inverse) et si il y a pas collision avec la liste des obstacles, alors le choix vers le bas est possible               
        if (self.directionMechant != "H" and self.collisionObstacle(tableauPositionsObstacles, positionDeplacementBas) == False):
            listeDirectionsPossibleMechant.append("B")        
        
        # si on a trouvé aucun choix possible (cul de sac), alors le méchant ira dans la direction inverse
        if (len(listeDirectionsPossibleMechant) == 0):
            self.directionMechant = self.sensInverseDirection(self.directionMechant)
        else:
            # on choisit une direction au hasard dans les directions possibles
            self.directionMechant = random.choice(listeDirectionsPossibleMechant)       
        
        # on recherche la position pour le choix de la direction qu'on a trouvé
        if (self.directionMechant == "D"):
            self.positionMechant = self.positionMechant.move(1, 0)
        elif (self.directionMechant == "G"):
            self.positionMechant = self.positionMechant.move(-1, 0)
        elif (self.directionMechant == "H"):
            self.positionMechant = self.positionMechant.move(0, -1)
        elif (self.directionMechant == "B"):
            self.positionMechant = self.positionMechant.move(0, 1)
             
        # on positionne l'image du méchant à la position qu'on a trouvé            
        fenetre.blit(self.imageMechant, self.positionMechant) 
        
    def detecterCollision(self, ciblePosition):
         return self.positionMechant.colliderect(ciblePosition)

# Classe Joueur
# Cette classe permet d'afficher le joueur dans le labyrinthe et de se déplacer  
class Joueur:
    
    # #############################################################################################
    # Contructeur de la classe
    # paramètres d'entrées : fenetre : objet pour la fenêtre pygame
    #                        nomFichierImgJoueur : nom du fichier de l'image pour afficher le joueur
    #                        nomFichierImgJoueurVide : nom du fichier de l'image pour effacer le joueur
    #                        ligne : ligne ou on affichera le joueur
    #                        colonne : colonne ou on affichera le joueur
    # #############################################################################################       
    def __init__(self, fenetre, nomFichierImgJoueur, nomFichierImgJoueurVide, ligneJoueur, colonneJoueur):
        self.fenetre = fenetre
        # on charge l'image pour le joueur
        self.imageJoueur=pygame.image.load(nomFichierImgJoueur)
        # on charge l'image pour effacer le joueur
        self.imageJoueurVide=pygame.image.load(nomFichierImgJoueurVide)
        # on créé une zone (rectangle) encadrant l'image du joueur          
        self.positionDepart=self.imageJoueur.get_rect()
        # on renseigne la position ou sera le joueur on multiplie par 32 qui correspond à la taille d'une image      
        self.positionDepart.left = colonneJoueur * 32
        self.positionDepart.top = ligneJoueur * 32
        self.positionJoueur = self.positionDepart
        
    # #############################################################################################
    # Méthode de la classe - permet d'afficher le joueur dans la fenêtre
    # #############################################################################################         
    def afficherDepartJoueur(self):
        fenetre.blit(self.imageJoueurVide, self.positionJoueur) 
        self.positionJoueur = self.positionDepart
        fenetre.blit(self.imageJoueur, self.positionDepart)        

    # #############################################################################################
    # Méthode de la classe - permet de déplacer le joueur vers le haut si possible
    # #############################################################################################
    def deplacerHaut(self, tableauPositionsObstacles):
        nouvellePosition = self.positionJoueur.move(0, -2)
        self.deplacerSiPossible(nouvellePosition, tableauPositionsObstacles)

    # #############################################################################################
    # Méthode de la classe - permet de déplacer le joueur vers le bas si possible
    # #############################################################################################
    def deplacerBas(self, tableauPositionsObstacles):
        nouvellePosition = self.positionJoueur.move(0, 2)
        self.deplacerSiPossible(nouvellePosition, tableauPositionsObstacles)
           
    # #############################################################################################
    # Méthode de la classe - permet de déplacer le joueur vers la droite si possible
    # #############################################################################################           
    def deplacerDroite(self, tableauPositionsObstacles):
        nouvellePosition = self.positionJoueur.move(2, 0)
        self.deplacerSiPossible(nouvellePosition, tableauPositionsObstacles)

    # #############################################################################################
    # Méthode de la classe - permet de déplacer le joueur vers la gauche si possible
    # #############################################################################################      
    def deplacerGauche(self, tableauPositionsObstacles):
        nouvellePosition = self.positionJoueur.move(-2, 0)
        self.deplacerSiPossible(nouvellePosition, tableauPositionsObstacles)
        
    # #############################################################################################
    # Méthode de la classe - permet de déplacer le joueur si s'est possible
    # paramètres d'entrées : nouvellePositionJoueur : la nouvelle position du joueur
    #                        tableauPositionsObstacles : liste des positions de obstacles
    # #############################################################################################    
    def deplacerSiPossible(self, nouvellePositionJoueur, tableauPositionsObstacles):
        collisionObstacle = False
        indiceObstacle = 0
        while (collisionObstacle == False and indiceObstacle < len(tableauPositionsObstacles)):
          
          if (nouvellePositionJoueur.colliderect(tableauPositionsObstacles[indiceObstacle]) == True):
              collisionObstacle=True
          else:    
            indiceObstacle = indiceObstacle + 1
          
        # si il y a pas collision alors le joueur peut se déplacer  
        if (collisionObstacle == False):
          # on efface le joueur à sa position
          fenetre.blit(self.imageJoueurVide, self.positionJoueur)
          # on déplace le joueur à sa nouvelle position
          self.positionJoueur = nouvellePositionJoueur
          fenetre.blit(self.imageJoueur, self.positionJoueur)            

pygame.init()
pygame.display.set_caption("LE LABYRINTHE !!!")
# la fenêtre aura une taille de 1100 * 670
fenetre = pygame.display.set_mode( (1100, 670) )

# Ce tableau servira pour contruire le labyrinthe, on va y mettre toutes les lignes du labyrinthe
tableauLabyrinthe = []
# liste de méchants
listeMechants = []
# nombre de vie au départ
nombreVie = 3

# on cré un objet labyrinthe
labyrinthe = Labyrinthe(fenetre,"mur.png", "caseblanche.png", "sablier.png", "sortie.png")

# police pour afficher du texte, la police est la police par défaut (None) et la taille est de 72 pixels 
police = pygame.font.Font(None,72)

# temps en ms depuis que le jeu est lancé, initialisation de pygame (appel de pygame.init())
debutProgrammeEnMs=pygame.time.get_ticks()

# On ouvre le fichier ou se trouve le labyrinthe en lecture (r)
fichierLabyrinthe = open('labyrinthe.txt', "r")
indiceLigne = 0
# On boucle sur toutes les lignes du fichier
for ligne in fichierLabyrinthe:
    # on initialise une nouvelle ligne pour le labyrinthe
    ligneLabyrinthe = [];
    indiceColonne = 0
    # On boucle sur les colonnes de la ligne (-, S, T, M, J)
    for colonne in ligne:
        # Si on a un "-" ça sera un mur
        if (colonne == "-"):
            ligneLabyrinthe.append("MUR");
        # Sinon si on a un "S" ça sera la sortie    
        elif (colonne == "S"):
            ligneLabyrinthe.append("SORTIE");
        # Sinon si on a un "T" ça sera un sablier
        elif (colonne == "T"):
            ligneLabyrinthe.append("SABLIER");
        # Sinon ça sera un couloir         
        else:
            ligneLabyrinthe.append("COULOIR");
                
        # Si on a un "M" on affiche le méchant    
        if (colonne == "M"):
            # création de l'objet méchant on l'affiche
            mechant = Mechant(fenetre, "mechant.png", indiceLigne, indiceColonne)
            # on rajoute le méchant à la liste des méchants
            listeMechants.append(mechant)
        # Si on a un "J" ça sera le joueur
        elif (colonne == "J"):
            # création de l'objet joueur
            joueur = Joueur(fenetre, "joueur.png", "joueurvide.png", indiceLigne, indiceColonne)
                 
        indiceColonne = indiceColonne + 1

    # on rajoute la ligne dans le tableau pour le labyrinthe pour pouvoir ensuite générer le labyrinthe
    tableauLabyrinthe.append(ligneLabyrinthe);
    indiceLigne = indiceLigne + 1   
        
# on ferme le fichier        
fichierLabyrinthe.close()

# On génère le labyrinthe
labyrinthe.genererLabyrinthe(tableauLabyrinthe)
# On affiche le joueur dans le labyrinthe
joueur.afficherDepartJoueur()

partieTermine = False
partieQuitter = False
# le temps maximum pour sortir sera de 60s
tempsMaximum = 60

# on cré un fond
fond = pygame.Surface(fenetre.get_size())

# on boucle tant qu'on a pas fini la partie
while partieTermine == False:
    # on choisit la couleur du fond
    fond.fill((0, 200, 255))
    # on positionne le fond à la position x=670 y=0
    fenetre.blit(fond, (672, 0))
    
    # on affiche LabyLu à la position x=747 y=100
    texte = police.render("Jeu LabyLu", True, (215, 250, 51))
    fenetre.blit(texte,(747, 100))
    
    # on calcule le temps restant, on divise par 1000 parceque get_ticks retourne un temps en ms
    secondesRestantes = tempsMaximum - int((pygame.time.get_ticks() - debutProgrammeEnMs) / 1000)
    
    # si on a plus de temps on a perdu, la partie est terminé
    if (secondesRestantes == 0):
        # on affiche Perdu en rouge à la position x=750 y=500
        texte = police.render("Perdu !!!", True, (255, 51, 73))
        fenetre.blit(texte,(750, 500))
        partieTermine = True       
    
    keys = pygame.key.get_pressed()
    pygame.event.get()
    
    # Si le joueur appuie sur la flèche gauche il se déplace vers la gauche
    if keys[pygame.K_LEFT] :
         joueur.deplacerGauche(labyrinthe.positionsBlocMurs)
    # Si le joueur appuie sur la flèche droite il se déplace vers la droite        
    elif keys[pygame.K_RIGHT] :
         joueur.deplacerDroite(labyrinthe.positionsBlocMurs )
    # Si le joueur appuie sur la flèche droite du haut il se déplace vers le haut        
    elif keys[pygame.K_UP] :
        joueur.deplacerHaut(labyrinthe.positionsBlocMurs )
    # Si le joueur appuie sur la flèche droite du bas il se déplace vers le bas         
    elif keys[pygame.K_DOWN] :
        joueur.deplacerBas(labyrinthe.positionsBlocMurs )
    # Si le joueur appuie sur la touche Q (clavier qwerty) on arrêtera le programme    
    elif keys[pygame.K_a] :
        partieTermine = True
        partieQuitter = True
            
    # Si il y a collision du joueur avec la sortie alors il a gagné            
    if (labyrinthe.detecterCollisionSortie(joueur.positionJoueur) == True):
        # on affiche Gagné bravo !!! en bleu à la position x=700 y=500, la partie est terminé
        texte = police.render("Gagné bravo !!!", True, (54, 51, 255))
        fenetre.blit(texte,(700, 500))
        partieTermine = True

    # Si il y a collision du joueur avec un sablier on rajoute 10s à son temps        
    if (labyrinthe.detecterCollisionSablier(joueur.positionJoueur) == True):
        tempsMaximum = tempsMaximum + 10

    # on boucle sur tout les méchants
    for mechant in listeMechants:    
        # on déplace le méchant dans le labyrinthe en lui passant tout les obstacles position des murs, sabliers et porte
        mechant.gererDeplacement(labyrinthe.positionsBlocMurs + labyrinthe.positionsSabliers + [labyrinthe.positionSortie])
        # on vérifie si il y a collision du méchant avec le joueur
        collisionAvecMechant = mechant.detecterCollision(joueur.positionJoueur)
        # si y a collision du machant avec le joueur, le joueur perd une vie
        if (collisionAvecMechant == True):
            # le joueur perd une vie
            nombreVie = nombreVie - 1
            # si le joueur n'a plus de vie est a perdu, le jeu s'arrête
            if (nombreVie == 0):
                # on affiche Perdu en rouge à la position x=750 y=500
                texte = police.render("Perdu !!!", True, (255, 51, 73))
                fenetre.blit(texte,(750, 500))
                # la boucle va s'arrêter
                partieTermine = True
            else:
               # si il reste des vies au joueur on remet le joueur au départ
               joueur.afficherDepartJoueur()

    # on affiche le nombre de vie en violet du joueur à la position x=750 y=300
    texte = police.render("Vie : " + str(nombreVie), True, (153, 51, 255))
    fenetre.blit(texte,(750, 300))
    # on affiche le temps restant en violet au joueur à la position x=750 y=400    
    texte = police.render("Reste : " + str(secondesRestantes) + "s", True, (153, 51, 255))
    fenetre.blit(texte,(750, 400))
    # pause de 30ms
    pygame.time.delay(30)
    # on raffraichit l'écran
    pygame.display.flip()

# si on quitte le programme
if (partieQuitter == True):
  # On ferme la fenêtre    
  pygame.display.quit()
  # On quitte
  pygame.quit()     