item1 = "East"
path = ["North", "South", "West"]

new_path = sum([[item1]], path)

print(f"path : {path}")
print(f"new_path : {new_path}")

list1 = [1, 2, 3, 4]
list2 = [11, 12, 13, 14]

combined1 = list1 + list2
print(f"combined1 = {combined1}")

combined2 = sum([list2], list1)
print(f"combined2 = {combined2}")

list1.append(list2)
print(f"combined3 = {list1}")
