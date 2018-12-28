
import json
import requests
import configparser
import time
import urllib
import random
from channels.base_channel import BaseChannel


class Telegram(BaseChannel):

    def __init__(self, attitude):
        super(Telegram, self).__init__(attitude)
        self._url = "{}/bot{}/".format(self._attitude.config.get("TELEGRAM", "api_url"),
                                       self._attitude.config.get("TELEGRAM", "token"))

    def get_url(self, url):
        response = requests.get(url)
        return response.content.decode("utf8")


    def get_json_from_url(self, url):
        content = self.get_url(url)
        json_content = json.loads(content)
        return json_content


    def get_updates(self, offset=None):
        url = self._url + "getUpdates"
        if offset:
            url += "?offset={}".format(offset)
        return self.get_json_from_url(url)


    def get_last_chat_id_and_text(self, updates):
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        text = updates["result"][last_update]["message"]["text"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        return (text, chat_id)


    def get_last_update_id(self, updates):
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)


    def send_message(self, text, chat_id):

        try:
            url = self._url + \
            "sendMessage?text={}&chat_id={}".format(text, chat_id)
            self.get_url(url)
        except Exception as e:

            print(e)



    
    def save_updates(self, updates):
   
        for item in updates["result"]:
            name = item["message"]["from"]["first_name"]
            last_name = item["message"]["from"]["last_name"]
            is_human = not bool(item["message"]["from"]["is_bot"])
            telegram_id = int(item["message"]["from"]["id"])
            self._attitude.save_person(name, last_name, is_human, telegram_id)
            print(item["message"]["from"])

    def answer_each_one(self, updates):
        self.save_updates(updates)
        for item in updates["result"]:
            user = item["message"]["from"]
            chat = item["message"]["chat"]["id"]
            print(item["message"])
            if("text" in item["message"]):
                
                msg = item["message"]["text"]

                message_result = self._attitude.answer(msg, "TELEGRAM",  str(chat))
                self.send_message(message_result, chat)
            else:
                self.send_message(item["message"], chat)

    def serve(self):
        last_update_id = None

        while True:
            updates = self.get_updates(last_update_id)
            
            if len(updates["result"]) > 0:
                last_update_id = self.get_last_update_id(updates) + 1
                self.answer_each_one(updates)

            time.sleep(0.5)
