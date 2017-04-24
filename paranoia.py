import os
import usb

if os.getuid()!=0:
	print("This program must be run as the super-user!")
	exit()
print("""
 _______  _______  ______    _______  __    _  _______  ___   _______        _______  __   __ 
|       ||   _   ||    _ |  |   _   ||  |  | ||       ||   | |   _   |      |       ||  | |  |
|    _  ||  |_|  ||   | ||  |  |_|  ||   |_| ||   _   ||   | |  |_|  |      |    _  ||  |_|  |
|   |_| ||       ||   |_||_ |       ||       ||  | |  ||   | |       |      |   |_| ||       |
|    ___||       ||    __  ||       ||  _    ||  |_|  ||   | |       | ___  |    ___||_     _|
|   |    |   _   ||   |  | ||   _   || | |   ||       ||   | |   _   ||   | |   |      |   |  
|___|    |__| |__||___|  |_||__| |__||_|  |__||_______||___| |__| |__||___| |___|      |___|  
""")

usb_list = list()
i = 1
for dev in usb.core.find(find_all=True):
	usb_list.append(dev)
	print(str(i) + ") " + usb.util.get_string(dev, dev.iProduct))
	i += 1
choice = str(i)
while int(choice) >= i and int(choice) > 0:
	choice = raw_input("Choice: ")
	if int(choice) >= i:
		print("Not a valid choice.")
print("Waiting for "+usb.util.get_string(usb_list[int(choice)-1], usb_list[int(choice)-1].iProduct)+" to be unplugged.\nCTRL+Z to quit.")
while True:
	try:
		usb.util.get_string(usb_list[int(choice)-1], usb_list[int(choice)-1].iProduct)
	except:
		break
os.system('shutdown -h now')
