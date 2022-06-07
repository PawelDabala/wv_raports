from imap_tools import MailBox
from seting import email_addr, email_passwd, imap

# get all attachments from INBOX and save them to files
with MailBox(imap).login(email_addr, email_passwd, 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.subject)
        for att in msg.attachments:
            print('-', att.filename, att.content_type)
            with open(f'attachents/{att.filename}', 'wb') as f:
                f.write(att.payload)