import sys
import random

class Jeu:
    def __init__(self):
        self.position = "entrée"
        self.sante = 100
        self.game_over = False

    def afficher_message(self, message):
        print(message)
    
    def afficher_menu(self):
        print("\nQue voulez-vous faire ?")
        print("1. Avancer")
        print("2. Regarder autour de vous")
        print("3. Vérifier votre santé")
        print("4. Quitter")
    
    def avancer(self):
        if self.position == "entrée":
            self.position = "passage interdit"
            self.afficher_message("Vous êtes à l'entrée d'une ancienne forêt. Deux passages s'offrent à vous.")
            self.afficher_message("Un passage à droite est marqué 'Interdit'. L'autre semble normal.")
            self.afficher_message("Que ferez-vous ?")
        elif self.position == "passage interdit":
            self.afficher_message("Le passage interdit est bloqué par un mur d'herbes denses.")
            self.afficher_message("Il n'y a aucun moyen de passer. Il vous faut choisir un autre chemin.")
        elif self.position == "passage sens unique":
            self.position = "nouveau chemin"
            self.afficher_message("Vous avez traversé un tunnel étroit et êtes maintenant dans un autre monde.")
            self.afficher_message("Il n'y a plus de retour possible.")
            self.sante -= 20
            self.afficher_message("Votre santé a diminué à cause de la fatigue. Santé restante : {}".format(self.sante))
        elif self.position == "nouveau chemin":
            self.afficher_message("Vous êtes dans un endroit étrange. La nature semble différente.")
            self.afficher_message("Vous ne pouvez pas revenir en arrière. Explorez ce nouvel environnement.")
        else:
            self.afficher_message("Il n'y a plus d'endroit à explorer.")
    
    def regarder(self):
        if self.position == "entrée":
            self.afficher_message("Vous êtes à l'entrée d'une forêt sombre. Vous pouvez apercevoir deux passages.")
        elif self.position == "passage interdit":
            self.afficher_message("Le passage interdit est barricadé et marqué de signes mystiques. Impossible de le franchir.")
        elif self.position == "passage sens unique":
            self.afficher_message("Vous avez franchi un passage étroit. Il y a un sentiment de perte et d'épuisement.")
        elif self.position == "nouveau chemin":
            self.afficher_message("Vous êtes maintenant dans un endroit calme, mais une étrange brume s'élève autour de vous.")
    
    def verifier_sante(self):
        self.afficher_message("Votre santé actuelle est de {} points.".format(self.sante))
        if self.sante <= 0:
            self.afficher_message("Vous êtes trop épuisé pour continuer. Vous avez perdu la partie.")
            self.game_over = True
    
    def quitter(self):
        self.afficher_message("Merci d'avoir joué ! À bientôt.")
        self.game_over = True
    
    def command_vide(self):
        self.afficher_message("Vous n'avez rien fait... Essayez d'entrer une commande valide.")
    
    def choisir_passage(self):
        self.afficher_message("\nQuel passage voulez-vous prendre ?")
        self.afficher_message("1. Passage interdit")
        self.afficher_message("2. Passage à sens unique")
        passage_choisi = input("Votre choix : ").strip()
        
        if passage_choisi == "1":  # Passage interdit
            self.afficher_message("Vous tentez d'entrer dans le passage interdit, mais un mur magique apparaît et vous bloque l'entrée.")
            self.afficher_message("Vous devez choisir un autre passage.")
            self.position = "entrée"
        elif passage_choisi == "2":  # Passage à sens unique
            self.position = "passage sens unique"
            self.afficher_message("Vous entrez dans un tunnel étroit et sombre. Vous ne pouvez plus revenir.")
        else:
            self.afficher_message("Commande non reconnue, essayez encore.")

    def jouer(self):
        while not self.game_over:
            self.afficher_menu()
            commande = input("Votre choix : ").strip().lower()
            
            if commande == "1":  # Avancer
                if self.position == "entrée":
                    self.choisir_passage()
                else:
                    self.avancer()
            elif commande == "2":  # Regarder autour de vous
                self.regarder()
            elif commande == "3":  # Vérifier votre santé
                self.verifier_sante()
            elif commande == "4":  # Quitter le jeu
                self.quitter()
            elif commande == "":  # Commande vide
                self.command_vide()
            else:
                self.afficher_message("Commande non reconnue. Essayez encore.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()