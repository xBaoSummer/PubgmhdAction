from datetime import datetime

from src.env import EnvUtil
from src.http import HttpUtil


def signin():
    resp_json = HttpUtil.post_h5api('/act_dailysigninmonthly.php', {})
    if resp_json is not None:
        print("签到成功")


if __name__ == '__main__':
    print("##########################################")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # EnvUtil.init()
    signin()
