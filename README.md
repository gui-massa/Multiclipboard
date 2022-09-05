# Multiclipboard
Create a "super" ctrl+C ctrl+V, with multiple content saved to the clipboard.

Python project.

This is a simple project, but very interesting to be able to use the clipboard on your aplications. 
Another good learning point is that we are controlling our application via terminal, creating keyworks to be read directly on the command line.

To test this:

## 1. Getting the first text (test1):
  Copy some text into your clipboard (ctrl+C);  
  Open the directory with the multiclipboard.py and type:  
  ```
  python3 multiclipboard.py save
  ```
  It will ask for a keyword. Use "test1" as an exemple;  
  
## 2. Getting another text (test2):
  Copy another text into your clipboard (ctrl+C);  
  Again type the following in the terminal;  
  ```
  python3 multiclipboard.py save
  ```
  It will ask for a keywork. Use "test2" as an exemple;  
  
## Unloading text to your clipboard (to be used on your ctrl+V):
  Type on the terminal:  
  ```
  python3 multiclipboard.py load
  ```
  It will ask for a keyword, use one previosly used to save texts on the steps above (test1 or test2).  
  Now unload (ctrl+V) the previously saved text anywhere.  

## Notes:  
  You can find a json file in the same directory as the application, where the information is kept.  
  Please note that this inforation is completely open to anyone entering the folder, so don't use it for passwords.  
  Is it possible to make something similar for passwords, that's for a future project I will be posting here.  
