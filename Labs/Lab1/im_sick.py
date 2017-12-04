from gmail import GMail, Message
from random import choice
from datetime import datetime

#get current datetime
now = datetime.now()
hour = now.hour
#html5-editor.net
template = [
    '''<p>Em xin phep nghi.</p>
    <p>{{sickness}}</p>
    <p>Hay.&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
    <p><em>Hoc sinh,</em></p>
    <p><em>Dat</em></p>''',

    '''<p>Em thua co em xin phep duoc gui mail.</p>
    <p>{{sickness}}</p>
    <p>Hay.&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
    <p><em>Hoc sinh,</em></p>
    <p><em>Dat</em></p>''',

    '''<p>Em thua co em co chuyen quan trong can lien lac.</p>
    <p>{{sickness}}</p>
    <p>Em se chep bai day du.</p>
    <p><em>Hoc sinh,</em></p>
    <p><em>Dat</em></p>'''
]

reasons = [
    '''Hom nay em thich nghi.''',
    '''Hom nay em bi om em xin phep duoc nghi.''',
    '''Hom nay em co viec ca nhan nen xin phep duoc nghi.'''
]
# login

gmail = GMail('c4e14phamthanhdat@gmail.com', 'c4e14phamthanh')

# msg = Message('Xin nghỉ ốm', to = 'c4e14phamthanhdat@gmail.com', text = 'Em xin phép hôm nay em nghỉ, vì em thích.')
# msg = Message('Xin nghỉ ốm', to = 'c4e14phamthanhdat@gmail.com', html = 'Em xin phép hôm nay em nghỉ, vì <b>em thích</b>.')
reason = choice(reasons)
content = choice(template)
use_content = content.replace("{{sickness}}", reason)

msg = Message('Xin nghỉ ốm', to = 'c4e14phamthanhdat@gmail.com', html = use_content)
gmail.send(msg)
