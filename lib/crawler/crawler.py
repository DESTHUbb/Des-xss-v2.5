import requests
from lib.helper.Log import *
from lib.helper.helper import *
from lib.core import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing import Process

class crawler:
  
	visited=[]
	
	@classmethod
	def getLinks(self,base,proxy,headers,cookie):
		lst=[]
	
		conn=session(proxy,headers,cookie)


