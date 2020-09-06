import os,subprocess as sp


def menu(menu):
	if menu != 0:
		a = sp.check_output("pm list packages -u", shell=True).decode("utf-8").splitlines()
		b = sp.check_output("pm list packages", shell=True).decode("utf-8").splitlines()
		packages = [i.split(":")[1] for i in a]
		packages_b= [i.split(":")[1] for i in b]
		hidden_packages = [i for i in packages if i not in packages_b]
		if menu == 1:
			for i in range(len(packages_b)):
				print('\033[92m',i+1,'\033[0m.',packages_b[i])
			s = input("Select package to hide: ")
			input(f"\033[93mPress enter to hide {packages[int(s)-1]}\033[0m ")
			os.system(f"pm hide {packages[int(s)-1]}")
			print("Done")
		else:
			if len(hidden_packages) != 0:
				for i in range(len(hidden_packages)):
					print('\033[92m',i+1,'\033[0m.',hidden_packages[i])
				s = input("Select package to unhide (a/A for all): ")
				if s != "a" and s != "A":
					input(f"\033[93mPress enter to unhide all package(s)\033[0m ")
					os.system(f"pm unhide {hidden_packages[int(s)-1]}")
				else:
					input(f"\033[93mPress enter to unhide all package(s)\033[0m ")
					for i in hidden_packages:
						os.system(f"pm unhide {i}")
				print("Done")
			else:
				print("No hidden package(s) available")
	else:
		print("Contact: \033[92mhttps://t.me/om_karjok\033[0m for asking a question")
		exit()
def home():
	print("""
	\033[92mApp Hider\033[0m v0.1
	by Karjok Pangesty
	===================
	""")
	print("""
1. Hide app
2. Unhide app
0. Exit
""")
	s = input("Select menu: ")
	while int(s) not in [i for i in range(3)]:
		s = input("Select menu: ")
	menu(int(s))
	#try:
	#		menu(int(s))
	#except:
	#		print("Contact: \033[92mhttps://t.me/om_karjok\033[0m for asking a question")
			
if __name__=='__main__':
	os.system("clear")
	if os.getuid() != 0:
		print("You must root for run this script")
		print("type: tsu")
	else:
		home()
