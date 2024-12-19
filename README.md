# Bank Account Management System

Welcome to the Bank Account Management System! This project allows you to manage user accounts, handle transactions, and maintain account balances seamlessly.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Bank Account Management System is a Python-based application designed to manage user accounts and perform banking transactions. It uses SQLAlchemy as the ORM for database interactions and Alembic for database migrations.

## Features
- User account creation
- Multiple account types (savings, checking)
- Deposit and withdrawal transactions
- Transaction history tracking
- Account balance checking

## Installation

### Prerequisites
- Python 3.12 or higher
- SQLite (for database management)

### Setup
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/bank-account-project.git
    cd bank-account-project
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    cd lib/db
    alembic upgrade head
    ```

## Usage

### Running the Application
1. **Start the CLI application**:
    ```sh
    python cli.py
    ```

2. **Example Commands**:
    - Create a new user:
      ```python
      create_user(name="Alice", email="alice@example.com")
      ```

    - Create a new account for a user:
      ```python
      create_account(user_id=1, account_type="savings")
      ```

    - Deposit money into an account:
      ```python
      deposit(account_id=1, amount=100.0, description="Initial deposit")
      ```

    - Withdraw money from an account:
      ```python
      withdraw(account_id=1, amount=20.0, description="ATM withdrawal")
      ```

    - Check account balance:
      ```python
      view_balance(account_id=1)
      ```

    - View transaction history:
      ```python
      view_transactions(account_id=1)
      ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any features, git remote add origin https://github.com/tymontiphy/bank-account-project.gitenhancements, or bug fixes.

1. **Fork the repository**
2. **Create a new branch (`git checkout -b feature-branch`)**
3. **Commit your changes (`git commit -m 'Add a new feature'`)**
4. **Push to the branch (`git push origin feature-branch`)**
5. **Open a pull request**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## author
simon tiphy
 
 ### code .
