import json
facts = '{"hostname": "nxosv", "os": "7.3", "IP": "192.168.1.1"}'
factsd = json.loads(facts)
print(factsd)
print(json.dumps(factsd, indent=4))
