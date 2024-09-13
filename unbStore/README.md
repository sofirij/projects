# Project Title: UNBSTORE
### Video Demo: <https://youtu.be/vzprdKhsOyY>
### Description


UNB Student Marketplace
Overview
The UNB Student Marketplace is a web application that facilitates buying and selling products or services within the University of New Brunswick (UNB) student community. Designed with Flask and SQLite, this platform allows students to register as buyers or sellers, manage their listings, and find items based on categories and descriptions. This application aims to create a localized marketplace where students can easily connect and trade goods, from textbooks and electronics to services like tutoring.

Project Structure and File Descriptions
The project consists of multiple Python scripts, HTML templates, and SQL configurations, each serving a specific function in the application:

1. app.py
This is the main application file that initializes the Flask app, sets up the database connection, and defines all the routes and their corresponding logic. Key functionalities include:

User Authentication: Handles registration, login, and logout functionalities using password hashing for security.
Inventory Management: Allows sellers to add, edit, and delete items from their inventory. Items include details like category, condition, and description.
Search: Provides search functionality where buyers can look for products by category and keyword, searching both item names and descriptions.
Error Handling: Uses custom apology functions to handle various user errors gracefully, providing feedback when operations fail.
2. helpers.py
Contains utility functions that support the main application, including:

login_required: A decorator to protect routes that should only be accessible to logged-in users.
usd: A filter used to format numbers as USD currency in templates.
apology: A function that renders custom error messages to users, maintaining a consistent error handling approach throughout the application.
3. templates/
This directory contains HTML files that define the structure and design of the application's user interface. Notable files include:

index.html: The main page where users can search for items by category and keyword. Displays search results dynamically.
inventory.html: Allows sellers to manage their inventory, showing a list of their products with options to add, edit, or delete items.
register.html and login.html: Pages for user registration and login, respectively, ensuring secure access to the application.
searchIndex.html: Displays search results when a buyer queries the inventory based on category and keywords.
editableInventory.html: Facilitates editing inventory items with pre-filled data for the user’s convenience.
4. static/
This folder contains static assets like CSS for styling the application, JavaScript files for interactive elements, and images.

5. schema.sql
This SQL file is used to set up the database tables required for the application, including:

users: Stores user information, including usernames, hashed passwords, and their role (buyer or seller).
inventory: Contains the product listings with details such as category, name, condition, location, and seller information.
categories: Lists predefined categories available for inventory items, ensuring consistency in classification.
conditions: Contains possible conditions for items (e.g., new, used), providing standardized options during listing creation.
Design Decisions
1. Database Choice: SQLite
SQLite was chosen for its simplicity and ease of integration with Flask, making it ideal for small to medium-scale applications. The database schema is designed to maintain relationships between users and their inventory items, with additional tables for categories and item conditions to standardize inputs.

2. User Roles (Buyer vs. Seller)
The application differentiates users as buyers or sellers to manage their access and functionalities effectively. This role distinction simplifies user experience: sellers are provided inventory management features, while buyers have access to search and purchase functionalities.

3. Case-Insensitive Search
To enhance the search experience, the application implements case-insensitive search functionality by using the LOWER() SQL function. This ensures that users can find items regardless of how the keywords are typed, making searches more user-friendly.

4. Input Validation and Error Handling
The application includes extensive input validation to prevent incorrect or malicious data entry. It also employs consistent error handling with the apology function, providing users with clear feedback when they make mistakes or when a requested action cannot be completed.

5. Session Management and Security
Session management is handled using Flask-Session, which stores session data on the server side. This enhances security by avoiding client-side session manipulation. Passwords are securely stored using werkzeug.security's hashing functions, protecting user credentials from potential breaches.

Usage
Register as a buyer or seller.
Sellers can add, edit, and remove items from their inventory.
Buyers can search for items using category and keywords.
Logout securely when done.
Future Enhancements
Payment Integration: Adding secure payment gateways to facilitate transactions directly through the platform.
Review System: Allowing users to leave feedback on sellers and products, enhancing trust within the community.
Enhanced Search Filters: Implementing additional filters such as price range, item condition, and location.
Conclusion
The UNB Student Marketplace provides a dedicated and secure platform for UNB students to engage in buying and selling within their community. Through careful design and thoughtful implementation, this project aims to foster a safe and efficient trading environment tailored specifically for students.

Future Enhancements
Payment Integration: Adding secure payment gateways to facilitate transactions directly through the platform.
Review System: Allowing users to leave feedback on sellers and products, enhancing trust within the community.
Enhanced Search Filters: Implementing additional filters such as price range, item condition, and location.

Installation
Clone the repository:

bash
git clone https://github.com/sofiri/projects.git
cd project
Set up a virtual environment (recommended):

Install required packages:
bash
pip install -r requirements.txt

Run the application:

bash
flask run
