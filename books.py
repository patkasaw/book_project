import menu_functions

def menu():
    is_running = True

    while is_running:
        print()
        print('💫Menu💫')
        print('1. Add Book')
        print('2. Show all books')
        print('3. Update book')
        print('4. Delete Book')
        print('5. Show books statistics')
        print('6. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            menu_functions.add_book()

        elif choice == '2':
            menu_functions.show_books()
            
        elif choice == '3':
            menu_functions.update_book()

        elif choice == '4':
            menu_functions.delete_book()

        elif choice == '5':
            menu_functions.show_statistics()

        elif choice == '6':
            is_running = menu_functions.exit_app()
        
        else:
            print('Invalid choice. Please try again.')        
                           
menu()



    


