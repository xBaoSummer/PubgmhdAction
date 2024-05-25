from src.http import HttpUtil


def signin():
    resp_json = HttpUtil.post_h5api(
        "/act_dailysigninmonthly.php",
        {}
    )
    return resp_json


def tasklist():
    resp_json = HttpUtil.post_h5api(
        "/act_getscoretasklist.php",
        {}
    )
    return resp_json


def task_complete(task_id):
    resp_json = HttpUtil.post_h5api(
        "/completescoretask.php",
        {
            "taskId": task_id,
        }
    )
    return resp_json


def game_tool(tool_id, status):
    resp_json = HttpUtil.post_api(
        "/play/gametoolchange",
        {
            "id": tool_id,
            "status": status,
        }
    )
    return resp_json


def share(action, action_id):
    resp_json = HttpUtil.post_api(
        "/user/sharecallback",
        {
            "action": action,
            "id": action_id,
        }
    )
    return resp_json
