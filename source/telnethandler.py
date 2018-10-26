"""This module will handle telnet connections and IO.

"""

import telnetlib
import queue
import threading

class TelnetHandler:
    
    def __init__(self, host, port, new_msg_callback):
        self.host = host
        self.port = port
        self.new_msg_callback = new_msg_callback
        self.terminate = False
        self.connection = telnetlib.Telnet(host, port)
        self.output_queue = queue.Queue()

    def read_line(self):
        line = self.connection.read_until(b"\n", 0.2)
        if len(line) > 0:
            self.output_queue.put(line)
            self.new_msg_callback()

    def send(self, userInput):
        self.connection.write((userInput + "\n").encode("ascii"))

    def run(self):
        while True:
            if self.terminate:
                break
            self.read_line()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def end(self):
        self.terminate = True



