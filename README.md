# Internship Tracker

## About

Internship Tracker is a terminal-based Python application designed to help students organise and manage their internship
applications in one place.

I built this project while applying for software engineering placements because I wanted a simple way to keep track of 
the companies I had applied to, the roles, application dates, locations, and the current stage of each application.

The project also gave me an opportunity to apply Python concepts outside of tutorials, including object-oriented 
programming, CRUD operations, file handling, input validation, and data persistence.

## Features

- Add new internship applications
- View all stored applications
- Search applications by company
- Update the status of an application
- Delete applications
- Generate a four-digit ID for each application
- Handle multiple applications to the same company using application IDs
- Store application data persistently in a CSV file
- Validate menu selections and application IDs

## Technologies Used

- Python
- Pandas
- CSV file storage
- Tabulate
- Git
- GitHub

## Concepts Practised

- Object-Oriented Programming (OOP)
- CRUD operations
- File handling
- Data persistence
- Input validation
- Error handling
- Refactoring

## Getting Started

### Requirements

- Python 3
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akamba008/Internship_Tracker.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Internship_Tracker
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```
   
## How to Use

When the application starts, the following menu is displayed:

1. Enter application information
2. View all applications
3. Search applications by company
4. Update an application
5. Delete an application
6. Exit

Select an option by entering the corresponding number.

Each application stores the following information:

- Application ID
- Company Name
- Role
- Industry
- Company Location
- Application Date
- Application Stage

Application data is saved to `applications.csv`, allowing the information to persist between sessions.

## Project Structure

```text
Internship_Tracker/
├── main.py
├── menu.py
├── application_manager.py
├── requirements.txt
└── README.md
```

- `main.py` - Runs the application and controls the main program flow.
- `menu.py` - Handles the menu and collects user input.
- `application_manager.py` - Handles application creation, searching, updating, deletion, and CSV data management.
- `requirements.txt` - Lists the external Python packages required to run the project.
- `README.md` - Provides project documentation.

The application automatically creates an `applications.csv` file when first run. This file stores application data 
locally and is excluded from the repository.

## Future Improvements

- Replace CSV storage with a database such as SQLite.
- Add automated tests to improve reliability.
- Develop a web-based user interface.
- Add more advanced application filtering and sorting.
- Add application deadline tracking.
- Improve input validation and error handling.

## Author

**Akamba Isoni**

Computer Science undergraduate at the University of Birmingham.

- GitHub: [Akamba008](https://github.com/Akamba008)
- LinkedIn: [Akamba Isoni](https://www.linkedin.com/in/akambaisoni)