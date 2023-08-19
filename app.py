import os
from module import get_cost, format, my_slack
import json
import sys
# import boto3
# client = boto3.client("sns")

from env import env


def handler(event: dict, context):

    gc = get_cost.GetCost()
    dc = gc.get_cost_today()
    mc = gc.get_cost_month()
    message = format.message.format(
        title=env.SLACK_MESSAGE_TITLE,
        daily_value=dc.amount,
        daily_unit=dc.unit,
        monthly_value=mc.amount,
        monthly_unit=mc.unit
    )
    my_slack.send_message(message)

    return {"result": "success"}


if __name__ == "__main__":
    # local
    res = handler(None, None)
    print(res)
