s = input("File name: ").lower().strip().replace("jpg", "jpeg")
t = "application/octet-stream"
ext = s.split(".")[-1]
fname = s.split(".")[0]
if ext in ["jpeg", "gif", "png"]:
    t = "image/" + ext
elif ext in ["pdf", "zip"]:
    t = "application/" + ext
elif ext in "txt":
    t = "text/" + fname
print(t)
