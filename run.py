from checklist import Checklist, ChecklistItem

def main():
    c = Checklist()
    print("Welcome to the CRUD checklist!")
    print("The checklist is currently empty.")
    while True:
        choice = input("\nChoose one of the following:\n1. Add Item\n2. View All\n3. View One Item\n4. Mark Completed\n5. Mark Incomplete\n6. Edit Item\n7. Delete Item\n8. Quit Program\n")
        while choice not in {'1','2','3','4','5','6','7','8'}:
            choice = input("Please pick a valid option: ")
        if choice == '8':
            break
        elif choice == '1':
            c.create_new_item()
        elif choice == '2':
            print(c)
        elif choice == '3':
            c.view_item()
        elif choice == '4':
            c.complete_item()
        elif choice == '5':
            c.uncomplete_item()
        elif choice == '6':
            c.edit_item()
        elif choice == '7':
            c.delete_item()
    print("Thank you for using the crud checklist.")
    print("This was the final checklist:")
    print(c)

main()
        
