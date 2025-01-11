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


## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone github.com/Ravi9550/FinTrack.git
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv

  For Linux/macOS
  ```bash
   source venv/bin/activate
  ```
  For Windows
   ```bash
   venv\Scripts\activate
  ```

