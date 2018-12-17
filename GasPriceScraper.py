# This script finds the first n listed
# gas prices on GasBuddy.com for a
# given zip code.


import requests
import re

num_gas_prices = 5 # 
zip_code = '46202'
prices = [0]*num_gas_prices

my_url = 'https://www.gasbuddy.com/home?search=' + zip_code +'&fuel=1'
page = requests.get(my_url)

page_as_string = page.content.decode("utf-8")

for ii in range(num_gas_prices):
	index = re.search('<span class="styles__price___3DxO5">',page_as_string)
	last_match = index.span()[1]
	prices[ii] = float(page_as_string[(last_match+1):(last_match + 5)])
	print(prices[ii])
	page_as_string = page_as_string[(last_match + 5):]

print("Mean: " + str(sum(prices)/num_gas_prices) )

