import random
import string
import requests


def gencode():
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(19))


class NitroGenerator:
	def __init__(self):
		self.codes = []
		self.check()
	
	def check(self):
		while True:
			code = gencode()
			self.codes.append(code)
			response = requests.get(
				"https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
			data = response.json()
			if data["message"] == 'You are being rate limited.':
				print("Not worked: " + code)
			else:
				print("Worked: " + code)
				file = open("workedcodes.txt", "a+")
				file.write("\n" + code)


NitroGenerator()