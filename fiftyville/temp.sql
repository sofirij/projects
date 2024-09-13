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





