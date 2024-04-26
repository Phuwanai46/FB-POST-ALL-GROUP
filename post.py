import requests
import time

ACCESS_TOKEN = ""
MESSAGE = ""

def get_group_ids():
    url = "https://graph.facebook.com/me/groups?limit=200&access_token=" + ACCESS_TOKEN
    response = requests.get(url)
    data = response.json()

    group_ids = []
    for group in data["data"]:
        group_ids.append(group["id"])

    return group_ids

def post_message_to_group(group_id):
    post_url = "https://graph.facebook.com/" + group_id + "/feed?access_token=" + ACCESS_TOKEN
    post_data = {"message": MESSAGE}
    response = requests.post(post_url, data=post_data)

    if response.status_code == 200:
        print(f"โพสต์ข้อความในกลุ่ม {group_id} สำเร็จ")
    else:
        print(f"โพสต์ข้อความในกลุ่ม {group_id} ล้มเหลว: {response.status_code}")

if __name__ == "__main__":
    group_ids = get_group_ids()

    for group_id in group_ids:
        post_message_to_group(group_id)
