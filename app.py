import os

def compose_ping_command(ip,target_filepath):
	date_formatting = "+%s"
	return "ping %s | while read line; do echo `date %s` - $line; done >> %s"%(ip,date_formatting,target_filepath)

def main():
	ip_list = [line.rstrip('\n') for line in open("ip_list.txt")]
	commands = [compose_ping_command(ip,"out_%s.txt"%(ip)) for ip in ip_list]
	res = "&".join(commands)
	# print("Process init for IPs")
	# [print(str(ip)) for ip in ip_list]
	os.system(res)

# unixtime date +%s

if __name__ == '__main__':
	main()