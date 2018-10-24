"""This program will connect to MUD servers via telnet.
 Hopefully we will provide some useful functions like triggers,
aliases, macros, and maybe even some scripting for your mud
experience.
"""

import telnethandler
import threading

def main():
    connection = telnethandler.TelnetHandler("aardwolf.org", 23)
    connection.start()
    def f():
        while True:
            line = connection.output_queue.get()
            print(line.decode("ascii"))
    t = threading.Thread(target=f)
    t.start()
    while True:
        inn = input("> ")
        connection.send(inn)

















if __name__ == "__main__":
    main()

