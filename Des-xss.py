
import argparse
from lib.helper.helper import *
from lib.helper.Log import *
from lib.core import *
from random import randint
from lib.crawler.crawler import *

def check(getopt):
  	payload=int(getopt.payload_level)
	  if payload > 6 and getopt.payload is None:

