
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import boto3
import json


class Granularity:
    daily = "DAILY"
    monthly = "MONTHLY"


class Cost:
    amount: int = None
    unit: int = None


class GetCost:
    def __init__(self) -> None:
        self.client = boto3.client('ce')

    def __get_cost_range(
        self,
        start: datetime,
        end: datetime,
        granularity: str
    ) -> Cost:
        res = self.client.get_cost_and_usage(
            TimePeriod={
                "Start": start.strftime("%Y-%m-%d"),
                "End": end.strftime("%Y-%m-%d")
            },
            Granularity=granularity,
            Metrics=[
                "BlendedCost", "UnblendedCost", "UsageQuantity"
            ]
        )
        cost_dict = res["ResultsByTime"][0]["Total"]["BlendedCost"]
        cost = Cost()
        cost.amount = round(float(cost_dict["Amount"]), 2)
        cost.unit = cost_dict["Unit"]

        return cost

    def get_cost_today(self) -> Cost:

        end = datetime.now()
        start = end-timedelta(days=1)
        return self.__get_cost_range(start, end, Granularity.daily)

    def get_cost_month(self) -> Cost:
        end = datetime.now()
        end = end.replace(day=1)
        end = end+relativedelta(months=1)
        start = end-relativedelta(months=1)
        return self.__get_cost_range(start, end, Granularity.monthly)
