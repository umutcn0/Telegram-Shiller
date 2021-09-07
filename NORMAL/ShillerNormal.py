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

#id0 = Shill("7170514","545c2fbf8d373be9ef98742e15c1cc29","0",group0) #Anastasia
id1 = Shill("7926583","dc6e057634064908cfc3abd802246859","1",group1) #Tom
id2 = Shill("7774550","82e74cb492cbff8b6ba6bdc898bf3734","2",group2) #Johny
id3 = Shill("7484147","5bfc0ec7576a9c9a0ccde47b535b7042","3",group3) #Ruski
id4 = Shill("7452885","a3814383c5c84904b594dfb96d80b0d4","4",group4)


#t1 = Thread(target=id0.account)
t2 = Thread(target=id1.account)
t3 = Thread(target=id2.account)
t4 = Thread(target=id3.account)
t5 = Thread(target=id4.account)


#t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


#t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

