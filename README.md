# FinTrack (Personal Finance Manager)

## Overview
The **Personal Finance Manager** is a web-based system that allows users to efficiently track their income, expenses, and savings goals. The system supports adding, viewing, updating, and deleting transactions, as well as categorizing them for better financial management. Users can also set and monitor savings goals and generate reports to visualize their financial patterns.

## Features
- **User Management:**
  - Users can register, login, and manage their profiles.
  - Each user has a unique profile with personal details (name, email, etc.).

- **Transaction Management:**
  - Users can add, view, update, and delete financial transactions.
  - Transactions contain details like amount, date, category (e.g., Food, Rent), and description.

- **Category Management:**
  - Users can create and manage custom categories for their transactions.

- **Savings Goals:**
  - Users can set savings goals with target amounts and dates.
  - The system tracks progress towards these goals based on the user's financial transactions.

- **Reports:**
  - The system generates monthly and yearly reports showing income, expenses, and savings.
  - Visual charts (e.g., pie charts, bar graphs) display the user's spending patterns.

## Assumptions
- Users authenticate using a basic username/password mechanism.
- The system uses a simple SQLite database for storing data (alternatively, an in-memory database can be used for testing).
- The system provides a basic web interface usinf django for interacting with users.
- The application tracks income and expenses, and the users' savings goals are tied to their financial transactions.

## Technology Stack
- **Frontedn:** HTML, CSS, Javascript, Bootstrap
- **Backend:** Python, Django
- **Database:** SQLite
- **Authentication:** Basic username/password system
- **Visualization:** Chart.js


## Screenshots
![home1](https://github.com/user-attachments/assets/6eb612e7-2d4f-4b70-87b9-7865681babdf)
![dash1](https://github.com/user-attachments/assets/002be1f3-d07a-4cc7-a45e-02bca6df99ba)
![dash2](https://github.com/user-attachments/assets/ae0c7d43-2834-4292-8120-44a87fec1811)
![dash3](https://github.com/user-attachments/assets/7e9dffc6-aa03-4474-87c4-68f220e2ff2b)
![dash4](https://github.com/user-attachments/assets/db233136-e85e-4f0d-a606-0cae07a5c177)
![trans](https://github.com/user-attachments/assets/9572a18d-35e2-41e2-9fd7-e2c65e0d5dab)
![tans_summ](https://github.com/user-attachments/assets/2ba06810-ded2-49c1-8789-48caefb1b485)



## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ravi9550/FinTrack.git
   ```
2. **Go to the folder**
   ```bash
    cd Fintrack
3. **Create a virtual environment**
   ```bash
   python3 -m venv venv
3. **Activate the virtual environment**

   - For Linux/macOS
     ```bash
     source venv/bin/activate
     ```
  
   - For Windows
     ```bash
     venv\Scripts\activate
4. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
5. **Create Django project**
   ```bash
   django-admin startproject fintrack
   ```
6. **Go to project folder**
   ```bash
    cd fintrack
7. **Create a Django app**
   ```bash
   django-admin startapp finanaceapp
8. **Apply database migrations**
   ```bash
   python manage.py migrate
9. **Create a superuser**(for admin access)
    ```bash
    python manage.py createsuperuser
10. **Run the development server**
    ```bash
    python manage.py runserver
## Running the Tests

1. **To run the tests:**

    In your terminal, make sure you are in the project directory, and run the following command:

    ```bash
    python manage.py test
    ```

    Django will automatically discover any test cases in your app and run them.

2. **Test Output:**

    The results will show which tests passed and which failed. Here's an example of what to expect:

    ```
   Found 6 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 1.639s
    
    OK
    Destroying test database for alias 'default'...
    ```

    This indicates that all tests have passed.

## Sample Test Cases

The following tests have been included in the app:

1. **test_transaction_creation**: Verifies that transactions are created correctly.
2. **test_transaction_str_method**: Verifies the string representation of a transaction.
3. **test_income_creation**: Verifies that incomes are created correctly.
4. **test_income_str_method** : Verifies the string representation of a income
5. **test_savings_goal_creation**:Verifies that savings goal is created correctly.
6. **test_savings_goal_str_method** : Verifies the string representation of savings goals.

5. **test_savings_goal_creation**: Verifies that savings goals are created correctly.
6. **test_transaction_str_method**: Verifies the string representation of a transaction.
