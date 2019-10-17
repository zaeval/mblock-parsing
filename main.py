import requests
import json

ROOT_URL = "https://ide.mblock.cc/#/"
NEW_PROJECT_URL = ROOT_URL + "projects/projects"
PROJECT_CHANGE_SAVE_URL = ROOT_URL + "web/saveas"

API_URL = "https://eu.passport2.makeblock.com/v1/"
LOGIN_URL = API_URL + "user/login"
EMAIL_REGISTER = "user/emailregisternocode"

account = "chl8273@naver.com"
password = "chlworkd13"

header = {
    "Referer": "https://ide.mblock.cc/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}


def regist(ses, account, password):
    ses.post(API_URL + EMAIL_REGISTER, data={"email": account, "password": password})


def login(ses, account, password):
    header = {
        "Referer": "https://ide.mblock.cc/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    res = ses.post(LOGIN_URL, data={
        "account": account,
        "password": password
    }, headers=header)
    # cookie = res.headers['Set-Cookie'][:89]
    # print(cookie)
    # headers = {"Cookie": cookie}
    print(res.text)
    # response = s.get(ROOT_URL, headers=headers)
    # print(response.text)
    print(res.text)
    print(res.status_code)
    # response = s.get(ROOT_URL, headers=headers)
    # print(response.text)

    response = s.get(ROOT_URL, headers=header)


# def save(ses):
# res = ses.post("https://planet.mblock.cc/getprojectbycpids", projectIds=[projectIds])
# print(res.text)


def get_list(ses):
    res = ses.post("https://planet.mblock.cc/cloud/pro/list")
    print(res.text)


s = requests.session()
# regist(s, account, password)
# login(s, account, password)
res = s.post(LOGIN_URL, data={
    "account": account,
    "password": password
}, headers=header)
print(res.text)
res_header = json.loads(res.text)['data']
print(res_header['token'])
header = {
    "token": res_header['token'],
    "utoken": res_header['token'],
}
print(header)
# cookie = dict(res.headers['Set-Cookie'][:89])
# print(cookie)
# headers = {"Cookie": cookie}
response = s.get(ROOT_URL, headers=header)
print(response)
test = s.get("https://planet.mblock.cc/cloud/token/coverupload")
print(test.text)
