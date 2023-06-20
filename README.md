# Python-Project
Contact Book using Python
The following Python code implements a simple contact book application using the pandas library. The contact book grants the users to add contacts, delete contacts, display the list of contacts, and search for particular contacts.
Packages Used
The code starts by importing the pandas library as pd. The pandas library provides powerful data manipulation and analysis tools, including data structures and operations for handling structured data.
CSV File
The code uses a CSV file, contacts.csv, to store the contact information. The CONTACTS_FILE variable is set for the filename. The CSV file is used as a persistent storage for the contacts, allowing the user to add, display, and search contacts across different program executions.
Functions Description
1.	add_contact(): This function prompts the user to enter contact information, including name, email, and phone number. It then creates a dictionary with the contact data and converts it into a pandas DataFrame. The DataFrame is then appended to the contacts.csv file using the to_csv() method. Finally, a success message is displayed.
2.	display_contacts(): This function reads the contacts.csv file using the read_csv() function from pandas and stores the data in a DataFrame. If the DataFrame is empty, it means no contacts have been added yet, and a corresponding message is displayed. Otherwise, the contact information is printed using the to_string() method, which formats the DataFrame as a string without the index column. After displaying the contacts, a message indicating the completion of the operation is printed.
3.	search_contact(): This function prompts the user to enter a search term. It then reads the contacts.csv file and creates a DataFrame. The function searches for the entered term in the columns using the contains() method. The user is allowed to enter anything related to the contact which includes "Name," "Email," and "Phone Number" to display the respective details. The search is case-insensitive due to the case=False argument. If no matches are found, a message is displayed. Otherwise, the matched contacts are printed using the to_string() method. Finally, a message indicating the completion of the search operation is printed.
4.	main(): This function is the entry point of the program. It displays a menu to the user with four options: add a contact, display contacts, search contacts, or quit. The user's choice is taken as input using the input() function. Depending on the choice, the corresponding function is called. If an invalid choice is entered, an error message is displayed. The program continues to loop until the user chooses to quit.
Execution
To execute the contact book, the main() function is called at the end of the script. It starts the program and displays the main menu. The user can choose options by entering the corresponding number. Based on the chosen option, the respective function is called, and the contact book operation is performed.
This code can be further expanded to include additional functionalities such as updating or deleting contacts, sorting contacts, or handling duplicate entries.


