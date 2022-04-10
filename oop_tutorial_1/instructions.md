# Programmation orientée objet (POO)

Dans cet exo, nous allons créer et gérer divers véhicules.

## 1 - Coordonnées dans l'espace
Une position dans l'espace est définie par trois coordonnées, X (gauche/droite), Y (haut/bas) et Z (avant/arrière). Nous allons créer un objet permettant de représenter ces coordonnées : la class Vector3.

Complémeter la class Vector3:
- déclarer un constructeur prenant trois paramètres "pos_x", "pos_y" et "pos_z", initialisant trois attributs "_x", "_y" et "_z"
	```
	position = Vector3(5, 0, -10)
	```
	
- déclarer trois propriétés appelées x, y et z, retournant respectivement les attributs "_x", "_y", et "_z"
	```
	position = Vector3(5, 0, -10)
	print(position.x)  # prints "5"
	```
	
- déclarer une méthode str qui retourne une représentation d'un Vector3
	```	
	position = Vector3(5, 0, -10)
	print(position)  # prints "(x:5, y:0, z:-10)"
	```
	
## 2 - Voiture
Une voiture est un objet ayant une couleur (rouge, bleu, cyan, etc.) ainsi qu'une position dans l'espace. 
Une voiture va être représentée par la class Car.

Note: la class Color va servir d'enum pour représenter une couleur. 

Complémeter la class Car:
- déclarer un constructeur prenant un paramètre "color" représentant la couleur de la voiture
	```
	car = Car(Color.BLUE)	
	```	
	
- déclarer une propriété color retournant la couleur initialisée dans le constructeur
```	
car = Car(Color.BLUE)
print(car.color)  # prints "blue"
```

- ajouter un paramètre "position" au constructeur, et ajouter une propriété "position" à la class Car
```
position = Vector3(10, 0, -5)
car = Car(Color.BLUE, position)
print(car.position)  # prints "(x:10, y:0, z:-5)"
```

- pour pouvoir faire avancer une voiture, ajouter une méthode "move_forward", qui incrémente la position d'une voiture de 1 sur la coordonnée Z.
```
position = Vector3(10, 0, -5)
car = Car(Color.BLUE, position)
print(car.position)  # prints "(x:10, y:0, z:-5)"
car.move_forward()
print(car.position)  # prints "(x:10, y:0, z:-4)"
```

- déclarer une méthode str qui retourne une représentation de Car
```
position = Vector3(10, 0, -5)
car = Car(Color.BLUE, position)
print(car)  # prints "Blue car at (x:10, y:0, z:-5)"
car.move_forward()
print(car)  # prints "Blue car at (x:10, y:0, z:-4)"
```

- dans le main, créer une list appelée "vechicles"
- ajouter à cette list 3 voitures avec des couleurs variées et des coordonnées arbitraires, mais en les gardant au sol (Y à 0)
- dans le main, faire avancer ces voitures en n'écrivant la méthode move_forward qu'une seule fois, et printer chaque voiture après qu'elles aient bougé


## 3 - Bus
Un bus est un véhicule ayant également une couleur et une position dans l'espace, comme les voitures. Un bus avance comme une voiture (en incrémentant sa position de 1 sur la coordonnée Z). Cependant, une voiture n'a que 4 places assises, alors qu'un bus peut avoir entre 20 et 70 places assises.

Compléter la class Car:
- déclarer une propriété seat_cout qui renvoie la valeur 4

Compléter la class Bus:
- déclarer un constructeur prenant trois paramètre color, position, et seat_count
- déclarer trois propriétés color, position et seat_count retournant les valeurs initialisées dans le constructeur
- déclarer une méthode move_forward qui incrément la position d'un bus de 1 sur la coordonnée Z
- déclarer une méthod str qui retourne une représentation de bus

```
position = Vector3(10, 0, -5)
car = Bus(Color.BLUE, position)
print(car)  # prints "Blue car at (x:10, y:0, z:-5)"
car.move_forward()
print(car)  # prints "Blue car at (x:10, y:0, z:-4)"
```

Constater que du code se retrouve dupliqué. Si move_forward doit être renommée "go_forward" par exemple, il est nécessaire de faire des changements répétitif à plusieurs endroits (dans Car et Bus). Le même problème est présent si la propriété "position" doit être renommée en "location". 

Pour éviter ces problèmes, nous allons utiliser l'héritage.

Une voiture est un Véhicule, et un bus est également un Véhicule.

- Déclarer une class Vehicle
- Déclarer un constructeur prenant trois paramètres color, position, et seat_count
- Déclarer une méthode "move_forward", qui incrémente la position d'un Vehicle de 1 sur la coordonnée Z
- Faire hériter Bus de Vehicle, et supprimer les propriétés et les méthodes de la class Bus
- Déclarer un constructeur de Bus prenant trois paramètre color, position, et seat_count, et simplement appeler le constructeur de la class Vehicle pour lui laisser faire tout le travail d'initialisation
- (optionnel) Avant d'appeler le constructeur de Vehicle depuis le constructeur de Bus, vérifier que seat_count est bien compris entre 20 et 70
- Faire hériter Car de Vehicle, et supprimer les propriétés et les méthodes de la class Car
- Déclarer un constructeur de Car prenant deux paramètre color, position, et appeler le constructeur de Vehicle en lui passant la valeur 4 pour le paramètre seat_count 
- Dans le main, ajouter un bus rouge de 50 places à la liste "vehicles"


## 4 - Batmobile
La batmobile est une voiture pouvant voler.

- Déclarer une class Batmobile
- Faire en sorte qu'une Batmobile hérite des même comportements de base qu'une Voiture
- Faire en sorte qu'une Batmobile soit forcément de couleur noire
- Ajouter une méthode take_off() mettant la position Y de la batmobile à 10, et la faisant avancer de 10 en avant
- Surcharger la méthode str pour qu'elle renvoie "Batmobile " suivi de sa position


## 5 - Station essence
Un véhicule consomme de l'essence.
- Dans le constructeur de Vehicle, ajouter l'initialisation d'un attribut "_gas" de telle sorte qu'il ait toujours la valeur 10.
- Modifier la méthode move_forward pour qu'elle diminue "_gas" de 1 à chaque appel, et que si "_gas" est à zéro, le vehicule n'avance pas (reste à la même position).
- Ajouter une method refill_tank() qui remet "_gas" à 10.

Une station essence peut faire le plein d'un véhicule, mais que si celui-ci est de la même couleur que la station essence. C'est idiot, mais c'est la loi dans un monde où il y a des Batmobiles.

- Déclarer une class GasStation, avec un constructeur prenant la couleur d'affiliation de la station essence
- Ajouter une méthode "refill" prenant en paramètre un véhicule, et ne remplissant le réservoir de ce vehicule que si sa couleur est identique à celle de la Station

