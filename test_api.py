import requests
import yaml
import pprint

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)



def test_homework1(login, post_title):
    header = {"X-Auth-Token": login}
    # create post
    description = "ayda-post description"
    res = requests.post(
        data["address"] + "api/posts",
        params={
            "title": post_title,
            "description": description,
            "content": "content of post",
        },
        headers=header,
    )
    assert res.status_code == 200

    res = requests.get(
        data["address"] + "api/posts", headers=header
    )
    # print("api:", pprint.pformat(res.json()))
    listres = [i["description"] for i in res.json()["data"]]
    assert description in listres

def test_step1(login, post_title):
    header = {"X-Auth-Token": login}
    res = requests.get(
        data["address"] + "api/posts", headers=header
    )
    # print("api:", pprint.pformat(res.json()))
    listres = [i["title"] for i in res.json()["data"]]
    assert post_title in listres