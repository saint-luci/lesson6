#dicts
my_dict = {"Swiat": 2004, "Max": 2008, "Egor": 1986}
print("Dict:", my_dict)
print("Existing key:", my_dict.get("Swiat"))
print("None existing key:", my_dict.get("Papa", "This key is none"))
my_dict.update({"Papa": 1400, "Anna": 1900})
element = my_dict.pop("Swiat")
print("Deleted value:", element)
print("Modified dict:", my_dict)

print('\n')

#sets
my_set = {1, 2, 1, 2, False, False, "12", "12"}
print("Set:", my_set)
my_set.discard(False)
print("Modified set:", my_set)