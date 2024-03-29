# company_employees
This website is a simple web application for managing information about company employees. Here's a brief description of its functionality:

1. **Home Page (`/`)**:
   - The home page displays a table with a list of all company employees.
   - The table shows the following data for each employee: ID, name, position, hire date, salary, city, country.
   - Additionally, there's a form on this page for filtering employees by name. Users can enter an employee's name in the text field and submit the form to filter the list of employees by the specified name.

2. **Selected Employees Page (`/selected_employees`)**:
   - After submitting the form on the home page with a specified employee name, the user is redirected to the selected employees page.
   - This page displays a table with data of the selected employees based on the provided name.
   - If multiple employees have the same name, all of them will be displayed.

3. **Interaction with the Database**:
   - SQLite database is used to store information about employees.
   - The database schema includes the `employees` table, which stores information about each employee.

This simple web application provides the ability to view information about employees and filter this information by their names.

Test commit
