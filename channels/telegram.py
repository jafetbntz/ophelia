
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
        #text = urllib.parse.quote_plus(text)
        result_text = ""
        try:

            if(text == "/start"):
                result_text = self._attitude.greetings()
            else:
                result_text = self._attitude.answer(text)

            #print(text)
            #result_text = str(eval(text))

        except Exception as e:
            result_text = str(e)
            print(e)

        url = self._url + \
            "sendMessage?text={}&chat_id={}".format(result_text, chat_id)
        self.get_url(url)


    def echo_all(self, updates):
        for update in updates["result"]:
            try:
                text = update["message"]["text"]
                chat = update["message"]["chat"]["id"]
                self.send_message(text, chat)
            except Exception as e:
                print(e)
    
    def serve(self):
        last_update_id = None

        while True:
            updates = self.get_updates(last_update_id)

            if len(updates["result"]) > 0:
                last_update_id = self.get_last_update_id(updates) + 1
                self.echo_all(updates)

            time.sleep(0.5)
