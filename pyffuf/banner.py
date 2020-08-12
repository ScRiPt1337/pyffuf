from clint.textui import puts, colored, indent

class Banner:
    def banner(self):
        with indent(4, quote='>>>'):
            puts(colored.red(str(self.bannerdata())))


    def bannerdata(self):
        data = r"""
   _____  ________     ___
  / _ \ \/ / _/ _/_ __/ _/
 / ___/\  / _/ _/ // / _/ 
/_/    /_/_//_/ \_,_/_/     
                    version 0.3 (beta)
        """
        return data
