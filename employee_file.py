import db_config_file as database
import smtplib
import logging


class Employee:
    @staticmethod
    def create_employee_table():
        my_cursor = database.my_database.cursor()
        logging.debug("Demo Demo ")
        try:
            my_cursor.execute("CREATE TABLE IF NOT EXISTS j_employee_list ( "
                              "employee_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, "
                              "employee_first_name VARCHAR(30) NOT NULL, "
                              "employee_last_name VARCHAR(30) NOT NULL,"
                              "employee_email_id VARCHAR(50) NOT NULL,"
                              "employee_phone_no VARCHAR(15) NOT NULL,"
                              "employee_registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP )"
                              "")
        except Exception as e:
            print("Oops Something Wrong in Query Execution create_employee_table")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()
        my_cursor.close()

    def insert_employee_details(self):
        print("::::: Enter the employee details ::::")
        employee_first_name = input("First Name : ")
        employee_last_name = input("Last Name  : ")
        employee_email_id = input("Email Id : ")
        employee_phone_no = input("Phone No : ")
        self.save_employee_details_to_db(employee_first_name, employee_last_name, employee_email_id, employee_phone_no)

    @staticmethod
    def save_employee_details_to_db(employee_first_name, employee_last_name, employee_email_id, employee_phone_no):
        add_employee = ("INSERT INTO j_employee_list "
                        "(employee_first_name, employee_last_name, employee_email_id, employee_phone_no) "
                        "VALUES (%s, %s, %s, %s)")
        data_employee = (employee_first_name, employee_last_name, employee_email_id, employee_phone_no)
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(add_employee, data_employee)
        except Exception as e:
            print("Oops Something Wrong in Query Execution add_employee ")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()
        my_cursor.close

    @staticmethod
    def view_all_employee_using_no_return_email(employee_no):

        print("Employee Number : ", employee_no)
        view_all_employee_using_no_return_email_sql = ("SELECT DISTINCT "
                                                       " employee_email_id "
                                                       " FROM j_employee_list "
                                                       " WHERE employee_id = "+str(employee_no)+"")
        # print("Query: ", view_all_employee_using_no_return_email_sql)
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(view_all_employee_using_no_return_email_sql)
            all_mail = my_cursor.fetchall()
            return all_mail
        except Exception as e:
            print("Oops Something Wrong in Query Execution view_all_employee_using_no_return_email_sql")
            print("Excepetion Occured ", str(e))
        database.my_database.commit()
        my_cursor.close()

    def view_all_employee_using_no(self, employee_no):
        view_all_employee_using_no_sql = ("SELECT employee_id, employee_first_name, employee_last_name, "
                                          "employee_email_id, employee_phone_no, employee_registration_date "
                                          "FROM j_employee_list "
                                          "where employee_id = "+str(employee_no)+
                                          " ORDER BY employee_first_name ASC LIMIT 1000")
        view_all_employee_using_no_data = str(employee_no)
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(view_all_employee_using_no_sql)
            records = my_cursor.fetchall()
            print(": : Displaying each Employee Details : : ")
            for row in records:
                print("")
                print("Employee Id = ", row[0], )
                print("First Name = ", row[1])
                print("Last Name = ", row[2])
                print("Email Id  = ", row[3])
                print("Phone no  = ", row[4], "\n")
        except Exception as e:
            print("Oops Something Wrong in Query Execution view_all_employee_using_no_sql")
            print("Exception Occured ", str(e))
        database.my_database.commit()
        my_cursor.close()

    @staticmethod
    def view_all_employee():
        sql_select_all_employee_query = ("SELECT employee_id, employee_first_name, employee_last_name, "
                                         "employee_email_id, employee_phone_no, employee_registration_date "
                                         "FROM j_employee_list "
                                         "ORDER BY employee_first_name ASC LIMIT 1000")
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(sql_select_all_employee_query)
            records = my_cursor.fetchall()
            print("Total number of Employees is - ", my_cursor.rowcount)
            print(": : Displaying each Employee Details : : ")
            for row in records:
                print("")
                print("Employee Id = ", row[0], )
                print("First Name = ", row[1])
                print("Last Name = ", row[2])
                print("Email Id  = ", row[3])
                print("Phone no  = ", row[4], "\n")
        except Exception as e:
            print("Oops Something Wrong in Query Execution sql_select_all_employee_query")
            print("Exception Occured ", str(e))
        database.my_database.commit()
        my_cursor.close()

    @staticmethod
    def return_all_employee_no_having_due():
        return_all_employee_no_having_due_sql = ("SELECT DISTINCT employee_id  "
                                                 "FROM j_issue_list "
                                                 "WHERE issue_return_status = 'No' ")
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(return_all_employee_no_having_due_sql)
            all_employee = my_cursor.fetchall()
            print("All Employee", all_employee)
            return all_employee
        except Exception as e:
            print("Oops Something Wrong in Query Execution return_all_employee_no_having_due_sql", str(e))
        database.my_database.commit()

    def return_all_book_no_having_due(self, employee_no):
        # print("Employee_no in return_all_book_no_having_due ", employee_no)
        return_all_book_no_having_due_sql = ("SELECT book_id  "
                                             "FROM j_issue_list "
                                             "where issue_return_status = %s "
                                             "AND employee_id = %s ")
        return_all_book_no_having_due_data = ('No', employee_no)
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(return_all_book_no_having_due_sql, return_all_book_no_having_due_data)
            all_book_no = my_cursor.fetchall()
            return all_book_no
        except Exception as e:
            print("Oops Something Wrong in Query Execution return_all_book_no_having_due_sql")
            print("Exception Occured ", str(e))

        database.my_database.commit()

    def due_amount_calculation_book_no(self, return_book_no):
        due_amount_calculation_sql = ("SELECT DATEDIFF(CURRENT_TIMESTAMP(),DATE_ADD(issue_date, INTERVAL 10 DAY)) "
                                      "FROM j_issue_list "
                                      "WHERE book_id = "+str(return_book_no)+" AND issue_return_status = 'No' ")
        # print("due_amount_calculation_sql : ", due_amount_calculation_sql)
        my_cursor = database.my_database.cursor()
        try:
            my_cursor.execute(due_amount_calculation_sql)
            date_diff = my_cursor.fetchall()
            # print("date_diff : ", date_diff)
            return date_diff[0]
        except Exception as e:
            print("Oops Something Wrong in Query Execution due_amount_calculation_sql")
            print("Exception Occured ",str(e))
        database.my_database.commit()

    def send_mail_to_due_defaulters(self,employee_mail,employee_no):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("mailerdaemon1337x@gmail.com", "Q2Mqad$K9gjVHgqqSKk6%&q&C%ZNHkqqjmNnNwq5xq+8Ssz6nE7jH7^aqqq9W8R_z&D3Sg^jaYU22$r^")
        all_book_no = self.return_all_book_no_having_due(employee_no)
        rate_diff = 0
        # print("Book Number", all_book_no)
        for book_no in all_book_no:
            for in_book_no in book_no:
                due_amount_calculation_book_no_carriage_variable = self.due_amount_calculation_book_no(in_book_no)
                for in_x_above in due_amount_calculation_book_no_carriage_variable:
                    # print("rate Diff Before", rate_diff)
                    # print("due_amount_calculation_book_no_carriage_variable : ", in_x_above)
                    rate_diff = rate_diff + in_x_above
                    # print("rate Diff After", rate_diff)

        message = "This is a reminder mail. please do pay "+str(rate_diff*10) + " RS dues in the library "
        # print("Message to send:", message)
        # print("Employee mail = ", employee_mail[0])
        s.sendmail("mailerdaemon1337x@gmail.com", employee_mail[0], message)
        print(":: Mail Send to :: "+employee_mail[0])
        s.quit()

    def check_employee_status(self):
        print(":::: Employee Status & Send Mail Regarding Book Return Due ::::")
        see_all_employee = input("Do You Want to See all Employees having Due (y/n): ")
        if see_all_employee == 'y':
            all_employee = self.return_all_employee_no_having_due()
            # print(all_employee)
            for row in all_employee:
                for row_row in row:
                    # print("for row in all_employee : ", row_row)
                    self.view_all_employee_using_no(row_row)

        send_mail = input("Do You Want to Send Notification mail to all Employees having Due (y/n): ")
        if send_mail == 'y':
            all_employee = self.return_all_employee_no_having_due()
            # print("all_employee = self.return_all_employee_no_having_due() ", all_employee)
            for employee_no in all_employee:
                for in_employee_no in employee_no:
                    # print("Employee_  number : ", in_employee_no)
                    employee_email = self.view_all_employee_using_no_return_email(in_employee_no)
                    # print("employee mail", employee_email)
                    for mail in employee_email:
                        self.send_mail_to_due_defaulters(mail, in_employee_no)
