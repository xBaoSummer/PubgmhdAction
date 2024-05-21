import os

import requests


def signin():
    try:
        resp = requests.post(
            'https://c.gp.qq.com/gp/api/php/act_dailysigninmonthly.php',
            {
                "algorithm": "v2",
                "encode": "2",
                "source": "heping_yingdi",
                "version": "3.1.96i",
                "appid": os.environ["appid"],
                "msdkEncodeParam": os.environ["msdkEncodeParam"],
                "openid": os.environ["openid"],
                "sig": os.environ["sig"],
                "timestamp": os.environ["timestamp"],
                "roleId": os.environ["roleId"],
            }
        )
        resp_json = resp.json()
        if resp_json["returnCode"] == 0:
            print("签到成功")
        else:
            print(resp_json["returnMsg"])
    except Exception as e:
        print(f"接口异常: {e}")


if __name__ == '__main__':
    signin()
