import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import ssl
import json

class RecipeNotFound(Exception):
    pass

class Marmiton(object):
	@staticmethod
	def search(query_dict):
		"""
		Search recipes parsing the returned html data.
		Options:
		'aqt': string of keywords separated by a white space  (query search)
		Optional options :
		'dt': "entree" | "platprincipal" | "accompagnement" | "amusegueule" | "sauce"  (plate type)
		'exp': 1 | 2 | 3  (plate expense 1: cheap, 3: expensive)
		'dif': 1 | 2 | 3 | 4  (recipe difficultie 1: easy, 4: advanced)
		'veg': 0 | 1  (vegetarien only: 1)
		'rct': 0 | 1  (without cook: 1)
		'sort': "markdesc" (rate) | "popularitydesc" (popularity) | "" (empty for relevance)
		"""
		base_url = "http://www.marmiton.org/recettes/recherche.aspx?"
		query_url = urllib.parse.urlencode(query_dict)

		url = base_url + query_url

		
		handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
		opener = urllib.request.build_opener(handler)
		response = opener.open(url)
		html_content = response.read()
	
		soup = BeautifulSoup(html_content, 'html.parser')

		search_data = []

		articles = soup.findAll("a", href=True)
		articles = [a for a in articles if a["href"].startswith("/recettes/recette_")]

		iterarticles = iter(articles)
		for article in iterarticles:
			data = {}
			try:
				data["name"] = article.find("h4").get_text().strip(' \t\n\r')
				data["url"] = article['href']
				try:
					data["rate"] = article.find("span").get_text().split("/")[0]
				except Exception as e0:
					pass
				try:
					data["image"] = article.find('img')['data-src']
				except Exception as e1:
					try:
						data["image"] = article.find('img')['src']
					except Exception as e1:
						pass
					pass
			except Exception as e2:
				pass
			if data:
				search_data.append(data)
		
		return search_data

	@staticmethod
	def _get_name(soup):
		return soup.find("h1").get_text().strip(' \t\n\r')

	@staticmethod
	def _get_ingredients(soup):
		ingredients_list = []
	
		# Trouver toutes les balises span avec la classe "card-ingredient-title"
		ingredient_titles = soup.find_all('span', class_='card-ingredient-title')
		
		for ingredient_title in ingredient_titles:
			quantity_span = ingredient_title.find('span', class_='card-ingredient-quantity')
			ingredient_quantity = quantity_span.find('span', class_='count').text.strip()
			unit = quantity_span.find('span', class_='unit').text.strip()
			ingredient_name = ingredient_title.find('span', class_='ingredient-name').text.strip()
        
        	# Créer une chaîne de caractères représentant l'ingrédient et sa quantité associée
			ingredient_string = f"{ingredient_quantity} {unit} de {ingredient_name}"
			ingredients_list.append(ingredient_string)
		return ingredients_list

	@staticmethod
	def _get_steps(soup):
		steps = []
		containers = soup.find_all("div", class_="recipe-step-list__container")
		for container in containers:
			step_paragraph = container.find("p")
			if step_paragraph:
				steps.append(step_paragraph.get_text().strip())
		return steps

	@staticmethod
	def _get_total_time(soup):
		total_time_element = soup.find("div", class_="time__total").find("div")
		if total_time_element:
			return total_time_element.get_text(strip=True)
		return None
	

	@staticmethod
	def _get_budget(soup):
		budget_tag = soup.find("i", class_="icon icon-price")
		if budget_tag:
			budget_span = budget_tag.find_next_sibling("span")
			if budget_span:
				return budget_span.get_text().strip()
		return None


	@classmethod
	def get(cls, uri):
		
		base_url = "http://www.marmiton.org"
		url = base_url + ("" if uri.startswith("/") else "/") + uri

		try:
			handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
			opener = urllib.request.build_opener(handler)
			response = opener.open(url)
			html_content = response.read()
		except urllib.error.HTTPError as e:
			raise RecipeNotFound if e.code == 404 else e
			
		soup = BeautifulSoup(html_content, 'html.parser')

		elements = [
			{"name": "name", "default_value": ""},
			{"name": "ingredients", "default_value": []},
			{"name": "steps", "default_value": []},
			{"name": "budget", "default_value": ""},
			{"name": "total_time", "default_value": ""},
		]

		data = {"url": url}
		for element in elements:
			try:
				data[element["name"]] = getattr(cls, "_get_" + element["name"])(soup)
			except:
				data[element["name"]] = element["default_value"]

		return data

def search_and_display_recipe(keywords=None):
    if not keywords:
        #Demande à l'utilisateur de saisir des mots-clés pour la recherche
        keywords = input("Entrez vos mots-clés pour rechercher une recette sur Marmiton : ")
    
    # Définit les options de la requête de recherche
    query_options = {
        "aqt": keywords,            # Les mots-clés de la recherche
        "dt": "",                   # Type de plat : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optionnel)
        "exp": "",                  # Prix du plat : 1 -> Bon marché, 2 -> Moyen, 3 -> Plutôt cher (optionnel)
        "dif": "",                  # Difficulté de la recette : 1 -> Très facile, 2 -> Facile, 3 -> Moyenne, 4 -> Avancée (optionnel)
        "veg": "",                  # Végétarien uniquement : 0 -> Faux, 1 -> Vrai (optionnel)
        "sort": ""                  # Tri : "markdesc" (note), "popularitydesc" (popularité), "" (vide pour la pertinence)
    }
    
    # Effectue la recherche de recettes avec les mots-clés saisis
    query_result = Marmiton.search(query_options)
    
    #Si des résultats sont trouvés, affiche les caractéristiques de la première recette
	
    if query_result:
        first_recipe_url = query_result[0]['url']
        return Marmiton.get(first_recipe_url)
    else:
        return None
	

#recipe_details = Marmiton.get(first_recipe_url)
#print("Caractéristiques de la recette:")
#for key, value in recipe_details.items():
#print(f"{key.capitalize()}: {value}")
#else:
#print("Aucune recette trouvée pour les mots-clés saisis.")