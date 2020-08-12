import os
import subprocess
import sys
from datetime import datetime

from clint.textui import puts, colored, indent
from wordcounter import Counter

class CHECKER:
    def __init__(self, url,wordlist):
        self.url = url
        self.wordlist = wordlist

    def printfx(self,cldata, data):
        with indent(4, quote='>>>'):
            puts(colored.red(str(cldata)) + data)

    def check(self):
        if os.path.isfile(self.wordlist):
            if os.name == "posix":
                numofword = subprocess.check_output(['wc', '-l', self.wordlist])
                line = numofword.decode().split(" ")
            else:
                line= []
                c = Counter(self.wordlist)
                line.append(c.count())
                line.append(self.wordlist)
                
        else:
            self.printfx("Wordlist File Not found!", "")
            sys.exit()
        self.printfx("Target : ", self.url)
        self.printfx("Wordlist : ", line[1].replace("\n", ""))
        self.printfx("Wordlist Size : ", line[0])
        self.printfx("Starting time : ", datetime.now().strftime('%H:%M:%S'))
        return line[0]
