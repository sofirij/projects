Runoff Election Simulation
This program simulates a ranked-choice voting system (also known as an instant runoff election), allowing voters to rank candidates in order of preference. Unlike a traditional plurality vote, this system helps ensure that the winner of an election better reflects the preferences of the voters.

Overview
In a ranked-choice voting system, voters can rank candidates in order of preference. If no candidate receives a majority of the first-preference votes, the candidate with the fewest votes is eliminated, and their votes are transferred to the next preferred candidate on each ballot. This process repeats until one candidate has a majority of the votes.

This program, runoff.c, simulates this election system.

How It Works
Input: Each voter ranks the candidates according to their preferences.
First Round: The program counts the first-choice votes for each candidate.
Majority Check: If a candidate has more than 50% of the votes, they are declared the winner.
Elimination and Runoff:
If no candidate has a majority, the candidate with the fewest votes is eliminated.
Voters who selected the eliminated candidate will have their votes transferred to their next choice.
Repeat: The process continues until a candidate has a majority of the votes.
Example Scenarios
Scenario 1: Five Ballots, Tie Between Alice and Bob
Voters’ Preferences:

Voter 1: Alice > Bob > Charlie
Voter 2: Alice > Charlie > Bob
Voter 3: Bob > Alice > Charlie
Voter 4: Bob > Charlie > Alice
Voter 5: Charlie > Alice > Bob
Result:

Initial tally: Alice = 2, Bob = 2, Charlie = 1
Charlie is eliminated, and their vote goes to Alice, making Alice the winner.
Scenario 2: Nine Ballots, Plurality Winner vs. Majority Preference
Voters’ Preferences:

Voters 1–4: Charlie > Bob > Alice
Voters 5–7: Bob > Alice > Charlie
Voters 8–9: Alice > Bob > Charlie
Result:

Initial tally: Charlie = 4, Bob = 3, Alice = 2
Alice is eliminated, and their votes go to Bob.
Final tally: Bob = 5, Charlie = 4
Bob wins with a majority.
How to Compile and Run the Program
Compile: Use GCC or any C compiler to compile the program.

bash
gcc runoff.c -o runoff
Run: Execute the compiled program and provide the required inputs.

bash
./runoff
Input: Enter the number of voters and candidates when prompted, and then enter each voter’s ranked choices.

Key Features
Implements ranked-choice voting (instant runoff).
Handles tie-breaking scenarios by eliminating the least preferred candidate.
Ensures the winner represents a majority preference among voters.
