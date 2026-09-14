from internship_aplication import InternshipApplication

class ApplicationManager:

    def __init__(self):
        self.application_list = []

    def add_application(self, company_name, role, industry, company_location,
                        application_date, application_stage):
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

    def search_applications(self, function, company_name):
        for application in self.application_list:
            if application.company_name == company_name:
                function(application)
                return
        print(f"No application found for {company_name}.")

    @staticmethod
    def view_application(application_id):
        print(f"Company Name: {application_id.company_name}\nRole: {application_id.role}\n"
              f"Industry: {application_id.industry}\nLocation: {application_id.company_location}\n"
              f"Date: {application_id.application_date}\nStage: {application_id.application_stage}")

    @staticmethod
    def update_application_status(application_id):
        new_status =input(f"This was the former status of application: {application_id.application_stage}"
                          f"\nEnter the new application status: ")
        application_id.application_stage = new_status

    def delete_application(self, application_id):
        print(f"The application for {application_id.company_name} has been permanently deleted.")
        self.application_list.remove(application_id)



