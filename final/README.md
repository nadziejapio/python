# LoL info bot
#### Video Demo:  [Link to the video](https://youtu.be/aowlEX_-1gY)
#### Description:
This app is about live checking if typed users are currently playing League of Legends and notyfying it directly on the desktop.

At the beggining CLI asks you to input username and tag then it sends requests to the Riot's API to check what are uuids of the users and write them in memory.

Next it checks repetivly if the users started ranked match. If so, it pushes the notification and starts to check if this match has ended. When finished, check the results of the user and pushes notyfication with info of winning/losing and some stats of the player and of the metch itself.

You are able to add how many users you want to check (handy with several teammates).

For now it is hardcoded only for EUROPE servers.
