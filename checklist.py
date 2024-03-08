# In this project, you will create a command-line To-Do List Manager using Python. The application should allow users to add tasks, view tasks, edit task completion status, delete tasks, and quit.
import colorama


class Checklist:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        all_items = ""
        for item in self.items:
            all_items += str(item) + '\n'
        return f"""
Your Checklist:
{all_items}"""

    def __get_item_by_id(self):
        item_id = input("What item (ID) are you looking for? ")
        while not item_id.isdigit():
            item_id = input("Input a valid integer ID: ")
        item_id = int(item_id)
        for item in self.items:
            if item_id == item.item_id:
                return item
        else:
            print(f"\033[31mERROR: could not find item #{item_id}\033[39m")
            return None

    def create_new_item(self):
        print("Attempting to add a new item...")
        new_entry = input("Name your new item below:\n")
        new_item = ChecklistItem(new_entry)
        self.items.append(new_item)
        print(f"{new_item.name} has been added to the checklist.")

    def view_item(self):
        print("Attempting to view an item...")
        item = self.__get_item_by_id()
        if item:
            print(item)
        else:
            print("That could not be displayed. Moving on...")

    def edit_item(self):
        print("Attempting to edit an existing item...")
        item = self.__get_item_by_id()
        if item:
            print(item)
            confirm_edit = input("Confirm edit this item (y) ?").lower()
            if confirm_edit == 'y':
                item.name = input("Write the new name below:\n")
                print(f"The item has been edited successfully.")
            else:
                print(f"No edits were made to {item.name}")

    def complete_item(self):
        print("Attempting to complete an item...")
        item = self.__get_item_by_id()
        if item:
            print(item)
            if item.completed == False:
                confirm_complete = input("Confirm complete this item (y)? ").lower()
                if confirm_complete == 'y':
                    item.complete()
                    print(f"\033[32m{item.name}\033[39m has been marked completed")
                else:
                    print(f"No changes were made to {item.name}")
            else:
                print(f"{item.name} is already complete.")
    
    def uncomplete_item(self):
        print("Attempting to uncomplete an item...")
        item = self.__get_item_by_id()
        if item:
            print(item)
            if item.completed == True:
                confirm_complete = input("Confirm mark incomplete (y)? ").lower()
                if confirm_complete == 'y':
                    item.uncomplete()
                    print(f"\033[33m{item.name}\033[39m has been marked incomplete.")
                else:
                    print(f"No changes were made to {item.name}")
            else:
                print(f"{item.name} is already incomplete.")

    def delete_item(self):
        print("Attempting to delete an item...")
        item = self.__get_item_by_id()
        if item:
            print(item)
            confirm_del = input("Confirm deletion (y)? ").lower()
            if confirm_del == 'y':
                print(f"Deleting \033[31m{item.name}...\033[39m")
                self.items.remove(item)
            else:
                print("Cancelling deletion.")
                

# Class ChecklistItem handles individual entries in the Checklist
class ChecklistItem:
    item_id = 1
    def __init__(self, name):
        self.item_id = ChecklistItem.item_id
        ChecklistItem.item_id += 1
        self.name = name
        self.completed = False
    
    def __str__(self): # Incomplete will be colored yellow, complete colored green
        ret_str = ""
        check = " "
        if self.completed:
            check = "X"
            ret_str += '\033[32m' #GREEN
        else:
            ret_str += '\033[33m' #YELLOW
        ret_str += f"{self.item_id}. {self.name} [{check}]\033[39m"
        return ret_str
    
    def complete(self):
        self.completed = True
    
    def uncomplete(self):
        self.completed = False