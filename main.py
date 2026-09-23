from menu import Menu
from application_manager import ApplicationManager

menu = Menu()
application_manager = ApplicationManager()

# Keep the program running until the user selects Exit.
running = True
while running:
    print("=== Internship Tracker ===")
    menu.display_menu()

    if menu.option == 1:
        menu.get_application_details()
        application_manager.add_application(menu.company_name, menu.role, menu.industry,
                                            menu.company_location, menu.application_date,
                                            menu.application_stage)

    elif menu.option == 2:
        application_manager.view_applications()

    elif menu.option == 3:
        if not menu.is_file_empty(menu.get_company_to_search):
            application_manager.search_company(application_manager.view_application,
                                               menu.company_name)

    elif menu.option == 4:
        if not menu.is_file_empty(menu.get_company_to_update):
            application_manager.search_company(application_manager.update_application_status,
                                               menu.company_name)

    elif menu.option == 5:
        if not menu.is_file_empty(menu.get_company_to_delete):
            application_manager.search_company(application_manager.delete_application,
                                               menu.company_name)

    elif menu.option == 6:
        running = False
