shopping_list = list()

print("what should we pick up  at the store?")
print("Enter 'DONE' to stop adding items.")

while  True:
    new_item = input(">")

    if new_item == 'DONE':
        break

    shopping_list.append(new_item)
    print("Added! list has {} items. ".format(len(shopping_list)))
    continue

print("here is your list:")

for item in shopping_list:
    print(item)
