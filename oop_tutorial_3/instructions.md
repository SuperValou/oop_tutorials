# OOP 3

On va plonger dans la séparation des responsabilités en créant un mini-jeu.

## Prérequis

Une application est un peu comme un restaurant. Quand vous allez au restaurant, vous n'intéragissez jamais avec le cuisinier, alors que c'est pourtant lui qui prépare votre plat. Techniquement, vous pourriez débarquer en cuisine et manger directement debout au milieu des casseroles, ça marcherait très bien, mais ce serait désagréable pour tout le monde et très vite ingérable avec plusieurs clients.

Vous, vous interagissez avec un serveur, qui s'assure que vous soyez bien installé et que vous avez tout ce qu'il vous faut. Ce serveur s'occupe également d'intéragir avec la cuisine afin de vous apporter votre plat, et de vous débarrasser quand vous avez fini. Ainsi, vous n'avez jamais à mettre les pieds en cuisine.

Il y a une séparation des responsabilités : le serveur s'occupe de vous, et le cuisinier s'occupe des plats.

L'intérêt évident de séparer les responsabilités, c'est que le cuisinier peut se concentrer pleinement sur son travail sans s'inquiéter de savoir si un client veut une autre corbeille de pain ou trouve que la clim est trop forte et que ça lui casse la voix. Inversement, un serveur n'a pas à se préoccuper de la température des fourneaux ni du nombre de casseroles disponibles en cuisine. D'ailleurs, une majorité de serveurs ne sait probablement même pas cuisiner tout court.

Séparer les responsabilités permet donc à chacun d'avoir un minimum de préoccupation, tout en pouvant s'y consacrer au maximum.

Un autre bénéfice est qu'un serveur peut être intervertit avec un autre serveur, ça n'a aucun impact sur la façon dont le cuisinier travaille. L'organisation devient donc modulaire.

Dans une application, il y a donc une interface utilisateur, la UI ("you-aïe"), qui a pour préoccupation d'afficher des choses à l'utilisateur, de récupérer ses inputs, et de lui re-présenter des choses en fonction de ces inputs. 
Tout ce qu'on appelle la logique métier (la cuisine), qui consiste à manipuler des données, faire des calculs, créer des objets, doit être distinctement séparé de la UI, dont ce n'est pas le rôle. Ainsi, on pourra par la suite facilement changer de UI, sans impacter les fonctionnalités de l'application.

### Code

Pour itérer de 0 à 100:
```python
for i in range(0, 100):
	print(i)
```

Pour balancer une erreur et arrêter le programme:
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

### Echauffement

- Exécuter le programme pour s'assurer qu'il dit bien bonjour



### ?


#### 1 - ?



- Implémenter initialize()
> Note: Pensez à assigner les champs concernant les joueurs et à remplir la grille avec le CellSymbol vide.

- Implémenter swap_player()

- Implémenter is_filled()
> Note: 

- Implémenter get_player_symbol()
> Note: vous devez renvoyer l'une des constantes de la class CellSymbol en fonction du nom du joueur. Vous pouvez considérer que la première personne qui joue utilise forcément les X, et la personne suivante les O.

- Implémenter play_move()
> Astuce: le paramètre de la fonction indique où placer le symbole du joueur courant. Notez qu'il est interdit de placer un symbole en dehors de la grille, ou de recouvrir un symbole déjà placé.

- Implémenter la méthode is_won_by()
> Astuce: au lieu d'essayer de tout écrire d'un coup, procédez par étapes.
Vous pouvez commencez par renvoyer True si juste la première ligne est occupée par le symbole du joueur,  et vérifier que ce cas-là fonctionne correctement. 
Ensuite, vous pouvez faire en sorte de vérifier la même chose pour toutes les lignes horizontales. 
Ensuite, pareil pour une colonne, puis les trois colonnes, puis les diagonales.
Si vous en avez envie, vous pouvez faire des fonctions séparées pour différent cas.
Notez qu'il y a plusieurs façons possibles de résoudre ce problème, à vous de trouver celle qui vous convient.

- Implémenter display_game_over()
> Note: affichez le nom du gagnant ou indiquez qu'il y a match nul



# Tests
> Note: pour ces tests, une phrase telle que "Jouer 0, 4, 8" signifie "Player One rentre 0, puis Player Two rentre 4, puis Player One rentre 8"

- Jouer 0, 8, 1, 7, 2, et vérifier que le joueur 1 l'emporte (ligne du haut)
- Jouer 1, 0, 2, 3, 4, 6 et vérifier que le joueur 2 l'emporte (colonne de gauche)
- Jouer 2, 0, 8, 4, 5 et vérifier que le joueur 1 l'emporte (colonne de droite)
- Jouer 4, 0, 2, 1, 6 et vérifier que le joueur 1 l'emporte (diagonale / )
- Jouer 2, 0, 3, 4, 5, 8 et vérifier que le joueur 2 l'emporte (diagonale \ )

- Jouer 1, 0, puis rentrer 'quit' et vérifier que le programme s'arrête sur un match nul

- Jouer 0, 0, et vérifier que le programme s'arrête avec une erreur indiquant qu'il est interdit de recouvrir un symbole déjà placé

- Jouer, 4, 1, 'oups' et vérifier que le programme affiche un message en continuant normalement





