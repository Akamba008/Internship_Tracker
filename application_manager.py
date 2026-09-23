import csv
from pathlib import Path
from tabulate import tabulate
import pandas

column_headers = [
    "Application ID","Company Name", "Role", "Industry",
    "Company Location", "Application Date", "Application Stage"
]

class ApplicationManager:

    def __init__(self):
        file = Path("applications.csv")
        self.application_count = 0
        self.application_list = []
        if file.is_file():
            self.reader = pandas.read_csv("applications.csv",
                                          dtype={"Application ID": str, "Application Stage": str})
            if not self.reader.empty:
                self.application_count = int(self.reader["Application ID"].max())
        else:
            with open("applications.csv", mode="w",) as application_csv:
                writer = csv.writer(application_csv)
                writer.writerow(column_headers)
            self.reader = pandas.read_csv("applications.csv",
                                              dtype={"Application ID": str, "Application Stage": str})
        self.search_column = self.reader["Company Name"]


    def add_application(self, company_name, role, industry, company_location,
                        application_date, application_stage):
        self.application_count += 1
        self.application_list = [f"{self.application_count:04d}" , company_name,
                                 role, industry, company_location, application_date,
                                 application_stage]
        with open("applications.csv", mode="a", ) as application_csv:
            writer = csv.writer(application_csv)
            writer.writerow(self.application_list)
        self.reader = pandas.read_csv("applications.csv", dtype={"Application ID": str,
                                                                 "Application Stage": str})


    def view_applications(self):
        if self.reader.empty:
            print("No applications found.")
        else:
            print(tabulate(self.reader, headers=column_headers, tablefmt="fancy_grid",
                           showindex=False))


    def view_application(self, company_name):
        company_row = self.reader[self.search_column == company_name]
        print(tabulate(company_row, headers=column_headers, tablefmt="fancy_grid",
                       showindex=False))


    def search_company(self, function, company_name):
        self.search_column = self.reader["Company Name"]
        for row in self.search_column:
            if row == company_name:
                function(company_name)
                return
        print(f"No application found for {company_name}.")


    def is_valid_application_id(self, app_id, company_row):
        self.search_column = company_row[column_headers[0]]
        for row in self.search_column:
            if row == app_id:
                return True
        return False


    def select_application(self, company_name):
        company_row = self.reader[self.search_column == company_name]
        if len(company_row) <= 1:
            company_index = self.get_index(company_name, column_headers[1])
            return company_index
        else:
            while True:
                app_id = input("Enter the Application ID: ").zfill(4)
                if not self.is_valid_application_id(app_id, company_row):
                    print("Invalid Application ID.")
                else:
                    company_index = self.get_index(app_id, column_headers[0])
                    return company_index


    def update_application_status(self, company_name):
        self.view_application(company_name)
        app_index = self.select_application(company_name)
        new_status = input("Enter the new stage of your application: ").title()
        self.reader.at[app_index[0], column_headers[6]] = new_status
        self.reader.to_csv("applications.csv", index=False)
        print(f"Application status updated to {new_status}.")


    def delete_application(self, company_name):
        self.view_application(company_name)
        app_index = self.select_application(company_name)
        self.reader.drop(app_index[0], inplace=True)
        self.reader.to_csv("applications.csv", index=False)
        print(f"The above application has been permanently deleted.")


    def get_index(self, value, column):
        self.search_column = self.reader[column]
        company_row = self.reader[self.search_column == value]
        company_row_index = company_row.index
        return company_row_index

