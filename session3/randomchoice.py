from random import choice
menu = ["rice", "kebab", "sushi", "girls"]
random_item = choice(menu)
menu.remove(random_item)
print(*menu, sep=", ")
