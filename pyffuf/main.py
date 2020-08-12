#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import asyncio
import sys
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup as bs
from clint.textui import puts, colored, indent

from pyffuf.banner import Banner
from pyffuf.checker import CHECKER


class FUZZER:
    def __init__(self, urlx, wordlist, total):
        self.urlx = urlx
        self.wordlist = wordlist
        self.totalsend = 1
        self.totalsuc = 0
        self.total = total

    async def checkpage(self, html):
        soup = bs(html, 'lxml')
        try:
            chex = str(soup.select_one('title').text).upper()
            # print(chex)
            if "NOT FOUND" in chex or "404" in chex:
                return False
            else:
                return True
        except:
            pass

    async def printf(self, cldata, data, status_code="", responsex=""):
        try:
            with indent(4, quote='>>>'):
                if status_code != 404 and status_code != 403:
                    if await self.checkpage(responsex):
                        puts(colored.green(str(cldata)) + colored.green(data) +
                             colored.green(str(status_code)))
                        self.totalsuc = 1 + self.totalsuc
                    else:
                        print('>>> ' + colored.red(str(cldata)) + data, end="\r")
                else:
                    print('>>> ' + colored.red(str(cldata)) + data, end="\r")
        except KeyboardInterrupt:
            pass

    async def fetch(self, session, url):
        try:
            async with session.get(url, ssl=False) as response:
                txt = await response.text()
                await self.printf(f"[{self.totalsend}/{self.total}]" + " ", url + " > ", status_code=response.status,
                                  responsex=txt)
                self.totalsend = 1 + self.totalsend
        except Exception as e:
            await self.printf("Error : " + str(e), "")
            self.totalsend = 1 + self.totalsend

    async def readlist(self):
        try:
            async with aiohttp.ClientSession() as session:
                with open(self.wordlist, mode='r') as f:
                    tasks = [await self.fetch(session, str(self.urlx.replace(
                        "PUFF", line).replace("\n", ""))) for line in f]
                    await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            self.done()
            return 0
        except UnicodeDecodeError:
            print('>>> ' + colored.red(str("There is a encoding error Please use a diffrent wordlist!")), end="\r")

    def fuzz(self):
        try:
            asyncio.run(self.readlist())
        except KeyboardInterrupt:
            self.done()

    def done(self):
        with indent(4, quote='>>>'):
            puts(colored.red(str(">>>>>>>>>>>>>>>>>>>>>>>>>>>> DONE!")))
            puts(colored.red(str("Total Dir Found : ")) + str(self.totalsuc))
            puts(colored.red(str("End Time : ")) +
                 str(datetime.now().strftime('%H:%M:%S')))
            sys.exit()


def main():
    banner = Banner()
    banner.banner()
    parser = argparse.ArgumentParser(
        description='Simple and Fast web fuzzer.')
    parser.add_argument('-u', '--url', metavar='', type=str, required=True,
                        help='Target url { example : https://google.com/PUFF }')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, required=True,
                        help='Wordlist path { example : /usr/share/wordlists/dirb/common.txt }')

    args = parser.parse_args()
    ch = CHECKER(args.url, args.wordlist)
    with indent(4, quote='>>>'):
        puts(colored.red(str(">>>>>>>>>>>>>>>>>>>>>>>>>>>> INFO!")))
    lenword = ch.check()
    with indent(4, quote='>>>'):
        puts(colored.red(str(">>>>>>>>>>>>>>>>>>>>>>>>>>>> ACTIVE!")))
    fuzzer = FUZZER(args.url, args.wordlist, lenword)
    fuzzer.fuzz()
    fuzzer.done()

if __name__ == '__main__':
    main()
