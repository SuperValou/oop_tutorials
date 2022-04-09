# OOP 3

On va plonger dans la séparation des responsabilités en créant un mini-jeu.


### Introduction

Une application est un peu comme un restaurant. Quand vous allez au restaurant, vous n'intéragissez jamais avec le cuisinier, alors que c'est pourtant lui qui prépare votre plat. Techniquement, vous pourriez débarquer en cuisine et manger directement debout au milieu des casseroles, ça marcherait très bien, mais ce serait désagréable pour tout le monde et très vite ingérable avec plusieurs clients.

Vous, vous interagissez avec un serveur, qui s'assure que vous soyez bien installé et que vous avez tout ce qu'il vous faut. Ce serveur s'occupe également d'intéragir avec la cuisine afin de vous apporter votre plat, et de vous débarrasser quand vous avez fini. Ainsi, vous n'avez jamais à mettre les pieds en cuisine.

Il y a une séparation des responsabilités : le serveur s'occupe de vous, et le cuisinier s'occupe des plats.

L'intérêt évident de séparer les responsabilités, c'est que le cuisinier peut se concentrer pleinement sur son travail sans s'inquiéter de savoir si un client veut une autre corbeille de pain ou trouve que la clim est trop forte et que ça lui casse la voix. Inversement, un serveur n'a pas à se préoccuper de la température des fourneaux ni du nombre de casseroles disponibles en cuisine. D'ailleurs, une majorité de serveurs ne sait probablement même pas cuisiner tout court.

Séparer les responsabilités permet donc à chacun d'avoir un minimum de préoccupation, tout en pouvant s'y consacrer au maximum.

Un autre bénéfice est qu'un serveur peut être intervertit avec un autre serveur, ça n'a aucun impact sur la façon dont le cuisinier travaille. L'organisation devient donc modulaire.

Dans une application, il y a donc une interface utilisateur, la UI ("you-aïe"), qui a pour préoccupation d'afficher des choses à l'utilisateur, de récupérer ses inputs, et de lui re-présenter des choses en fonction de ces inputs. 
Tout ce qu'on appelle la logique métier (la cuisine), qui consiste à manipuler des données, faire des calculs, créer des objets, doit être distinctement séparé de la UI, dont ce n'est pas le rôle. Ainsi, on pourra par la suite facilement changer de UI, sans impacter les fonctionnalités de l'application.


### Présentation du projet

Nous allons programmer un tic-tac-toe, ce jeu très simple où deux joueurs tentent d'aligner respectivement trois X ou trois O dans une grille de 3x3.

Pour que l'exercice ne soit pas trop difficile, un squelette de code est déjà étayé. Dans les fichiers fournis, vous trouverez donc :
- main.py, contenant un main (le programme principal à executer)
- game.py, contenant:
	- la classe TicTacToeGame, contenant la logique du jeu, qu'il va falloir compléter 
	- la classe CellSymbol, qui sert simplement d'enum pour représenter un X / un O / une case vide
- ui.py, contenant la class UserInterface, qu'il va falloir compléter


### Echauffement

- Exécuter le programme pour s'assurer qu'il ne fait pas grand chose de formidable. Et c'est déjà mieux que crasher, figurez-vous.

> Note: ne taper aucun nom pour un joueur équivaut à taper la string "Player 1" ou "Player 2" par défaut. Pour le moment, ça ne change rien, mais vous trouverez vite ça pratique pour vos tests sur la durée.

- Lisez le code de TicTacToeGame :
	- Déterminez ce qu'il se passe dans le constructeur
	- Notez quelles sont les propriétés disponibles. Ces propriétés font partie de ce qui est exposé vers l'exterieur, c'est-à-dire que UserInterface aura certainement intérêt à faire appel à ces propriétés de TicTacToeGame.
	- Notez quelles sont les méthodes disponibles. De même, toute méthode qui ne commence par par un "_" pourra être appelée par UserInterface, ce qui lui sera probablement très utile.

> Remarque: une convention en Python est qu'une méthode commençant par un "_" n'est pas censée être utilisée depuis l'exterieur, seulement en interne par la classe qui la déclare.

- Lisez le code de UserInterface :
	- Déterminez ce que fait le constructeur
	- Déterminez ce qu'il se passe dans la méthode show()


> Note : si vous ne connaissez pas le mot-clé `while`, `while` execute une boucle *tant que* la condition qui lui est associée est vraie. Un `while True:` va donc tourner pour toujours, sauf si le mot clé `break` est appelé à l'intérieur (`break` stoppe immédiatement n'importe quelle boucle pour en sortir).

