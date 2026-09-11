from internship_aplication import InternshipApplication

class ApplicationManager:

    def __init__(self):
        self.application_list = []

    def add_application(self, company_name, role, industry, company_location, application_date, application_stage):
        internship_application = InternshipApplication(
            company_name,
            role,
            industry,
            company_location,
            application_date,
            application_stage
        )
        self.application_list.append(internship_application)

    def view_applications(self):
        for application in self.application_list:
            print(application.company_name,
                  application.role,
                  application.industry,
                  application.company_location,
                  application.application_date,
                  application.application_stage)