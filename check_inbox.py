import imaplib
import email

def get_inbox(host,username,password):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message 
def parse_data(host,username,password):
    my_inbox = get_inbox(host,username,password)
    data = my_inbox
    if data !=[]:
        data_parser = data[0]
        if data_parser['from'] == 'GitHub <noreply@github.com>':
            main_data = data_parser['body']
            import re
            patt = re.compile(r'\d{6}')
            matches = patt.finditer(main_data)
            for match in matches:
                print(main_data[243: 249])
                code = main_data[243: 249]
                code  = str(code)
                return code
        else:
            return "no code"
    else:
        return "no code"


