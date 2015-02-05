import os
os.chdir('../')

from toontown.chat import WhiteListData


def acceptWord():
    word = raw_input('> ').rstrip().lower()

    if word == 'exit()':
        saveChanges()
        return

    if word in LOCAL_LIST:
        print 'The word "%s" is already whitelisted.' % word
    else:
        LOCAL_LIST.append(word)
        print 'Added the word "%s" to the whitelist.' % word

    acceptWord()


def saveChanges():
    print 'Saving the whitelist...'

    with open('toontown/chat/WhiteListData.py', 'w') as f:
        f.write('WHITELIST = [\n')

        LOCAL_LIST.sort()
        addedWords = []

        for word in LOCAL_LIST:
            if word in addedWords:
                continue
            addedWords.append(word)

            if "'" in word:
                f.write('    "%s",\n' % word)
            else:
                f.write("    '%s',\n" % word)

        f.write(']')

    print 'Your changes have been saved! Make sure to push your changes!'


LOCAL_LIST = WhiteListData.WHITELIST


print 'Welcome to the Toontown Fellowship Whitelist Tool!'
print 'Type any word you want to add to the whitelist.'
print 'When you are done and want to save your changes, type "exit()"'


acceptWord()