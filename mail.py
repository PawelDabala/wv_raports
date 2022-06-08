import os
from datetime import date, timedelta

from imap_tools import MailBox

from seting import EMAIL_ADR, EMAIL_IMAP, EMAIL_APP_PASSWD

# get all attachments from INBOX and save them to files
msg_from = ["lukasz.getter@phdmediadirection.com.pl", "no-reply@omniture.com", "pdabala@googlemail.com"]
today_date = date.today()
daybefore = date.today() - timedelta(days=5)
directory = "attachments"


def remove_files(directory: str):
    os.chdir(rf"{directory}")
    all_files = os.listdir()
    for f in all_files:
        os.remove(f)

def get_mails():
    remove_files(directory)
    os.chdir("..")

    with MailBox(EMAIL_IMAP).login(EMAIL_ADR, EMAIL_APP_PASSWD, "INBOX") as mailbox:
        for msg in mailbox.fetch():
            if msg.from_ in msg_from and msg.date.date() >= daybefore:
                for att in msg.attachments:
                    print("-", att.filename, att.content_type)
                    with open(rf"{directory}/{att.filename}", "wb") as f:
                        f.write(att.payload)
