

class OutputHandler():
    def __init__(self):
        self.buffer = []
        
    def read_to_buffer(self, output_queue):
        while not output_queue.empty():
            try:
                self.buffer.append(output_queue.get(False).decode("ascii"))
            except queue.Empty:
                break
        while len(self.buffer) > 10:
            self.buffer.pop(0)
        
        return "".join(self.buffer)
