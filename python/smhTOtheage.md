<!-- smhTotheage apple script for macOS catalina -->  
<!-- This is a comment -->  
<!-- This is a apple script that I execute on the desktop using automator application to run the shell command as follows:

cd /Users/flurshelley/Desktop
osascript SMHtoTHEAGE.scpt

apple script:

tell application "Google Chrome"
	set currentTab to active tab of front window
	set currentURL to URL of currentTab
	if currentURL contains "smh.com.au" then
		set newURL to my replaceText(currentURL, "smh.com.au", "theage.com.au")
		set URL of currentTab to newURL
	end if
end tell

on replaceText(theText, oldText, newText)
	set AppleScript's text item delimiters to oldText
	set theTextItems to text items of theText
	set AppleScript's text item delimiters to newText
	set theText to theTextItems as string
	set AppleScript's text item delimiters to ""
	return theText
end replaceText
-->