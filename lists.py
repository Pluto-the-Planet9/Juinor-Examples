breakfest_items = ["frootloops" , "raisin bran" , "frosted flakes" , "fruity pebbles" , "coco pebbles" , "capn crunch"]

print(breakfest_items)
print(breakfest_items[2])
breakfest_items.append("frosted mono wheats")
breakfest_items.append("golden grahams")

print(breakfest_items)
breakfest_items.sort()
print(breakfest_items)
breakfest_items.remove(breakfest_items[2])
breakfest_items.remove("coco pebbles")
print(breakfest_items)

total_cereal_items = len(breakfest_items)
print(f"The total items we have for cereal are: {total_cereal_items}")
