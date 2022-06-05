from datetime import date

from imap_tools import MailBox

from seting import EMAIL_ADR, EMAIL_IMAP, EMAIL_PASSWD

# get all attachments from INBOX and save them to files
msg_from = "pdabala@googlemail.com"
today_date = date.today()

with MailBox(EMAIL_IMAP).login(EMAIL_ADR, EMAIL_PASSWD, "INBOX") as mailbox:
    for msg in mailbox.fetch():
        if msg.from_ == msg_from and msg.date.date() == today_date:
            print(msg.from_, msg.subject)
            for att in msg.attachments:
                print("-", att.filename, att.content_type)
                with open(f"attachments/{att.filename}", "wb") as f:
                    f.write(att.payload)
