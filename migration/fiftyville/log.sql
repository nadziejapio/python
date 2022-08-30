-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Check what is in Crime reports
SELECT *
FROM crime_scene_reports;
-- check what is in crime reports on July 28, 2021 on Humphrey Street
SELECT *
FROM crime_scene_reports
WHERE day = 28
AND month = 7
AND year = 2021
AND street = "Humphrey Street";
-- check bakery logs around 10:15am
SELECT *
FROM bakery_security_logs
WHERE day = 28
AND month = 7
AND year = 2021
AND hour = 10;
-- plate ent 13FNH73 exit 5P2BI95
-- check interviews
SELECT *
FROM interviews
WHERE transcript LIKE '%bakery%';
-- check security footage within 10 mins after theft - who exited
SELECT *
FROM bakery_security_logs
WHERE day = 28
AND month = 7
AND year = 2021
AND hour = 10
AND minute BETWEEN 15 AND 26
AND activity LIKE 'exit';
-- check who was withdrawing money from ATM before the theft - 28.07 morning
SELECT *
FROM atm_transactions
WHERE day = 28
AND month = 7
AND year = 2021
AND atm_location LIKE 'Leggett Street'
AND transaction_type LIKE 'withdraw';
-- check who was calling for less than 1 min, check if tha guy bought ticket
SELECT *
FROM phone_calls
WHERE day = 28
AND month = 7
AND year = 2021
AND duration < 60;
-- check  what is the earliest flight from Fiftyville 29.07 - 8 fiftyville
SELECT *
FROM flights
WHERE origin_airport_id = 8
AND day = 29
AND month = 7
AND year = 2021
ORDER BY hour ASC, minute ASC LIMIT 1;
-- what is 4? id = 36 - where did he go?
SELECT *
FROM airports
WHERE id = 4;
-- who is flying?
SELECT *
FROM passengers
WHERE flight_id = 36;
-- who is thief?
SELECT *
FROM people, bank accounts, atm_transactions
WHERE phone_number IN (SELECT caller
    FROM phone_calls
    WHERE day = 28
    AND month = 7
    AND year = 2021
    AND duration < 60)
AND passport_number IN (SELECT passport_number
    FROM passengers
    WHERE flight_id = 36)
AND license_plate IN (SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28
    AND month = 7
    AND year = 2021
    AND hour = 10
    AND minute BETWEEN 15 AND 26
    AND activity LIKE 'exit')
AND atm_transactions.account_number = bank_accounts.account_number
AND bank_accounts.person_id = people.id
AND person_id IN (SELECT 
        (SELECT account_number
        FROM atm_transactions
        WHERE day = 28
        AND month = 7
        AND year = 2021
        AND atm_location LIKE 'Leggett Street'
        AND transaction_type LIKE 'withdraw')