# Multiclipboard
Create a "super" ctrl+C ctrl+V, with multiple content saved to the clipboard.

Python project.

This is a simple project, but very interesting to be able to use the clipboard on your aplications. 
Another good learning point is that we are controlling our application via terminal, creating keyworks to be read directly on the command line.

To test this:

  Getting the first text (test1):
  1. Copy some text into your clipboard (ctrl+C);
  2. Open the directory with the multiclipboard.py and type "python3 multiclipboard.py save";
  3. It will ask for a keyword. Use "test1" as an exemple;
  
  Getting anothe text (test2):
  4. Copy another text into your clipboard (ctrl+C);
  5. Again type "python3 multiclipboard.py save" on the terminal;
  6. It will ask for a keywork. Use "test2" as an exemple;
  
  Unloading text to your clipboard (to be used on your ctrl+V):
  7. Type "python3 multiclipboard.py save" on the terminal.
  8. It will ask for a keyword, use one previosly used to save texts on the steps above. (test1 or test2)
  9. Now unload (ctrl+V) the previously saved text anywhere.

  Notes:
  1. You can find a json file in the same directory as the application, where the information is kept.
  2. Please note that this inforation is completely open to anyone entering the folder, so don't use it for passwords.
  3. Is it possible to make something similar for passwords, that's for a future project I will be posting here.
