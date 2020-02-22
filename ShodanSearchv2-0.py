import os, sys

#[!]Shodan API Key:

SHODAN_API_KEY = "BlfnLSqwU8m0N0fom6IdVcgjS2cyd18T"#this is a randomly acquired key for the community to use, if its out of uses get your own key
#SHODAN_API_KEY = ""#Enter your shodan API key here and remove this comment and the hashtag before SHODAN_API_KEY = ""(<-leave this)
#you can easily get an api key by making an acount at shodan.io with a temp mail account :)

run = os.system

txtgreen = '\033[32m'
txtred = '\033[31m'
txtgreen = '\033[32m'
txtyellow = '\033[33m'
txtwhite = '\033[37m'
txtcyan = '\033[36m'

endline = txtyellow + '[Enter] When Finished.' + txtwhite
###################################################################################################
def CheckUpdate():
	run('pip3 install shodan; pip3 install webbrowser; shodan init ' + SHODAN_API_KEY)
	print('Finished! Entering Shodan')
	run('clear')
###################################################################################################
CheckUpdate()

import shodan, webbrowser#import updated modules

api = shodan.Shodan(SHODAN_API_KEY)

run('clear')
__author__ = '\nRawVendetta - GitHub\n'
banner = txtred + '''  ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄       ███▄    █ 
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ 
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒      ░   ░ ░ 
      ░   ░  ░  ░    ░ ░     ░          ░  ░         ░ 
                           ░                           
''' + '\nShodan Command Line Version 2.0\n' + txtyellow + __author__ + txtwhite
###################################################################################################
def targetidentify():
	targetidentify.target = input(txtwhite + 'Enter Search Criteria:')
###################################################################################################
def browser():
	option = int(input(txtcyan + '[1]OpenInBrowser [2]Quit\n' + txtwhite + 'Choice:'))
	results = api.search(targetidentify.target)#searching again thats why its a little slow
	lines = '-'
	linesbanner = lines.center(55, '-')

	if option ==1:
		url = input('Enter The IP Address To Connect:')
		port = ':' + str(input('Enter port to connect to [80, 8080, etc.]\nPort:'))
		print('Checking if ' + url + ' is a honeypot...' + txtgreen + '\n[HONEYSTATE]')
		os.system('shodan honeyscore ' + url)
		print(txtwhite + '')
		input(txtcyan + '[ENTER]Okay& Continue\n' + txtwhite)
		webbrowser.open('http://' + url + port)
		print(url + ' open in webbrowser window.')
		input(txtcyan  + '[ENTER]Done' + txtwhite)
		os.system('clear')
		print(banner + txtgreen + 'Results Found: {}'.format(results['total']))
		print(linesbanner)
		for result in results['matches']:
			print(txtwhite + '{}'.format(result['ip_str']))
		print(txtgreen + linesbanner)
		browser()
			
	elif option ==2:
		print(txtred + 'User Exit.' + txtwhite)
		sys.exit()
	else:
		print(txtred + 'Invalid Choice, Please Try Again.' + txtwhite)
###################################################################################################
def main():
	print(banner)
	targetidentify()
	#target = input(txtwhite + 'Enter Search Criteria:')
	choice = int(input(txtcyan + '[1]AllInfo [2]IpList\n' + txtwhite + 'Choice:'))
	lines = '-'
	linesbanner = lines.center(55, '-')
	bar = '|'
	sidebars = bar.rjust(54, ' ')
	if choice == 1:
			#Search Shodan API
		print('Querying for ' + targetidentify.target + ' with AllInfo\n')
		results = api.search(targetidentify.target)

			#Show Results
		print(txtgreen + 'Results Found: {}'.format(results['total']))	
		if results['total'] == 0:
			input(txtred + 'There were no results for "' + targetidentify.target + '"' + '\nExiting...' + txtcyan + '\n[OKAY]' + txtwhite)
			os.system('clear')
			main()
		else:
			print(linesbanner)
			for result in results['matches']:
				print(txtwhite + 'IP: {}'.format(result['ip_str']))
				print(result['data'].strip())
			print(txtgreen + linesbanner)
			browser()

	elif choice == 2:
		print('Querying for ' + targetidentify.target + ' with IpList\n')
		results = api.search(targetidentify.target)#Searcb Shodan API
		print(txtgreen + 'Results Found: {}'.format(results['total']))
		if results['total'] == 0:
			input(txtred + 'There were no results for "' + targetidentify.target + '"' + '\nExiting...' + txtcyan + '\n[OKAY]' + txtwhite)
			os.system('clear')
			main()
		else:
			print(linesbanner)
			for result in results['matches']:
				print(txtwhite + '{}'.format(result['ip_str']))
			print(txtgreen + linesbanner)
			browser()

	elif KeyboardInterrupt:
		print('Script Cancel [Success]')

	else:
		print(txtred + 'Invalid Choice, Please Try Again.' + txtwhite)
		return main
###################################################################################################

main()
