# encoding: utf-8
import json
import requests
from robot_view.settings import SMS_SEND_URL, SMS_CONTENT_TEXT


class YunPian(str):
    def __int__(self, api_key):
        self.api_key = api_key
        self.single_send_url = SMS_SEND_URL

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": SMS_CONTENT_TEXT.format(code=code)
        }
        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("")
    yun_pian.send_sms("2018", "15033536789")
