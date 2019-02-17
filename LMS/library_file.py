import db_config_file as database
from datetime import datetime
from datetime import timedelta


class Book:
    @staticmethod
    def create_book_table():
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute("CREATE TABLE IF NOT EXISTS j_book_list ( "
                              "book_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, "
                              "book_title VARCHAR(255) NOT NULL, "
                              "book_author VARCHAR(30) NOT NULL,"
                              "book_description VARCHAR(300) NOT NULL,"
                              "book_isbn VARCHAR(15) NOT NULL,"
                              "book_available VARCHAR(3) NOT NULL,"
                              "book_added_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
                              "")
        except Exception as e:
            print("Oops Something Wrong in Query Execution create_book_table ")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()
        my_cursor.close()

    @staticmethod
    def create_issue_table():
        # print("Came Here")
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute("CREATE TABLE IF NOT EXISTS j_issue_list ( "
                              "issue_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, "
                              "book_id INT(6) NOT NULL, "
                              "employee_id INT(6) NOT NULL,"
                              "issue_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
                              "issue_return_status VARCHAR(3) NOT NULL)"
                              "")
            print("Issue Table Is Created")

        except Exception as e:
            print("Oops Something Wrong in Query Execution create_issue_table")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()
        my_cursor.close()

    def add_book_details(self):
        # choice = " "
        while True:
            print("Enter the details of books : ")
            book_title = input("Title of Book : ")
            book_author = input("Author : ")
            book_description = input("Description : ")
            book_isbn = input("ISBN : ")
            book_quantity = input("Quantity : ")
            self.save_book_details_to_db(book_title, book_author, book_description, book_isbn, book_quantity)
            choice = input("Add More (y/n)")
            if choice == "n":
                break

    @staticmethod
    def save_book_details_to_db(book_title, book_author, book_description, book_isbn, book_quantity):
        str_no_of_query_execution = book_quantity
        no_of_query_execution = int(str_no_of_query_execution)
        # print("Number of query : ", no_of_query_execution)
        while no_of_query_execution >= 0:
            add_book = ("INSERT INTO j_book_list "
                        "(book_title, book_author, book_description, book_isbn, book_available) "
                        "VALUES (%s, %s, %s, %s, %s)")
            data_book = (book_title, book_author, book_description, book_isbn, 'Yes')
            my_cursor = database.my_database.cursor()
            try:
                my_cursor.execute(add_book, data_book)
            except Exception as e:
                print("Oops Something Wrong in Query Execution add_book ")
                print("Excepetion Occured ", str(e))
            database.my_database.commit()
            no_of_query_execution = no_of_query_execution - 1
            my_cursor.close()
        print("Books Added To  The Inventory Successfully !!!")

    @staticmethod
    def view_all_books():

        sql_select_all_book_query = ("SELECT book_id, book_title, book_author, book_description "
                                     "FROM j_book_list "
                                     "where book_available = 'Yes' "
                                     "ORDER BY book_title ASC LIMIT 1000")
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(sql_select_all_book_query)
            records = my_cursor.fetchall()
            print("Total number of available books in Inventory is - ", my_cursor.rowcount)
            print(": : Displaying each Books Details : : ")
            for row in records:
                print("Book Id = ", row[0], )
                print("Book Name = ", row[1])
                print("Book Author  = ", row[2])
                print("Book Description  = ", row[3], "\n")
        except Exception as e:
            print("Oops Something Wrong in Query sql_select_all_book_query")
            print("Exception Occur ", str(e))
        database.my_database.commit()
        my_cursor.close()

    def check_book_availability_direct(self):
        print("::: Check Book Availability :::")
        see_all_books = input("Do You Want to See all Available Books? (y/n): ")
        if see_all_books == 'y':
            self.view_all_books()
        book_no = input("Enter a book number : ")
        cba = self.check_book_availability(book_no)
        # print("CBAAAAAAAAAAAAA  ", cba[0])
        if cba[0] == 0:

            print(" I'm Sorry, that Book is not available :-( . Please return and check with any other books...")
        else:
            print("Yay That book is available!!!")

    @staticmethod
    def check_book_availability(issue_book_no):
        my_cursor = database.my_database.cursor()
        no_of_books_available_query = ("SELECT COUNT(*) "
                                       "FROM j_book_list "
                                       "where book_available = 'Yes' AND book_id = "
                                       "" + str(issue_book_no))
        no_of_books_available = []
        try:
            my_cursor.execute(no_of_books_available_query)
            no_of_books_available = my_cursor.fetchall()
        except Exception as e:
            print("Oops Something went wrong in the query Execution : check_book_availability")
            print("Exception Occur ", str(e))
        return no_of_books_available[0]

    @staticmethod
    def issue_a_book_db(issue_book_no, issue_employee_no):
        issue_book_sql = ("INSERT INTO j_issue_list "
                          "(book_id, employee_id, issue_return_status) "
                          "VALUES (%s, %s, %s)")
        issue_book_sql_data = (issue_book_no, issue_employee_no, 'No')
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(issue_book_sql, issue_book_sql_data)
        except Exception as e:
            print("Oops Something Wrong in Query Execution issue_book_sql")
            print("Exception Occur ", str(e))
        database.my_database.commit()

        book_availability_change_sql = ("UPDATE j_book_list "
                                        "SET book_available = %s "
                                        "WHERE book_id = %s ")
        book_availability_change_data = ('No', issue_book_no)
        try:
            my_cursor.execute(book_availability_change_sql, book_availability_change_data)
        except Exception as e:
            print("Oops Something Wrong in Query Execution book_availability_change_sql")
            print("Exception Occur ", str(e))
        database.my_database.commit()

    def issue_a_book(self):
        print("**** Take A Book **** ")
        see_all_books = input("Do You Want to See all Available Books? (y/n): ")
        if see_all_books == 'y':
            self.view_all_books()
        issue_book_no = input("Enter the issued book number : ")
        cba = self.check_book_availability(issue_book_no)
        if cba[0] == 0:
            print(" I'm Sorry, that Book is not available :-( . Please return and check with any other books...")
        else:
            print("Yay That book is available!!!")
            issue_employee_no = input("Enter Employee ID : ")
            print("Your Book : ", issue_book_no, "is issued ")
            return_date = datetime.now() + timedelta(days=10)
            print("Please do return/renew it before : ", return_date.strftime("%d %B,%y"))
            self.issue_a_book_db(issue_book_no, issue_employee_no)

    @staticmethod
    def return_a_book_db(return_book_no):

        book_availability_change_in_return_sql = ("UPDATE j_book_list "
                                                  "SET book_available = %s "
                                                  "WHERE book_id = %s")
        book_availability_change_in_return_data = ('Yes', str(return_book_no))
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(book_availability_change_in_return_sql, book_availability_change_in_return_data)
        except Exception as e:
            print("Oops Something Wrong in Query Execution book_availability_change_in_return_sql")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()

        issue_return_status_change_in_return_sql = ("UPDATE j_issue_list "
                                                    "SET issue_return_status = %s "
                                                    "WHERE book_id = %s")
        issue_return_status_change_in_return_data = ('Yes', str(return_book_no))
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(issue_return_status_change_in_return_sql, issue_return_status_change_in_return_data)
        except Exception as e:
            print("Oops Something Wrong in Query Execution issue_return_status_change_in_return_sql")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()

    @staticmethod
    def due_amount_calculation_book_no(return_book_no):
        due_amount_calculation_sql = ("SELECT DATEDIFF(CURRENT_TIMESTAMP(),DATE_ADD(issue_date, INTERVAL 9 DAY)) "
                                      "FROM j_issue_list "
                                      "WHERE book_id = %s AND issue_return_status = %s ")
        due_amount_calculation_data = (str(return_book_no), 'No')
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(due_amount_calculation_sql, due_amount_calculation_data)
            date_diff = my_cursor.fetchall()
            return date_diff[0]
        except Exception as e:
            print("Oops Something Wrong in Query Execution due_amount_calculation_sql")
            print("Exception Occur ", str(e))
        database.my_database.commit()

    def return_a_book(self):
        print(":::: Return Book ::::")
        return_book_no = input("Enter book Number : ")
        date_diff = self.due_amount_calculation_book_no(return_book_no)
        if date_diff[0] >= 0:
            print(date_diff[0] * 10, "Rs Should be payed as the DUE")
            does_due_paid = input("Does Due Amount Payed (y/n) :")
            if does_due_paid == 'y':
                self.return_a_book_db(return_book_no)
        elif date_diff[0] <= 0:
            print("No Dues")
            self.return_a_book_db(return_book_no)
