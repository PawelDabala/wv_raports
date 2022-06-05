import imaplib
from pprint import pprint
import importlib, email
from seting import email_addr, email_passwd, _smtp

user = email_addr
password = email_passwd
imap_url = 'imap.gmail.com'

# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
# print(con.list())
con.select('INBOX')

result, data = con.fetch('2','(RFC822)')
pprint(data)
# raw = email.message_from_bytes(data[0][1])
# print(get_body(raw))


