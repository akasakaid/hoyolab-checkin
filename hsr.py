import time
import requests


urlLogin = "https://sg-public-api.hoyolab.com/event/luna/os/sign"

# edit cookie
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '44',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': '',
    'Host': 'sg-public-api.hoyolab.com',
    'Origin': 'https://act.hoyolab.com',
    'Referer': 'https://act.hoyolab.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

def countdown(t:int):
    while t:
        print(f"[!] tunggu sampai {t} detik untuk login selanjutnya ", flush=True,end="\r")
        t -= 1
        time.sleep(1)
    print("                                                      ", flush=True,end="\r")


def main():
    while True:
        res = requests.post(urlLogin,headers=headers,json={"act_id":"e202303301540311","lang":"en-us"})
        print(res.text)
        countdown(24 * 3600)

main()