from colorama import *
import os
init() # inits colorama module
txtnum = [
	["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]
] # all possible combinations

os.system("cls") if os.name == "nt" else os.system("clear") # clears the terminal

print("""				
	████████╗░█████╗░  ████████╗██████╗░░█████╗░███╗░░██╗░██████╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
	╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
	░░░██║░░░╚██████║  ░░░██║░░░██████╔╝███████║██╔██╗██║╚█████╗░██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
	░░░██║░░░░╚═══██║  ░░░██║░░░██╔══██╗██╔══██║██║╚████║░╚═══██╗██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
	░░░██║░░░░█████╔╝  ░░░██║░░░██║░░██║██║░░██║██║░╚███║██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
	░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
	""")
print(Fore.YELLOW + "You can not enter anything expect 2-9 or A-Z.")
print(Fore.RED + "You can enter only 3 or 4 same numbers and you cant mix Latin with numbers." + Fore.RESET + "\n")
print("Enter text to translate: ")
entry = input("> ")

print(f"""
{Fore.YELLOW}Select operation mode.{Fore.RESET}
{Fore.BLUE}[0] - Latin to T9
{Fore.GREEN}[1] - T9 to Latin{Fore.RESET}
""")
help1 = int(input("> "))

def function(num): # the main program which suprisingly works
	times_pressed = 0
	last_pressed = int(num[0]) - 2
	text = ""
	space = ""

	for x in num:
		if x == " ": # space handling
			space = " "
		elif int(x) == 1:
			text += "1"
			text += space if space != "" else ""
			space = ""
		elif int(x) - 2 == last_pressed: # if number is same as previous
			if int(times_pressed) <= len(txtnum):
				times_pressed += 1
				text += space if space != "" else ""
				space = ""
			else: 
				text += txtnum[last_pressed][times_pressed - 1]
				times_pressed = 1
				text += space if space != "" else ""
				space = ""
		
		else: # if number isnt the same as previous
			text += txtnum[last_pressed][times_pressed - 1]
			times_pressed = 1
			last_pressed = int(x) - 2
			text += space if space != "" else ""
			space = ""
	
	text += txtnum[last_pressed][times_pressed - 1]
	return text

def function2(num):
	num = num.lower()
	result = ""
	space = " "
	for l in num :
		for i in range(len(txtnum)) :
			if l == " ":
				result = f"{result}{space}"
				continue
			elif (l in txtnum[i]) :
				for j in range(txtnum[i].index(l) + 1) :
					result = f"{result}{i + 2}"

		for x in range(len(result)):
				try:
					if result[x] == " " and result[x+1] == " ":
						result = result[:x] + result[x + 1:]
				except: # when loop goes through whole string, we break out of it
					break

	return result

try:
	if help1 == 0:
		t9 = function2(entry)
		latin = entry
	elif help1 == 1:
		t9 = entry
		latin = function(entry)
	os.system("cls") if os.name == "nt" else os.system("clear")
	print("""
		
	░█▀▀█ █▀▀ █▀▀ █──█ █── ▀▀█▀▀ █▀▀ 
	░█▄▄▀ █▀▀ ▀▀█ █──█ █── ──█── ▀▀█ 
	░█─░█ ▀▀▀ ▀▀▀ ─▀▀▀ ▀▀▀ ──▀── ▀▀▀
	""")
	print(f"""
	---------------------------------------------------
	  {Fore.BLUE}Latin text: {latin}
	  {Fore.YELLOW}T9 text: {t9+Fore.RESET}
	---------------------------------------------------
	""")
except:
	print("Exception occured! You probably entered more than 3 or 4 same numbers or mixed latin with numbers.")
