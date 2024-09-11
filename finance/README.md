# Yahoo Finance Web Application

This web application allows users to quote, buy, and sell stocks from the stock market. All stock data and quotes are retrieved using the Yahoo Finance API.

## Features

- Quote, buy, and sell stocks in real-time.
- Retrieve up-to-date stock information from the Yahoo Finance API.
- Secure user authentication with hashed passwords.
- Track all user transactions including buys and sells.
- Maintain current stock holdings for each user.

## Database Structure

The application uses an SQLite3 database with three main tables:

1. **Users Table**: Stores user information including:
   - `userId`: Unique identifier for each user.
   - `username`: The username for login.
   - `hashed_password`: The hashed password for user authentication.

2. **Transactions Table**: Records all buy and sell actions performed by users:
   - `transactionId`: Unique identifier for each transaction.
   - `userId`: Foreign key linking to the Users table.
   - `stock_symbol`: The symbol of the stock bought or sold.
   - `transaction_type`: Type of transaction (`buy` or `sell`).
   - `quantity`: Number of shares involved in the transaction.
   - `price`: Price per share at the time of the transaction.
   - `timestamp`: Date and time of the transaction.

3. **UserBalance Table**: Keeps track of the users' currently owned stocks:
   - `userId`: Foreign key linking to the Users table.
   - `stock_symbol`: The symbol of the owned stock.
   - `quantity`: Number of shares currently owned by the user.
   - `average_cost`: Average cost per share based on purchase history.
  
##Note line 54 - 56 in helpers.py is temporary as the API was down at the time of push

## Getting Started

### Prerequisites

- Python 3.x
- SQLite3
- Flask
- `yfinance` package (for Yahoo Finance API)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sofirij/finance.git
   cd finance
2. Install the required packages:
    pip install -r requirements.txt
3. flask run
