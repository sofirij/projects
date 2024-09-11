-- Keep a log of any SQL queries you execute as you solve the mystery.

--get the description of the crime report that happened on the day of the crime
SELECT id, description FROM crime_scene_reports
WHERE year = 2023 AND month = 7 AND day = 28 AND street ='Humphrey Street';

--get the information on the interviews of the 3 witnessess that happened that day from the interview logs
SELECT transcript FROM interviews
WHERE day = 28 AND month = 7 AND year = 2023;

--get the list of all the account numbers that withdrew money that morning on Leggett Street
SELECT * FROM atm_transactions
WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

--get the license plate of all the cars that left the bakery within 10 minutes of the robbery
SELECT * FROM bakery_security_logs
WHERE year = 2023 AND month = 7 AND day = 28 and hour = 10 AND minute >= 15 AND minute <= 25 AND activity = 'exit';


--get the list of the callers that made a call that day
SELECT * FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2023 AND duration < 60;

--get the list of flights that will take the criminal
SELECT * FROM flights
WHERE origin_airport_id = 8 AND year = 2023 AND day = 29 AND month = 7;

--get the passport numbers of those that were on the security tape and are on the flight out of fiftyville
--join the result of the 2 queries
SELECT passport_number_security.passport_number FROM
(
    --get the passport numbers of the people found in the security log
    SELECT passport_number FROM people
    JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
    WHERE people.license_plate IN
    (
        --get the license plate of all the cars that left the bakery within 10 minutes of the robbery
        SELECT license_plate FROM bakery_security_logs
        WHERE year = 2023 AND month = 7 AND day = 28 and hour = 10 AND minute >= 15 AND minute <= 25 AND activity = 'exit'
    )
) AS passport_number_security
JOIN
(
    --get the passport numbers of the individuals that are on a flight out of fiftyville
    SELECT passport_number FROM passengers
    JOIN flights ON flights.id = passengers.flight_id
    WHERE flights.id IN
    (
        --get the list of flights that will take the criminal
        SELECT flight_id FROM flights
        WHERE origin_airport_id = 8 AND year = 2023 AND day = 29 AND month = 7
    )
) AS passport_number_flight
ON passport_number_flight.passport_number = passport_number_security.passport_number;

--query for the passport numbers of those that were on the security footage and also on the flight and also on the caller list on the suspicious calls
--join the passport numbers of the previous join with the passport number for the callers
--then query for the passport numbers of the new query
--join the previous join to the query of the passport numbers of the suspicious callers and return the list of passport numbers
SELECT DISTINCT potential_passports.passport_number FROM
(
    --get the passport numbers of those that were on the security tape and are on the flight out of fiftyville
    --join the result of the 2 queries
    SELECT passport_number_security.passport_number FROM
    (
        --get the passport numbers of the people found in the security log
        SELECT passport_number FROM people
        JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
        WHERE people.license_plate IN
        (
            --get the license plate of all the cars that left the bakery within 10 minutes of the robbery
            SELECT license_plate FROM bakery_security_logs
            WHERE year = 2023 AND month = 7 AND day = 28 and hour = 10 AND minute >= 15 AND minute <= 25 AND activity = 'exit'
        )
    ) AS passport_number_security
    JOIN
    (
        --get the passport numbers of the individuals that are on a flight out of fiftyville
        SELECT passport_number FROM passengers
        JOIN flights ON flights.id = passengers.flight_id
        WHERE flights.id IN
        (
            --get the list of flights that will take the criminal
            SELECT flight_id FROM flights
            WHERE origin_airport_id = 8 AND year = 2023 AND day = 29 AND month = 7
        )
    ) AS passport_number_flight
    ON passport_number_flight.passport_number = passport_number_security.passport_number
) AS potential_passports
JOIN
(
    --query for the passport numbers of the suspicious calls
    SELECT people.passport_number from people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE phone_calls.caller IN
    (
        --get the list of the callers that made a call that day
        SELECT phone_calls.caller FROM phone_calls
        WHERE day = 28 AND month = 7 AND year = 2023 AND duration < 60
    )
) AS passports_call
ON passports_call.passport_number = potential_passports.passport_number;

