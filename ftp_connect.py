import os
from time import sleep

import paramiko

sftpHost = "194.145.229.133"
sftpPort = 22
uname = "PHD_Getter_Łukasz"
privateKeyFilePath = r"login\pem_privatekey"
password = "Xu%KP8WObh9@LA="
passphrase = "218522gttr"
directory = "attachments"


def connect_ftp():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=sftpHost,
        username=uname,
        password=password,
        allow_agent=False,
        key_filename=privateKeyFilePath,
        passphrase=passphrase,
    )

    ftp = client.open_sftp()
    files = ftp.listdir()
    print(files)

    #get file list
    files = [file for file in os.listdir(directory) if file.endswith(".csv")]

    for file in files:
        if file.find("totalvisits") != -1:
            print("totalvisits")
            ftp.put(
                rf"{directory}\{file}",
                f"/VWCV PHD Adobe/2021/Daily 2022/Totalvisits/{file}",
            )

        if file.find("visits_carline") != -1:
            print("viits_carline")
            ftp.put(
                rf"{directory}\{file}",
                f"/VWCV PHD Adobe/2021/Daily 2022/Visits_carline/{file}",
            )

        if file.find("visits_channel") != -1:
            print("visits_channel")
            ftp.put(
                rf"{directory}\{file}",
                f"/VWCV PHD Adobe/2021/Daily 2022/Visits_channel/{file}",
            )
        sleep(2)

    ftp.close()


print("Send Files")
