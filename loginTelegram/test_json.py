import json
import requests
import os, subprocess


file = open('chats.json', 'rb')
data = file.readlines()
file.close()
#print(data)

links = []
'''
for cont in data:
	#print(cont.decode().find('http'))
	cont = cont.decode()
	i = cont.rfind('http')
	f = cont.rfind('"')
	if cont[i:f] != '':
		links.append(cont[i:f])

'''
#print(links)

file_link = open('test_links.txt', 'w')

tg_cli = 'bin/telegram-cli -W tg-server.pub -e '
cmd_line = '"import_channel_link '
link = 'https://t.me/joinchat/AAAAAEDrakjDNoJR0vtulw"'
cmd = tg_cli + cmd_line + link
#'bin/telegram-cli -W tg-server.pub -e "import_channel_link https://t.me/joinchat/AAAAAEDrakjDNoJR0vtulw"
#'"import_channel_link https://t.me/joinchat/AAAAAEDrakjDNoJR0vtulw"'

print(cmd)
'''
i = 0
for link in links:
	response = requests.get(link)
	print(response.status_code, i)
	file_link.write(link + ' | #response_200_OK: ' + str(response.status_code) + '\n')
	i += 1

'''
file_link.close()
print('finish script')


print(os.listdir())
print(os.chdir('/home/jack/tg'))
print(os.getcwd())
path = os.getcwd()

test = open('/home/jack/Downloads/test.txt', 'w')
resp = subprocess.call(cmd, shell=True, cwd=path, stdout=subprocess.PIPE)

print()

print(type(resp))
print(dir(resp))
print('#Response Subprocess: {0}'.format(resp))

test.write('#Response Subprocess: {0}'.format(resp))
test.close()




#link Bot @grupos_ti
#https://t.me/joinchat/AAAAAEDrakjDNoJR0vtulw

'''
install telegram-cli
https://elias.praciano.com/2014/04/instale-o-telegram-messenger-cli-no-linux/
https://t.me/vagastibr

o comando que eu usei pra joinar no grupo:
bin/telegram-cli -W tg-server.pub -e "import_channel_link https://telegram.me/joinchat/BCOBsj6vVeV62WJXeajheA"

channel_get_admins <channel> [limit=100] [offset=0]	Gets channel admins
channel_get_members <channel> [limit=100] [offset=0]	Gets channel members
channel_info <channel>	Prints info about channel (id, members, admin, etc.)
channel_invite <channel> <user>	Invites user to channel
channel_join <channel>	Joins to channel
channel_kick <channel> <user>	Kicks user from channel
channel_leave <channel>	Leaves from channel
channel_list [limit=100] [offset=0]	List of last channels


export_channel_link	Prints channel link that can be used to join to channel
export_chat_link	Prints chat link that can be used to join to chat

import_chat_link <hash>	Joins to chat by link
import_channel_link <hash>	Joins to channel by link

https://t.me/joinchat/AAAAAENj9POI_clcHufixg

#comando para infos do grupo
raph@blackpearl:~/tg$ bin/telegram-cli -W tg-server.pub -e "channel_info @botgrupos_ti"


'''
