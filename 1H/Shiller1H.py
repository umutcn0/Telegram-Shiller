from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, fetch_list
import time
from telethon.errors import *
from threading import *
import asyncio


class Shill():
    def __init__(self,T_id,T_hash,owner):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = fetch_list()
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
            for var in self.channel_list:
                try:
                    entity = self.client.get_entity(var)
                    self.client.send_message(entity, self.message)
                    print(f"{self.owner}. hesap mesaj gönderimi yaptı.")
                    print("________________________________________")
                    time.sleep(10)
                except Exception as ex:
                    print(ex)
                    time.sleep(600)
                    continue
            time.sleep(3600)

    def account(self):
        self.connection()
        self.join_channel()
        #self.send_message()


id0 = Shill("7994860","ae3cb45edb6547f21b61331a5c9a8ba5","5")

t1 = Thread(target=id0.account)

t1.start()

t1.join()
