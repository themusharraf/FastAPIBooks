# from pprint import pprint
#
# import requests
#
# url = "http://127.0.0.1:8000/users/1"
#
# resp = requests.get(url)
#
# pprint(type(resp.json()) == dict)

from werkzeug.security import check_password_hash, generate_password_hash

s = "scrypt:32768:8:1$odrCbz48tp62xGkj$b689f5fe919ca1ac219afaa9af4681f4c6c6e7d998fb97320007d7ca060a053a04cfc81e3910f07c382fd7c2419a383ff63fb700286b3a5451a3c552dd77ab6a"

print(check_password_hash(password="ags90995", pwhash=s))
