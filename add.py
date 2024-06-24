import sys
import json
from urllib.parse import urlparse

def _add(file_name: str, info: dict):
    with open(file_name, "r") as reader:
        data: list = json.load(reader)
    data.append(info)
    with open(file_name, "w") as writer:
        json.dump(data, writer, indent=2)


def add(item: str, comment: str = "Scam"):
    if not item:
        print("missing parameters")
        exit(1)
    item = item.lower().strip()    
    if "." in item:
        if item.startswith("https://"):
            parsed = urlparse(item)
            item = parsed.netloc
        if item.startswith("www."):
            item = item[4:]
        _add("domain.json", {
            "scam_domain": item,
            "real_domain": "",
            "comment": comment
        })
    else:
        _add("address.json", {
            "address": item,
            "comment": comment
        })


if __name__ == "__main__":
    add(*sys.argv[1:])