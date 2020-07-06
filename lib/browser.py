# Date: 19/05/2020
# Author: theVirtualMan
# Description: Browser

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from pyvirtualdisplay import Display
from threading import Thread, RLock


from .const import tor_proxy, tor_port, geckodriver_path, display_size

class Browser(object):

	def __init__(self, max_browsers):
		self.browslist = []
		self.lock = RLock()
		self.max_browsers = max_browsers
		self.thread_map = []

	def br(self):
				
		display = Display(visible=0, size = display_size)
		display.start()

		profile = FirefoxProfile()
		profile.set_preference('network.proxy.type', 1)
		profile.set_preference('network.proxy.socks', tor_proxy)
		profile.set_preference('network.proxy.socks_port', tor_port)
		profile.set_preference("network.proxy.socks_remote_dns", False)
		profile.update_preferences()

		driver = webdriver.Firefox(firefox_profile = profile, executable_path = geckodriver_path)
		# driver = webdriver.Firefox(executable_path = geckodriver_path)
		with self.lock:
			self.browslist.append(driver)

	# def remove_browser(self):

	def start_threads(self):
		threads = []
		for i in range(self.max_browsers):
			threads.append(Thread(target=self.br))
			try:
				threads[i].start()
			except selenium.common.exceptions.WebDriverException:
				pass ###################

		for thread in threads:
			thread.join()




	@property
	def browsers(self):
		print('Starting Browsers ...')
		self.start_threads()
		# self.br()
		print(len(self.browslist))
		return self.browslist
