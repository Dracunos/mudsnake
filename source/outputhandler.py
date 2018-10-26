import re

class OutputHandler():
    def __init__(self):
        self.buffer = []
        self.escape_code = "\x1b"
        
    def read_to_buffer(self, output_queue):
        while not output_queue.empty():
            try:
                outline = output_queue.get(False).decode("ascii")
                outline = outline.replace("\r", "")
                outline = self.handle_escape_codes(outline)
                self.buffer.append(outline)
            except Queue.Empty:
                break
        while len(self.buffer) > 100:
            self.buffer.pop(0)
        
        return "".join(self.buffer)
    
    def handle_escape_codes(self, line):
        if line.find(self.escape_code + "[") == -1:
            return line
        return re.sub(self.escape_code + "\[\d+.*?m", "", line)



"""
\x1b[33m
escapecode[codem
or
escapecode[code;code2;code3m

/* ANSI color codes: sequence = "ESCAPE + [ code_1; ... ; code_n m"
      -----------------------------------------
      0 reset
      1 intensity bold on
      2 intensity faint on
      3 italics on
      4 underline on
      5 blink on slow
      6 blink on fast
      7 inverse on
      9 strikethrough on
      10 ? TODO
      22 intensity normal (not bold, not faint)
      23 italics off
      24 underline off
      25 blink off
      26 RESERVED (for proportional spacing)
      27 inverse off
      29 strikethrough off
      30 fg black
      31 fg red
      32 fg green
      33 fg yellow
      34 fg blue
      35 fg magenta
      36 fg cyan
      37 fg white
      39 fg default
      40 bg black
      41 bg red
      42 bg green
      43 bg yellow
      44 bg blue
      45 bg magenta
      46 bg cyan
      47 bg white
      49 bg default
      50 RESERVED (for proportional spacing)
      51 framed on
      52 encircled on
      53 overlined on
      54 framed / encircled off
      55 overlined off

"""