--link the atm withdrawal on the day of the theft with that of the remaining individuals
--get the passport number of those who made withdrawals on the day of the theft
--join the passport number of the withdrawals to that of what we have left



--join the passport number of the withdrawals to that of what we have left
SELECT DISTINCT likely_passport_number.passport_number FROM
(
    --query for the passport numbers of those that were on the security footage and also on the flight and also on the caller list on the suspicious calls
    --join the passport numbers of the previous join with the passport number for the callers
    --then query for the passport numbers of the new query
    --join the previous join to the query of the passport numbers of the suspicious callers and return the list of passport numbers
    SELECT DISTINCT potential_passports.passport_number FROM
    (
        --get the passport numbers of those that were on the security tape and are on the flight out of fiftyville
        --join the result of the 2 queries
        SELECT passport_number_security.passport_number FROM
        (
            --get the passport numbers of the people found in the security log
            SELECT passport_number FROM people
            JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
            WHERE people.license_plate IN
            (
                --get the license plate of all the cars that left the bakery within 10 minutes of the robbery
                SELECT license_plate FROM bakery_security_logs
                WHERE year = 2023 AND month = 7 AND day = 28 and hour = 10 AND minute >= 15 AND minute <= 25 AND activity = 'exit'
            )
        ) AS passport_number_security
        JOIN
        (
            --get the passport numbers of the individuals that are on a flight out of fiftyville
            SELECT passport_number FROM passengers
            JOIN flights ON flights.id = passengers.flight_id
            WHERE flights.id IN
            (
                --get the list of flights that will take the criminal
                SELECT flight_id FROM flights
                WHERE origin_airport_id = 8 AND year = 2023 AND day = 29 AND month = 7
            )
        ) AS passport_number_flight
        ON passport_number_flight.passport_number = passport_number_security.passport_number
    ) AS potential_passports
    JOIN
    (
        --query for the passport numbers of the suspicious calls
        SELECT people.passport_number from people
        JOIN phone_calls ON phone_calls.caller = people.phone_number
        WHERE phone_calls.caller IN
        (
            --get the list of the callers that made a call that day
            SELECT phone_calls.caller FROM phone_calls
            WHERE day = 28 AND month = 7 AND year = 2023 AND duration < 60
        )
    ) AS passports_call
    ON passports_call.passport_number = potential_passports.passport_number
) AS likely_passport_number
JOIN
(
    --get the passport number of those who made withdrawals on the day of the theft
    SELECT people.passport_number FROM people
    JOIN bank_accounts ON bank_accounts.person_id = people.id
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    WHERE atm_transactions.account_number IN
    (
        --get the list of all the account numbers that withdrew money that morning on Leggett Street
        SELECT account_number FROM atm_transactions
        WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
    )
) AS likely_withdrawals
ON likely_passport_number.passport_number = likely_withdrawals.passport_number;



--from the previous query we know that there are 2 suspects left so whoever has the earlier flight is the criminal
--from the passport number we can get the flight id then check the time of the flight
SELECT people.passport_number, flights.* FROM flights
JOIN passengers ON passengers.flight_id = flights.id
JOIN people ON people.passport_number = passengers.passport_number
WHERE people.passport_number = 3592750733 OR people.passport_number = 5773159633
ORDER BY people.passport_number;

--get the name of the criminal
SELECT people.name FROM people
WHERE passport_number = 5773159633;

--get the name of the person when we have gotten the phone number to be (375) 555-8161
SELECT people.name FROM people
WHERE people.phone_number IN
(
    --get the phone number of the receiver of the criminals call
    --from the list above get the phone number of the receiver where the callers passport is 5773159633
    SELECT phone_calls.receiver FROM phone_calls
    JOIN people ON people.phone_number = phone_calls.caller
    WHERE phone_calls.receiver IN
    (
        --get the list of the receivers that got a call that day
        SELECT receiver FROM phone_calls
        WHERE day = 28 AND month = 7 AND year = 2023 AND duration < 60
    )
    AND people.passport_number = 5773159633
)
