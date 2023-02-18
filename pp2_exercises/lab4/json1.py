import json

data = open('sample-data.json').read()

json_object = json.loads(data)
print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
data1 = json_object["imdata"]
for i in data1:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        description = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:50} {1:20} {2:7} {3:6}".format(dn,description,speed,mtu))