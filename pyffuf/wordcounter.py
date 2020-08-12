import subprocess

class Counter:
    def __init__(self,wordlist):
        self.wordlist = wordlist
    
    def count(self):
        try:
            numofword = subprocess.check_output('find /v /c "" ' + self.wordlist, shell=True)
            line = numofword.decode().split(" ")
            return line[-1].replace("\r\n","")
        except Exception as e:
            print(e)
    