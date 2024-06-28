import json

with open('sample-data.json') as f:
    data = json.load(f)

interface_status = [
    {
        "DN": item["l1PhysIf"]["attributes"]["dn"],
        "Description": item["l1PhysIf"]["attributes"]["descr"],
        "Speed": item["l1PhysIf"]["attributes"]["speed"],
        "MTU": item["l1PhysIf"]["attributes"]["mtu"]
    }
    for item in data["imdata"]
]

output = "Interface Status\n"
output += "="*80 + "\n"
output += "{:<50} {:<20} {:<7} {:<5}\n".format("DN", "Description", "Speed", "MTU")
output += "-"*50 + " " + "-"*20 + " " + "-"*7 + " " + "-"*5 + "\n"

for entry in interface_status:
    output += "{:<50} {:<20} {:<7} {:<5}\n".format(
        entry["DN"], entry["Description"], entry["Speed"], entry["MTU"]
    )

print(output)