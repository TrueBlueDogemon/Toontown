#!/bin/sh
cd ..

export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export DYLD_FRAMEWORK_PATH="Frameworks"

# Get the user input:
read -p "Username: " ttiUsername
read -p "Gameserver (DEFAULT:  www.ToontownFellowship.com): " TTI_GAMESERVER
TTI_GAMESERVER=${TTI_GAMESERVER:-"www.ToontownFellowship.com"}

# Export the environment variables:
export ttiUsername=$ttiUsername
export ttiPassword="password"
export TTI_PLAYCOOKIE=$ttiUsername
export TTI_GAMESERVER=$TTI_GAMESERVER

echo "==============================="
echo "Starting Toontown Fellowship"
echo "Username: $ttiUsername"
echo "Gameserver: $TTI_GAMESERVER"
echo "==============================="

ppython -m toontown.toonbase.ClientStart

