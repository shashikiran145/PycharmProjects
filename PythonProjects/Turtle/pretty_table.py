from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirter", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Strength", ["1000", "500", "800"])
#table.get_string(sortby="Type")
table.align = "l"
table.sortby = "Pokemon Name"
print(table)
