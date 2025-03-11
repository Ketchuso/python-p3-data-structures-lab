spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for item in spicy_foods:
        names.append(item.get("name"))
    return names

def get_spiciest_foods(spicy_foods):
    spicy = []
    for item in spicy_foods:
        if item["heat_level"] > 5:
            spicy.append(item)
    return spicy

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        spice_level = '🌶' * item["heat_level"]
        print(f'{item["name"]} ({item["cuisine"]}) | Heat Level: {spice_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"] == cuisine:
            return item

def print_spiciest_foods(spicy_foods):
    spicy = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy)

def get_average_heat_level(spicy_foods):
    sum = 0
    for item in spicy_foods:
        sum += item["heat_level"]
    return (sum / 3)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
