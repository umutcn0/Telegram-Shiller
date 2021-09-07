from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, group0, group1, group2, group3, group4
import time
from telethon.errors import *
from threading import *
import asyncio

group0 = group0()
group1 = group1()
group2 = group2()
group3 = group3()
group4 = group4()


class Shill():
    def __init__(self,T_id,T_hash,owner,group):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = group
            self.message = fetch_text()

    def connection(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash)
        self.client.start()
        print("Hesaba giriş yapıldı")

    def join_channel(self):
        for var in self.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"{self.owner}. hesap {var} kanalına giriş yaptı.")
                time.sleep(300)

            except Exception as ex:
                print(ex)
                time.sleep(600)
                continue
        print("TÜM KANALLARA KATILIM SAĞLANDI.")

    def send_message(self):
        while True:
            i=0
            for var in self.channel_list:
                try:
                    if i < 20:
                        entity = self.client.get_entity(var)
                        self.client.send_message(entity, self.message)
                        print(f"{self.owner}. hesap mesaj gönderimi yaptı.")
                        print("________________________________________")
                        i+=1
                        time.sleep(5)
                    else:
                        i=0
                        time.sleep(300)
                except Exception as ex:
                    print(ex)
                    time.sleep(10)
                    continue

    def account(self):
        self.connection()
        #self.join_channel()
        self.send_message()

id0 = Shill("","","0",group0) #Account 0
id1 = Shill("","","1",group1) #Account 1
id2 = Shill("","","2",group2) #Account 2
id3 = Shill("","","3",group3) #Account 3
id4 = Shill("","","4",group4) #Account 4


t1 = Thread(target=id0.account)
t2 = Thread(target=id1.account)
t3 = Thread(target=id2.account)
t4 = Thread(target=id3.account)
t5 = Thread(target=id4.account)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

