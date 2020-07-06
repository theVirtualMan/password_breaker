# password_breaker
Open for project name suggestions
A password breaker for Facebook, Twitter and Instagram. Made with python.

I am not resposible for any damage you cause, this is for educational purpose only

## Support

## Requirements
Python v3
TOR Proxy 

##Manual Configuration
Start torrc in the background (make sure that the ip changes for every 10-20 sec)

## Install Dependencies
python3 setup.py

## Help

## Usage
python3 password_breaker.py <service> <username> <passlist> -m <mode>

###service
instagram (yet to build)
twitter (yet to build)
facebook

###passlist
path to the file containing the password list

###mode
0: 32 threads
1: 16 threads
2: 8 threads
3: 4 threads

Each thread runs a new instance of a browser
If nothing is mentioned, by default 8 threads will run


