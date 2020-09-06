import os,subprocess as sp


def menu(menu):
	if menu != 0:
		a = sp.check_output("pm list packages", shell=True).decode("utf-8").splitlines()
		packages = [i.split(":")[1] for i in a]
		for i in range(len(packages)):
			print('\033[92m',i+1,'\033[0m.',packages[i])
		if menu == 1:
			s = input("Select package to hide: ")
			input(f"Press enter to hide {packages[int(s)-1]} ")
			os.system(f"pm hide {packages[int(s)-1]}")
			print("Done")
		else:
			s = input("Select package to unhide: ")
			input(f"Press enter to unhide {packages[int(s)-1]} ")
			os.system(f"pm unhide {packages[int(s)-1]}")
			print("Done")
	else:
		print("Contact: \033[92mhttps://t.me/om_karjok\033[0m for asking a question")

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
	try:
		menu(int(s))
	except:
		print("Contact: \033[92mhttps://t.me/om_karjok\033[0m for asking a question")
if __name__=='__main__':
	os.system("clear")
	if os.getuid() != 0:
		print("You must root for run this script")
		print("type: tsu")
	else:
		home()