> Note : le mot clé `continue` permet de passer immédiatement à l'itération suivante d'une boucle en cours. Cette information est purement indicative, il n'est pas nécessaire d'utiliser de `continue` dans cet exercice, ni de toucher à ceux qui sont en place.

> Note : `try` et `except` permettent de gérer un `raise` qui aurait potentiellement lieu dans le bloc try. Il n'est pas nécessaire de s'intéresser à ça pour cet exercice.


### Snippets

Pour printer les nombres de 0 inclu à 10 inclu:
```python
for i in range(0, 11):   # range(a, b) includes a but excludes b
	print(i)
```

Pour setter le premier élément d'une liste à "hey":
```python
my_list = ["hi", "hello", "sup"]
my_list[0] = "hey"
print(my_list)  # -> ["hey", "hello", "sup"]
```

Pour déclencher une erreur qui stoppe tout le programme:
```python
if something_is_wrong:
	raise ValueError("Something went wrong!")
```

Pour sortir d'une boucle:
```python
while True:
	print("I'm in the loop")
	if i_want_to_get_out_of_the_loop:
		break
		
print("I broke out of the loop!")
```


#### 1 - Initialisation des joueurs

Dans TicTacToeGame:
- Implémenter initialize() pour que le jeu retienne le nom des joueurs, et qu'il sache qui est le joueur courant. On considère que le joueur 1 commence la partie en premier.

- Implémenter get_player_symbol(), pour renvoyer l'une des constantes de la class CellSymbol en fonction du joueur en paramètre. Vous pouvez considérer que le joueur 1 utilise les X, et le joueur 2 les O.

- Implémenter swap_player() pour que le jeu intervertisse le joueur courant avec l'autre joueur.


#### 2 - Branchement de la UI

Maintenant que notre TicTacToeGame sait au moins se souvenir du prénom de ceux qui veulent jouer, faisons appel à son savoir-faire depuis l'extérieur.

Dans la méthode show() de UserInterface:
- Repérer où on appelle la méthode initialize() de l'objet TicTacToeGame, pour avoir un exemple
- Implémenter le "# TODO: change player" pour faire véritablement le changement de joueur

- Executer le main, et vérifier que le joueur change après chaque coup


#### 3 - Jouer un coup

Le jeu est déjà incroyable en l'état, mais accrochez-vous, on peut faire encore mieux.

Dans la class TicTacToeGame : 
- Implémenter play_move(). Le paramètre de la fonction est un int, l'index de la grille où placer le symbole du joueur courant. Vous n'avez rien à modifier en dehors de cette fonction, utilisez ce dont vous disposez déjà.

Dans la class UserInterface :
- Implémenter le "# TODO: play the move"

- Executer le main, et vérifier qu'on peut désormais jouer des coups.

- Jouez toujours 4 pour les deux joueurs. Jouez 999, puis -1. Jouez 'salut'. Modifiez play_move() pour gérer les cas qui vous semblent problématiques.


#### 4 - Match nul

- Dans TicTacToeGame, implémenter is_filled() pour renvoyer si oui ou non le plateau est entièrement rempli.
- Dans UserInterface.show(), implémenter le "# TODO: check if the game can still be played" pour sortir de la boucle lorsque le plateau est rempli.
- Executer le main et remplir le plateau pour vérifier que le jeu s'arrête.

- Dans UserInterface, implémenter display_game_over() pour indiquer à l'utilisateur qu'il y a match nul.

#### 5 - Combat de titans
Il est temps de déterminer un vainqueur à ce jeu fantastique quasiment au même niveau que Fortnite.

- Dans TicTacToeGame

- Jouer 0, 8, 1, 7, 2, et vérifier que le joueur 1 l'emporte (ligne du haut)
- Jouer 1, 0, 2, 3, 4, 6 et vérifier que le joueur 2 l'emporte (colonne de gauche)
- Jouer 2, 0, 8, 4, 5 et vérifier que le joueur 1 l'emporte (colonne de droite)
- Jouer 4, 0, 2, 1, 6 et vérifier que le joueur 1 l'emporte (diagonale / )
- Jouer 2, 0, 3, 4, 5, 8 et vérifier que le joueur 2 l'emporte (diagonale \ )

- Jouer 1, 0, puis rentrer 'quit' et vérifier que le programme s'arrête sur un match nul

- Jouer 0, 0, et vérifier que le programme s'arrête avec une erreur indiquant qu'il est interdit de recouvrir un symbole déjà placé

- Jouer, 4, 1, 'oups' et vérifier que le programme affiche un message en continuant normalement





