#! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.
   #        py.exe mcb.pyw delete - deletes all keywords in shelf file
   #        py.exe mcb.pyw delete <keyword> - deletes that keyword from shelf file

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

   # Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv)==3 and sys.argv[1].lower()=='delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower()=='delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()