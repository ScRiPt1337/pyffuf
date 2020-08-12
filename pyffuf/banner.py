from clint.textui import puts, colored, indent


def banner():
    with indent(4, quote='>>>'):
        puts(colored.red(str(bannerdata())))


def bannerdata():
    data = r"""
   _____  ________     ___
  / _ \ \/ / _/ _/_ __/ _/
 / ___/\  / _/ _/ // / _/
/_/    /_/_//_/ \_,_/_/
                version 0.1 (beta)
    """
    return data
