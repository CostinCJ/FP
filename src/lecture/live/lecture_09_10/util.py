from lecture.live.lecture_09_10.domain.ingredient import Ingredient
from lecture.live.lecture_09_10.domain.recipe import Recipe
from lecture.live.lecture_09_10.domain.stock import Stock


def create_ingredients():
    ingr = {}
    ingr[100] = Ingredient(100, "Bread Flour (White, 550)")
    ingr[101] = Ingredient(101, "Yeast (dry)")
    ingr[102] = Ingredient(102, "Sugar (white)")
    ingr[103] = Ingredient(103, "Salt (regular)")
    ingr[104] = Ingredient(104, "Oil (canola)")
    ingr[105] = Ingredient(105, "Butter")
    ingr[106] = Ingredient(106, "Egg (chicken)")
    ingr[107] = Ingredient(107, "Cake flour")
    ingr[108] = Ingredient(108, "Baking powder")
    ingr[109] = Ingredient(109, "Vanilla (extract)")
    return ingr


def create_stocks():
    ingredients = create_ingredients()
    stocks = {}

    for ingredient in ingredients.values():
        stocks[ingredient.id] = Stock(ingredient.id, ingredient, 1000)
    return stocks


def create_recipes():
    ingredients = create_ingredients()

    """
    Bread

    1 package (1/4 ounce) active dry yeast
    2-1/4 cups warm water (110° to 115°)
    3 tablespoons sugar plus 1/2 teaspoon sugar
    1 tablespoon salt
    2 tablespoons canola oil
    6-1/4 to 6-3/4 cups bread flour
    source: https://www.tasteofhome.com/recipes/basic-homemade-bread/
    """
    # TODO How do we fix that Stock instances have the same id's as Ingredient instances?
    recipe_bread = Recipe(500, "Basic Homemade Bread")
    recipe_bread.stocks.append(Stock(101, ingredients[101], 20))
    recipe_bread.stocks.append(Stock(102, ingredients[102], 30))
    recipe_bread.stocks.append(Stock(103, ingredients[103], 5))
    recipe_bread.stocks.append(Stock(104, ingredients[104], 10))
    recipe_bread.stocks.append(Stock(100, ingredients[100], 1000))

    """
    Cake recipe
    
    175g (6oz) margarine or softened butter
    175g (6oz) caster sugar
    3 large eggs
    175g (6oz) self-raising flour, sifted
    1tsp baking powder
    1tsp vanilla extract
    pinch of salt
    source: https://www.houseandgarden.co.uk/recipe/simple-vanilla-cake-recipe
    """
    recipe_cake = Recipe(501, "Tasty Cookies")
    recipe_cake.stocks.append(Stock(105, ingredients[105], 175))
    recipe_cake.stocks.append(Stock(102, ingredients[102], 175))
    recipe_cake.stocks.append(Stock(106, ingredients[106], 3))
    recipe_cake.stocks.append(Stock(107, ingredients[107], 175))
    recipe_cake.stocks.append(Stock(108, ingredients[108], 5))
    recipe_cake.stocks.append(Stock(109, ingredients[109], 5))
    recipe_cake.stocks.append(Stock(103, ingredients[103], 2))

    return [recipe_bread, recipe_cake]


if __name__ == "__main__":
    recipes = create_recipes()
    print(recipes)