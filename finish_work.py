import requests
from pprint import pprint
import json
from tqdm import tqdm


def get_token():
    with open("token.txt", "r") as file:
        return file.readline()


class YandexDisk:
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    @property
    def header(self):
        return self.get_headers()

    def get_upload_link(self):
        with open("token_vk.txt", "r") as file_object:
            token_vk = file_object.read().strip()
            URL = "https://api.vk.com/method/photos.get"
            params = {
                "user_ids": "711727951",
                "access_token": token_vk,
                "v": "5.131",
                "album_id": "wall",
                "photo_ids": "457239023,457239024,457239025,457239026,457239027",
                "extended": "1"
            }
            respons = requests.get(URL, params=params)
            res_json = respons.json()
            #pprint(res_json)
            list_link = []
            myList = []
            for res in res_json['response']['items']:
                for i in res['sizes']:
                    for k, v in i.items():
                        if k == 'height' and v == 1600:
                            img = i['url']
                            list_link.append(img)

                for k, v in res['likes'].items():
                    if k == 'count':
                        respons_items = dict.fromkeys(['file_name'], ["size"])
                        respons_items['file_name'] = f"{v}.jpg"
                        respons_items['size'] = "w"
                        myList.append(respons_items)
            pprint(list_link)
            print(myList)
            jsonString = json.dumps(myList, indent=4)
            print(jsonString)


            for l in tqdm(list_link, desc="Загрузка", ascii=False, ncols=50):
                #print(l)
                url_1 = l
                url_2 = "new/ghj"
                params = {"path": url_2, "url": url_1}
                response = requests.post(self.upload_url, params=params, headers=self.header)


yandex_client = YandexDisk(get_token())
yandex_client.get_upload_link()

