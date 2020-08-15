import json
facts = '{"hostname": "Router_1", "os": "7.3", "interface f0/0": { "IP": "192.168.1.1", "netmask":"255.255.255.0", "status":"up"}}'
factsd = json.loads(facts)
print(factsd)
print(json.dumps(factsd, indent=4))
