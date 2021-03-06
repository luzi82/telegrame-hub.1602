import sys
sys.path.append('src')

import db
import _db_common

#########
# TEST

assert(db.get_item('_test',k0='VTWONHZP')==None)
test_item0 = db.new_item('_test',k0='VTWONHZP')
assert(db.get_item('_test',k0='VTWONHZP')!=None)

assert(db.rm_item('_test',k0='VTWONHZP'))
assert(db.get_item('_test',k0='VTWONHZP')==None)

assert(db.get_item('_test',k0='SDAWPRLI')==None)
test_item0 = db.new_item('_test',k0='SDAWPRLI')
assert(db.get_item('_test',k0='SDAWPRLI')!=None)

assert(db.rm_item('_test',test_item0['UUIDD']))
assert(db.get_item('_test',k0='SDAWPRLI')==None)

assert(db.get_item('_test',k0='EFAEHDNF')==None)
test_item0 = db.new_item('_test',k0='EFAEHDNF')
assert(db.get_item('_test',k0='EFAEHDNF')!=None)

assert(not db.rm_item('_test',test_item0['UUIDD'],k0='LAYQGIGY'))
assert(db.get_item('_test',k0='EFAEHDNF')!=None)

assert(db.rm_item('_test',test_item0['UUIDD'],k0='EFAEHDNF'))
assert(db.get_item('_test',k0='EFAEHDNF')==None)


#########
# USER

assert(not db.is_item_exist('user',rolee='VECPFUBZ') )

user_item = db.new_item('user',user_tgid='1234',rolee='VECPFUBZ',api_token='QCLOUEDB')

user_item = db.get_item('user',user_item['UUIDD'])
assert(user_item!=None)

user_item = db.get_item('user',user_tgid='1234')
assert(user_item!=None)

assert(db.is_item_exist('user',rolee='VECPFUBZ') )

user_item = db.get_item('user',api_token='QCLOUEDB')
# print(user_item)
assert(user_item['user_tgid']=='1234')

user_uuid = user_item['UUIDD']

########
# BOT

db.new_item('bot',user_uid=user_uuid,bot_tgid='DROPYXLW')

bot_item = db.get_item('bot',user_uid=user_uuid,bot_tgid='DROPYXLW')
print(bot_item)

bot_item_0 = db.new_item('bot',user_uid=user_uuid,bot_tgid='XXMETXWP')
db.new_item('bot',user_uid=user_uuid,bot_tgid='WLNSRWBL')

bot_item_list = db.get_item_list('bot',user_uid=user_uuid)
assert(len(bot_item_list)==3)

db.rm_item('bot',bot_item_0['UUIDD'])

bot_item_list = db.get_item_list('bot',user_uid=user_uuid)
assert(len(bot_item_list)==2)

########
# CHAT

db.new('chat',user_tgid='1234',bot_tgid='DROPYXLW',chat_tgid='MEQWHMSC')

chat_item = db.get('chat',user_tgid='1234',bot_tgid='DROPYXLW',chat_tgid='MEQWHMSC')
assert(chat_item!=None)
#print(f'chat_item = {chat_item}')

#db_chat.new_chat('1234:DROPYXLW','FSSMUDAA')
#db_chat.new_chat('1234:DROPYXLW','JDGARDNH')
db.new('chat',user_tgid='1234',bot_tgid='DROPYXLW',chat_tgid='FSSMUDAA')
db.new('chat',user_tgid='1234',bot_tgid='DROPYXLW',chat_tgid='JDGARDNH')

chat_item_list = db_chat.get_chat_list_from_bot('1234:DROPYXLW')
assert(len(chat_item_list)==3)

db_chat.rm_chat('1234:DROPYXLW:FSSMUDAA')

chat_item_list = db_chat.get_chat_list_from_bot('1234:DROPYXLW')
assert(len(bot_item_list)==2)

########
# HUB

db_hub.new_hub('1234','AUDVNEVS')

hub_item = db_hub.get_hub('1234:AUDVNEVS')
print(f'hub_item = {hub_item}')

db_hub.new_hub('1234','CXCXSIJJ')
db_hub.new_hub('1234','PXEOIXAV')

hub_item_list = db_hub.get_hub_list_from_user('1234')
assert(len(hub_item_list)==3)

db_hub.rm_hub('1234:CXCXSIJJ')

hub_item_list = db_hub.get_hub_list_from_user('1234')
assert(len(hub_item_list)==2)

########
# PUBLISHER

db_publisher.new_publisher('1234','XLZCXHXF')

publisher_item = db_publisher.get_publisher('1234:XLZCXHXF')
print(f'publisher_item = {publisher_item}')

db_publisher.new_publisher('1234','DHVCVRWG')
db_publisher.new_publisher('1234','MJUXIKII')

publisher_item_list = db_publisher.get_publisher_list_from_user('1234')
assert(len(publisher_item_list)==3)

db_publisher.rm_publisher('1234:DHVCVRWG')

publisher_item_list = db_publisher.get_publisher_list_from_user('1234')
assert(len(publisher_item_list)==2)

########
# CHAT-HUB

db_chat_hub.set_chat_hub('1234','1234:DROPYXLW','1234:AUDVNEVS')

chat_hub_item = db_chat_hub.get_chat_hub('1234:1234:DROPYXLW:1234:AUDVNEVS')
print(f'chat_hub_item = {chat_hub_item}')

db_chat_hub.get_chat_hub_list_from_chat('1234:DROPYXLW')
db_chat_hub.get_chat_hub_list_from_hub('1234:AUDVNEVS')

db_chat_hub.set_chat_hub('1234','1234:DROPYXLW','1234:PXEOIXAV')
db_chat_hub.rm_chat_hub('1234:1234:DROPYXLW:1234:PXEOIXAV')

########
# HUB-PUBLISHER

db_hub_publisher.set_hub_publisher('1234','1234:AUDVNEVS','1234:XLZCXHXF')

hub_publisher_item = db_hub_publisher.get_hub_publisher('1234:1234:AUDVNEVS:1234:XLZCXHXF')
print(f'hub_publisher_item = {hub_publisher_item}')

db_hub_publisher.get_hub_publisher_list_from_hub('1234:AUDVNEVS')
db_hub_publisher.get_hub_publisher_list_from_publisher('1234:XLZCXHXF')

db_hub_publisher.set_hub_publisher('1234','1234:AUDVNEVS','1234:MJUXIKII')
db_hub_publisher.rm_hub_publisher('1234:1234:AUDVNEVS:1234:MJUXIKII')
