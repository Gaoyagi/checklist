checklist = list()

#CRUD functions
#C-create
def create(item):
    checklist.append(item)
#R-read
def read(index):
    mark_as_complete(int(index))
    return checklist[int(index)]
#U-update
def update(index, item):
    checklist[int(index)] = item
#D-destroy
def destroy(index):
    checklist.pop(int(index))

#list printer function
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_as_complete(index):
    checklist[int(index)] = "√" + checklist[int(index)]

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        return True

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?: ")
        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))
        return True

    # Print all items
    elif function_code == "P":
        list_all_items()
        return True

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    create("black shoes")
    create("purple sox")
    create("red cloak")
    create("blue shirt")
    create("orange button")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit: \n")
    running = select(selection)
#python3 checklist.py
