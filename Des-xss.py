import argparse
from lib.helper.helper import *
from lib.helper.Log import *
from lib.core import *
from random import randint
from lib.crawler.crawler import *

def check(getopt):
  	payload=int(getopt.payload_level)
	  if payload > 6 and getopt.payload is None:
       		Log.info("Do you want use custom payload (Y/n)?")
		answer=input("> "+W) 
		if answer.lower().strip() == "y":
			Log.info("Write the XSS payload below")
			payload=input("> "+W)

	else:
			payload=core.generate(randint(1,6))
	
	else:
		payload=core.generate(payload)

	return payload if getopt.payload is None else getopt.payload

def start():
	parse=argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,usage="Des-xss -u <target> [options]",epilog=epilog,add_help=False)

	pos_opt=parse.add_argument_group("Options")
	pos_opt.add_argument("--help",action="store_true",default=False,help="Show usage and help parameters")
	pos_opt.add_argument("-u",metavar="",help="Target url (e.g. http://testphp.vulnweb.com)")
	pos_opt.add_argument("--depth",metavar="",help="Depth web page to crawl. Default: 2",default=2)
	pos_opt.add_argument("--payload-level",metavar="",help="Level for payload Generator, 7 for custom payload. {1...6}. Default: 6",default=6)
	pos_opt.add_argument("--payload",metavar="",help="Load custom payload directly (e.g. <script>alert(2005)</script>)",default=None)
	pos_opt.add_argument("--method",metavar="",help="Method setting(s): \n\t0: GET\n\t1: POST\n\t2: GET and POST (default)",default=2,type=int)
	pos_opt.add_argument("--user-agent",metavar="",help="Request user agent (e.g. Chrome/2.1.1/...)",default=agent)










