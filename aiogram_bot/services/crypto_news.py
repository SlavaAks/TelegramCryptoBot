import requests

head_url = "https://cryptopanic.com/api/free/v1/posts/?auth_token=3d5e43ea5fb815cfa731d4f9a8937532b05f825a"


#
# #"&currencies=XRP&filter=rising"
#
# response = requests.get(head_url+"&regions=ru"+"&currencies=XRP")

def all_crypto_news():
    head_url = "https://cryptopanic.com/api/free/v1/posts/?auth_token=3d5e43ea5fb815cfa731d4f9a8937532b05f825a"
    response = requests.get(head_url)
    j_responce = response.json()

    news_list = []
    for i in j_responce["results"]:
        news_list.insert(0, (i["id"], i["created_at"], i["title"], i["url"]))
    return news_list


if __name__ == '__main__':
    print(all_crypto_news())
