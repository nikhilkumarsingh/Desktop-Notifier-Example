# alternative for windows
# download notify-send from here: http://vaskovsky.net/notify-send/notify-send.zip
# unzip the file and add notify-send.exe to environment variables OR
# keep notify-send.exe in same folder where this python script is kept.


from subprocess import call

call(["notify-send", "This is title!", "This is message body!"])
