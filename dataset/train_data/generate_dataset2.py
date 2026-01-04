import json

f = open("", "r", encoding="utf-8")
lines = f.readlines()
f.close()

t_list = []

for line in lines[:]:
    l = json.loads(line)
    c1 = {};c2 = {};c3 = {};c4 = {};conversation_list=[]
    c1["from"] = "human"
    c1["value"] = "<image>图中这道菜的菜名是什么？这道菜中有哪些食材？"
    dish = l["dish"]
    i = l["ingredients"]
    c2["from"] = "gpt"
    c2["value"] = f"这道菜的名字是{dish},这道菜中的食材有{i}。"
    disease = l["disease"]
    c3["from"] = "human"
    c3["value"] = f"{disease}患者能吃这道菜吗？"
    result = l["result"]
    c4["from"] = "gpt"
    c4["value"] = f"{result}"
    conversation_list.append(c1);conversation_list.append(c2);conversation_list.append(c3);conversation_list.append(c4);
    # print(conversation_list)
    image_list = [l["image"]]
    # print(image_list)
    t = {}
    t["conversations"] = conversation_list
    t["images"] = image_list
    t_list.append(t)

f = open("", "w", encoding="utf-8")
re = json.dump(t_list, f, ensure_ascii=False)
f.close()