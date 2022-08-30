import json
from datetime import date


products = json.loads(input())
NAME_CONTAINS = input().split(' ')[1]
PRICE_GREATER_THAN = int(input().split(' ')[1])
PRICE_LESS_THAN = int(input().split(' ')[1])
DATE_AFTER = (input().split(' ')[1].split('.'))
DATE_BEFORE = (input().split(' ')[1].split('.'))





products = [v for v in {inp['name']: inp for inp in products[::-1]}.values()]

products.sort(key=lambda x : x["id"])


def filter_items(item):
    is_item_contain_name = NAME_CONTAINS in item['name']
    is_item_in_price = PRICE_GREATER_THAN <= item['price'] <= PRICE_LESS_THAN
    date_time_to_int_after = date(*list(reversed(list(map(int, DATE_AFTER)))))
    date_time_to_int_before = date(*list(reversed(list(map(int, DATE_BEFORE)))))
    item_date = date(*list(reversed(list(map(int, item['date'].split('.'))))))
    is_item_in_date = date_time_to_int_after <= item_date <= date_time_to_int_before
    return is_item_contain_name and is_item_in_price and is_item_in_date



result = json.dumps(list(filter(filter_items, products)))

print(result)
