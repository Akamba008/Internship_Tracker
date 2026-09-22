import pandas

class Menu:

    def __init__(self):
        self.option = ""
        self.options = [1, 2, 3, 4, 5, 6]
        self.company_name = ""
        self.role = ""
        self.industry = ""
        self.company_location = ""
        self.application_date = ""
        self.application_stage = ""

    def list_options(self):
        print("1. Enter application information"
              "\n2. View all applications"
              "\n3. Search applications by company"
              "\n4. Update an application"
              "\n5. Delete an application"
              "\n6. Exit")
        while True:
            try:
                self.option = int(input("Please select an option: "))
            except ValueError:
                print("Please select a correct option\n\n")
            else:
                if self.option not in self.options:
                    print("Please select a correct option\n\n")
                else:
                    break

    def add_application_option(self):
        self.company_name = input("Please enter the company name: ").title()
        self.role = input("Please enter the role: ").title()
        self.industry = input("Please enter the industry: ").title()
        self.company_location = input("Please enter the company location: ").title()
        self.application_date = input("Please enter the application date(DD/MM/YYYY): ")
        self.application_stage = input("Please enter the application stage: ").title()

    @staticmethod
    def is_file_empty(function):
        reader = pandas.read_csv("applications.csv")
        if reader.empty:
            print("No applications yet. Add some!")
            return True
        else:
            function()
            return False

    def application_search(self):
        self.company_name = input("Enter the company name to search: ").title()

    def update_application_status(self):
        self.company_name = (input("Enter the company name whose application "
                                   "status you wish to update: ").title())

    def delete_application(self):
        self.company_name = (input("Enter the company name whose application "
                                   "you wish to delete: ").title())

