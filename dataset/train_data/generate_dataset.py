import json

f1 = open(R"", "r", encoding="utf-8")
lines1 = f1.readlines()
f1.close()
f2 = open(R"", "r", encoding="utf-8")
lines2 = f2.readlines()
f2.close()

for line1 in lines1[:]:
    l1 = json.loads(line1)
    for line2 in lines2:
        l2 = json.loads(line2)
        if l2["name"] == l1["dish"]:
            l1["ingredients"] = l2["ingredients"]
    print(l1)

    re = json.dumps(l1, ensure_ascii=False) + '\n'
    f = open(R"", "a", encoding="utf-8")
    f.write(re)
    f.close()