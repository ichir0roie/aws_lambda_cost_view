import os
from module import get_cost, format
import json
import sys
import boto3
client = boto3.client("sns")

sys.path.insert(0, "module")


def handler(event: dict, context):

    gc = get_cost.GetCost()
    dc = gc.get_cost_today()
    mc = gc.get_cost_month()
    message = format.message.format(
        daily_value=dc.amount,
        daily_unit=dc.unit,
        monthly_value=mc.amount,
        monthly_unit=mc.unit
    )
    client.publish(
        TopicArn=os.environ["TOPIC_ARN"],
        Message=message,
        Subject='AWS Cost Notification.'
    )

    return {"result": "success"}


if __name__ == "__main__":
    # local
    res = handler(None, None)
    print(res)
