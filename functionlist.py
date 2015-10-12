shopping_list= []

def show_help():
    print("what we should pick up the store?  ")
    print("Enter DONE to stop.")


def add_to_list(item):
    shopping_list.append(item)
    print("Added! list has {} items".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

show_help()

while True:
    new_item = input(">")
    if new_item == 'DONE':
        break
    add_to_list(new_item)
    continue
show_list()



