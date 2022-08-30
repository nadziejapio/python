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
-- check  what is the earliest flight from Fiftyville 29.07
SELECT 
