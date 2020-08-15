import json
facts = '{"hostname": "R1", "IP": "192.168.1.1", "Netmask": "255.255.255.0"}'
factsd = json.loads(facts)
print(factsd)
print(json.dumps(factsd, indent=4))
