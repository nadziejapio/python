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