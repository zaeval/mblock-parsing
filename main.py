import requests
import json

ROOT_URL = "https://ide.mblock.cc/#/"
NEW_PROJECT_URL = ROOT_URL + "projects/projects"
PROJECT_CHANGE_SAVE_URL = ROOT_URL + "web/saveas"

AUTHORIZE_API_URL = "https://eu.passport2.makeblock.com/v1"
LOGIN = "/user/login"
EMAIL_REGISTER = "/user/emailregisternocode"

account = "chl8273@naver.com"
password = "chlworkd13"

CONTENT_API_URL = "https://planet.mblock.cc"
LIST = "/cloud/pro/list"
GET_PROJECT = "/getprojectbycpids"
SHARE = "/project/ThirdPlatform"
# https://ide.mblock.cc/share.html?98628
# 85471
# blob:https://ide.mblock.cc/7c34c362-3302-490d-9848-d36f485b0f24

header = {
    "Referer": "https://ide.mblock.cc/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}


def regist(ses, account, password):
    ses.post(AUTHORIZE_API_URL + EMAIL_REGISTER, data={"email": account, "password": password})


def login(ses, account, password):
    header = {
        "Referer": "https://ide.mblock.cc/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    res = ses.post(AUTHORIZE_API_URL + LOGIN, data={
        "account": account,
        "password": password
    }, headers=header)
    return res


# def save(ses):
# res = ses.post("https://planet.mblock.cc/getprojectbycpids", projectIds=[projectIds])
# print(res.text)


def getList(ses, token):
    headers = {'token': token, 'utoken': token}

    res = ses.post(CONTENT_API_URL + LIST, headers=headers)
    return res


def share(ses, token, id):
    headers = {'token': token, 'utoken': token, 'accesstoken': None}
    res = ses.post(CONTENT_API_URL + SHARE, headers=headers, data={{"cloudProjectId": id}})
    return res


session = requests.session()
res = login(session, account, password)
res = json.loads(res.text)

token = res["data"]["token"]
res = getList(session, token)
res = json.loads(res.text)

id = res["data"]["cloudProjectList"][1]['id']

res = share(session, token, int(id))
print(res.text)
# print(res["data"])
# test = s.get("https://planet.mblock.cc/cloud/token/coverupload")
# print(test.text)
