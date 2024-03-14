# Challenge_IA - Master SISE 2024

## Réalisé par :

- Adrien CASTEX
- Paule Naomi KALDJOB 
- Albane NICOULLAUD
- Natacha PEREZ

## Enseignant : 

M. Ricco RAKOTOMALALA

## Introduction : 

Dans le cadre de notre challenge de fin d'année, nous avons dû réaliser une application IA qui permet le traitement de données non-structurées (images). Pour cela, nous avons décidé de créer une application permettant aux utilisateurs de retrouver des recettes de plats qu'ils ont vus dans la journée, et de les guider vers le supermarché le plus proche de leur position s'ils n'ont pas tous les ingrédients.

Notre modèle ne reconnaît que les plats de pâtes, de pizzas et les glaces.

## Guide d'installation :

Assurez-vous que Docker-desktop est installé sur votre machine. Si ce n'est pas le cas, téléchargez et installez Docker depuis : https://www.docker.com/get-started/ site officiel de Docker.
Ouvrez un terminal et exécutez la commande suivante pour télécharger l'image Docker de l'application:

**docker pull natachaperez/stest:0.1**

Exécutez l'application Streamlit dans un conteneur Docker en utilisant la commande suivante:

**docker run --rm -p 8501:8501 -it natachaperez/stest:0.1**

## Guide d'utilisation : 

Une fois que vous avez suivi le guide d'installation, l'application se lance automatiquement. 
Vous avez à disposition une barre de menu située sur la gauche de la page, vous permettant de naviguer dans les différents onglets de l'application que nous allons vous présenter ci-dessous.

### Page d'acceuil :

Cette première page vous présente l'objectif du challenge:

![Texte alternatif](chemin/vers/image.png)

### Page Importation d'image :

Vous pouvez ici télécharger une image du plat qui vous intéresse, notre modèle affichera ensuite le type de plat qu'il s'agit (pâte, pizza ou glace).
Ensuite, vous avez la possibilité de préciser la recette que vous souhaitez. Par exemple : J'ai une photo de pâtes que l'application a reconnue et je souhaite qu'elle me retourne une recette de pâtes au pesto.
Une fois cette spécification réalisée, vous avez le nom, le temps de préparation, le budget, les ingrédients et les différentes étapes de la recette..

![Texte alternatif](chemin/vers/image.png)
### Page Cartographie:

Ici, vous n'avez qu'à entrer l'adresse à laquelle vous vous trouvez et l'application vous montre l'ensemble des supermarchés proches de vous. La carte affichée met en avant le magasin le plus proche et l'itinéraire à prendre pour vous y rendre.

![Texte alternatif](chemin/vers/image.png)
