import pandas


class Menu:
    """Handle menu display and user input for the Internship Tracker."""

    def __init__(self):
        self.option = ""
        self.options = [1, 2, 3, 4, 5, 6]
        self.company_name = ""
        self.role = ""
        self.industry = ""
        self.company_location = ""
        self.application_date = ""
        self.application_stage = ""

    def display_menu(self):
        """Display the main menu and validate the user's selected option."""
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
                print("Please select a valid option\n")
            else:
                if self.option not in self.options:
                    print("Please select a correct option\n\n")
                else:
                    break

    def get_application_details(self):
        """Collect application details from the user."""
        self.company_name = input("Please enter the company name: ").strip().title()
        self.role = input("Please enter the role: ").strip().title()
        self.industry = input("Please enter the industry: ").strip().title()
        self.company_location = input("Please enter the company location: ").strip().title()
        self.application_date = input("Please enter the application date(DD/MM/YYYY): ").strip()
        self.application_stage = input("Please enter the application stage: ").strip().title()

    @staticmethod
    def is_file_empty(function):
        """Check for stored applications before performing the requested operation."""
        reader = pandas.read_csv("applications.csv")
        if reader.empty:
            print("No applications yet. Add some!")
            return True
        else:
            function()
            return False

    def get_company_to_search(self):
        """Collect the company name to search for."""
        self.company_name = input("Enter the company name to search: ").strip().title()

    def get_company_to_update(self):
        """Collect the company name of the application to update."""
        self.company_name = (input("Enter the company name whose application "
                                   "status you wish to update: ").strip().title())

    def get_company_to_delete(self):
        """Collect the company name of the application to delete."""
        self.company_name = (input("Enter the company name whose application "
                                   "you wish to delete: ").strip().title())

