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
              "\n3. Search for an application"
              "\n4. Update an application"
              "\n5. Delete an application"
              "\n6. Exit")
        self.option = int(input("Please select an option: "))

    def add_application_option(self):
        self.company_name = input("Please enter the company name: ").title()
        self.role = input("Please enter the role: ").title()
        self.industry = input("Please enter the industry: ").title()
        self.company_location = input("Please enter the company location: ").title()
        self.application_date = input("Please enter the application date(DD/MM/YYYY): ")
        self.application_stage = input("Please enter the application stage: ").title()

    def application_search(self):
        self.company_name = input("Enter the company name to search for: ").title()

    def update_application_status(self):
        self.company_name = (input("Enter the company name whose application "
                                   "status you wish to update: ").title())


