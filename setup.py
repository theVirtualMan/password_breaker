import os
import time

# selenium
os.system('clear')
print('installing Selenium....\n\n\n')
os.system("python3 -m pip install selenium")
time.sleep(2)


# geckodriver
os.system('clear')
print('installing geckodriver....\n\n\n')

os.system('firefox -v > tmp')
result   =  open('tmp', 'r').read()            # result var reads the output
marker   = result.find('Firefox') + 8          # marker marks the 8th letter from the word "Firefox"
version  = result[marker:].splitlines()[0]     # spliting the output, the version is something like aa.bb.cc
a,b,c = version.split(".")                     # a is the var with the aa
os.remove('tmp')                               # removing the temporary file

FirefoxVersion = int(a)

if FirefoxVersion >= 60:
	first = 26
	second = 0
	OS_bit = 64


elif FirefoxVersion > 57:
	first = 21
	second = 0
	OS_bit = 64

else:
	first = 16
	second = 1
	OS_bit = 64

os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,OS_bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))

os.system('mkdir webdrivers > tmp')
os.system('mv geckodriver webdrivers/')
os.remove('tmp')

time.sleep(2)






# pyvirtualdisplay
os.system('clear')
print('installing pyvirtualdisplay....\n\n\n')
os.system("sudo apt-get install -y python3-pyvirtualdisplay")
time.sleep(2)

os.system('clear')

#tor