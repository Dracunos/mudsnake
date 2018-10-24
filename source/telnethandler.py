"""This module will handle telnet connections and IO.

"""

import telnetlib
import queue
import threading

class TelnetHandler:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = telnetlib.Telnet(host, port)
        self.output_queue = queue.Queue()

    def read_line(self):
        line = self.connection.read_until(b"\n", 0.2)
        if len(line) > 0:
            self.output_queue.put(line)

    def send(self, userInput):
        self.connection.write((userInput + "\n").encode("ascii"))

    def run(self):
        while True:
            self.read_line()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()




