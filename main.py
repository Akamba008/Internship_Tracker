from menu import Menu
from application_manager import ApplicationManager

menu = Menu()
application_manager = ApplicationManager()
running = True
while running:
    print("=== Internship Tracker ===")
    menu.list_options()

    if menu.option == 1:
        menu.add_application_option()
        application_manager.add_application(menu.company_name, menu.role, menu.industry,
                                            menu.company_location, menu.application_date,
                                            menu.application_stage)
    elif menu.option == 2:
        application_manager.view_applications()
    elif menu.option == 3:
        menu.application_search()
        application_manager.search_applications(application_manager.view_application,
                                                menu.company_name)
    elif menu.option == 4:
        menu.update_application_status()
        application_manager.search_applications(application_manager.update_application_status,
                                                menu.company_name)
    elif menu.option == 5:
        pass
    elif menu.option == 6:
        running = False
