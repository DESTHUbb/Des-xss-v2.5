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





