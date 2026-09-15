import csv
from tabulate import tabulate
import pandas

column_headers = ["Company Name", "Role", "Industry", "Company Location",
                  "Application Date", "Application Stage"]

class ApplicationManager:

    def __init__(self):
        self.application_list = []
        with open("applications.csv", mode="w",) as application_csv:
            writer = csv.writer(application_csv)
            writer.writerow(column_headers)
        self.reader = pandas.read_csv("applications.csv")
        self.search_column = self.reader["Company Name"]


    def add_application(self, company_name, role, industry, company_location,
                        application_date, application_stage):

        self.application_list = [company_name, role, industry, company_location,
                        application_date, application_stage]
        with open("applications.csv", mode="a", ) as application_csv:
            writer = csv.writer(application_csv)
            writer.writerow(self.application_list)
        self.reader = pandas.read_csv("applications.csv")


    def view_applications(self):
        if self.reader.empty:
            print("No applications found.")
        else:
            print(tabulate(self.reader, headers=column_headers, tablefmt="fancy_grid",
                           showindex=False))


    def search_applications(self, function, company_name):
        self.search_column = self.reader["Company Name"]
        for row in self.search_column:
            if row == company_name:
                function(company_name)
                return
        print(f"No application found for {company_name}.")



    def view_application(self, company_name):
        company_row = self.reader[self.search_column == company_name]
        print(tabulate(company_row, headers=column_headers, tablefmt="fancy_grid",
                       showindex=False))


    @staticmethod
    def update_application_status(application_id):
        new_status =input(f"This was the former status of application: {application_id.application_stage}"
                          f"\nEnter the new application status: ")
        application_id.application_stage = new_status


    def delete_application(self, application_id):
        print(f"The application for {application_id.company_name} has been permanently deleted.")
        self.application_list.remove(application_id)



