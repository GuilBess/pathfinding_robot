import json

rows = 3
cols = 11

path = [0, 1, 2, 3, 4, 15, 16, 17, 18, 19, 8, 9, 10, 21, 32]

prev = ""
orientation = ""
inst = []

for idx, i in enumerate(path[:-1]): 
    if path[idx + 1] == i + 1:
           orientation = "r"
    elif path[idx + 1] == i - 1:
        orientation = "l"
    elif path[idx + 1] == i - 11:
        orientation = "u"
    elif path[idx + 1] == i + 11: 
        orientation = "d"
    else:
        print("uh oh")


    if prev == "":
        inst.append("forward:1")
    else:
        if prev == orientation:
            inst[-1] = "forward:" + str(int(inst[-1].split(":")[-1]) + 1)
        else:
            if prev + orientation in ["rl", "lr", "ud", "du"]:
                inst.append("rotate:180")
            elif prev + orientation in ["rd", "dl", "lu", "ur"]:
                inst.append("rotate:90")
            else: 
                inst.append("rotate:-90")
            inst.append("forward:1")
    prev = orientation

print(inst)

out = {"commands":[]}

for i in inst:
    cmd = i.split(":")[0]
    arg = i.split(":")[1]
    out["commands"].append({"command":cmd, "args":[arg]})

with open("out.json", "w") as f:
    json.dump(out, f)