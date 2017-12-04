from gmail import GMail, Message
from datetime import datetime

loop = True

while loop:
    now = datetime.now()
    hour = now.hour
    if hour == 7:
        gmail = GMail('c4e14phamthanhdat@gmail.com', 'c4e14phamthanh')
        msg = Message('Xin nghỉ ốm', to = 'c4e14phamthanhdat@gmail.com', text = 'Em xin phép hôm nay em nghỉ, vì em thích.')
        gmail.send(msg)
        loop = False
