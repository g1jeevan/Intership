import employee_file as employee_class
import library_file as library_class

employee_object = employee_class.Employee()
library_object = library_class.Book()


class Menu:

    def library_first_page(self):
        while True:
            print("")
            print(":::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("::::: Library Management System :::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("")
            print("1. Add Book ")
            print("2. Issue a Book ")
            print("3. Check Book Availability  ")
            print("4. Return a Book ")
            print("5. Check an Employee Status & Mail employee if he is having due amount")
            print("6. Exit")
            print("")
            print(":::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("")
            choice = int(input("Enter the choice : "))
            if choice == 1:
                library_object.create_book_table()
                library_object.add_book_details()
            elif choice == 2:
                library_object.create_issue_table()
                library_object.issue_a_book()
            elif choice == 3:
                library_object.check_book_availability_direct()
            elif choice == 4:
                library_object.return_a_book()
            elif choice == 5:
                employee_object.check_employee_status()
            elif choice == 6:
                break
        self.main_first_page()

    def employee_first_page(self):
        while True:
            print("")
            print(":::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("::::: Employee Management System ::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("")
            print("1. Add Employee ")
            print("2. View All Employee")
            print("3. Exit")
            print("")
            print(":::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("")
            choice = int(input("Enter the choice : "))
            if choice == 1:
                employee_object.create_employee_table()
                employee_object.insert_employee_details()
            elif choice == 2:
                employee_object.view_all_employee()
            elif choice == 3:
                break
        self.main_first_page()

    def main_first_page(self):

        while True:
            print("")
            print(":::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::")
            print("1. Library Management ")
            print("2. Employee Management ")
            print("3. Exit")
            print(":::::::::::::::::::::::::::::::::::::")
            print(":::::::::::::::::::::::::::::::::::::")
            choice = int(input("Enter choice : "))
            if choice == 1:
                self.library_first_page()
            elif choice == 2:
                self.employee_first_page()
            elif choice == 3:
                break


if __name__ == '__main__':
    menu_object = Menu()
    menu_object.main_first_page()
