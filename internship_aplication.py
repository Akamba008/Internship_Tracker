class InternshipApplication:

    def __init__(self, company_name, role, industry, company_location,
                 application_date, application_stage):
        self.company_name = company_name
        self.role = role
        self.industry = industry
        self.company_location = company_location
        self.application_date = application_date
        self.application_stage = application_stage

        self.application_dictionary = {
            "company_name": self.company_name,
            "role": self.role,
            "industry": self.industry,
            "company_location": self.company_location,
            "application_date": self.application_date,
            "application_stage": self.application_stage
        }

