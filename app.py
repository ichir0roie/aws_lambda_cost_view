import json
import sys

from module.get_cost import *

sys.path.insert(0, "module")


def handler(event: dict, context):

    gc = GetCost()
    dc = gc.get_cost_today()
    mc = gc.get_cost_month()

    result = {
        " daily ": f"{dc.amount}[{dc.unit}]",
        "monthly": f"{mc.amount}[{mc.unit}]",
    }

    return json.dumps(result)


if __name__ == "__main__":
    # local
    res = handler(None, None)
    print(res)
