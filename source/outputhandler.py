

class OutputHandler():
    def __init__(self):
        self.buffer = []
        
    def read_to_buffer(self, output_queue):
        if len(self.buffer) > 0:
            print((self.buffer[-1]))
        while not output_queue.empty():
            try:
                outline = output_queue.get(False).decode("ascii")
                print("l:" + outline)
                self.buffer.append(outline)
            except queue.Empty:
                break
        while len(self.buffer) > 10:
            self.buffer.pop(0)
        
        return "".join(self.buffer)
