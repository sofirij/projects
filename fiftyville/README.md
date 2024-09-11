Fiftyville Mystery Solver
Overview
Welcome to the Fiftyville Mystery Solver! This project is a solution to a challenging SQL-based mystery-solving problem, where the goal is to identify the thief who stole the CS50 Duck, the city to which the thief escaped, and the accomplice who helped them. The mystery takes place in the fictional town of Fiftyville, and the answers are hidden within the town's data records provided in a SQLite database.

Problem Statement
On July 28, 2023, the CS50 Duck was stolen on Humphrey Street in Fiftyville. Authorities suspect the thief escaped town shortly after the theft with the help of an accomplice. Your task is to find out:

Who the thief is.
What city the thief escaped to.
Who the thief’s accomplice is.
Solution Approach
The Fiftyville authorities provided a SQLite database (fiftyville.db) containing several tables of data from around the time of the theft. The task was to query this database using SQL to extract the relevant information and solve the mystery. The solution process is meticulously documented in the log.sql file, showcasing each query run, along with comments detailing the reasoning behind each step.

Key Steps Taken
Initial Investigation: Analyzed various tables in the database to understand the data available, focusing on records around July 28, 2023.
Security Footage Analysis: Investigated the security_clip.csv file to identify individuals present at the crime scene during the time of the theft.
Flight Records Review: Queried the flights.csv data to determine any suspicious flights that departed shortly after the theft, focusing on departures that fit the thief's escape pattern.
Call Logs Inspection: Examined the calls.csv file to identify communications between potential suspects and their accomplices.
Passport Checks: Cross-referenced individuals’ travel details in potential_passports.csv to confirm the thief’s identity and escape route.
Final Deduction: Combined all findings to identify the thief, the city they escaped to, and their accomplice.
Files
log.sql: Contains all the SQL queries run during the investigation, with detailed comments explaining each step and thought process.
calls.csv: Call records between individuals in Fiftyville.
flights.csv: Flight records of people leaving Fiftyville around the time of the theft.
security_clip.csv: Footage from security cameras near the crime scene.
potential_passports.csv: Passport data for individuals traveling around the time of the theft.
How to Use
Clone this repository.
Load the data into the SQLite database.
Run the queries in log.sql to follow the investigation process step-by-step.
Review the comments in log.sql to understand the logic behind each query.
Key Insights
The log.sql file serves as an excellent demonstration of SQL skills, particularly in data exploration, filtering, and complex query formulation. It provides clear evidence of a systematic approach to problem-solving and demonstrates proficiency in SQL for real-world applications.

Results
After thorough investigation, the following were identified:

Thief: Bruce
Escape City: New York City
Accomplice: Robin

Conclusion
The Fiftyville Mystery Solver project showcases the use of SQL for solving a complex, multi-layered problem. It reflects critical thinking, attention to detail, and a structured approach to data analysis, making it a valuable addition to any portfolio.

