class Menu:
    def __init__(self):
        self.option = ""
        self.options = [1, 2, 3, 4, 5, 6]

    def list_options(self):
        print("1. Enter application information"
              "\n2. View all applications"
              "\n3. Search for an application"
              "\n4. Update an application"
              "\n5. Delete an application"
              "\n6. Exit")
        self.option = int(input("Please select an option: "))