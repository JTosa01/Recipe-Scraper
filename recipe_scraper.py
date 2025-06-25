import curl_cffi
from bs4 import BeautifulSoup


#URL = "https://www.budgetbytes.com/creamy-garlic-chicken/"
#URL = "https://www.tamingtwins.com/marry-me-chicken/"
URL = input("Enter the URL of the recipe: ")

#page = requests.get(URL)
page = curl_cffi.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
recipe_block = soup.find("div", class_="wprm-recipe-container")

ingredients = recipe_block.find_all("li", class_="wprm-recipe-ingredient")
print("INGREDIENTS:\n")

for ingredient in ingredients:
    ingredient_names = ingredient.find("span", class_="wprm-recipe-ingredient-name")
    ingredient_quantities = type('',(object,),{"text": ""})() if ingredient.find("span", class_="wprm-recipe-ingredient-amount") is None else ingredient.find("span", class_="wprm-recipe-ingredient-amount")
    ingredient_units = type('',(object,),{"text": ""})() if ingredient.find("span", class_="wprm-recipe-ingredient-unit") is None else ingredient.find("span", class_="wprm-recipe-ingredient-unit")
    print(f"{ingredient_quantities.text.strip()} {ingredient_units.text.strip()} {ingredient_names.text.strip()}")

instructions = recipe_block.find_all("li", class_="wprm-recipe-instruction")
print("\n\nINSTRUCTIONS:\n")

for n in range(len(instructions)):
    instruction_text = instructions[n].find("div", class_="wprm-recipe-instruction-text")
    if instruction_text:
        print("Step", str(n), ": ", instruction_text.text.strip(), end="\n" * 2)
    else:
        print("No instruction text found.")

