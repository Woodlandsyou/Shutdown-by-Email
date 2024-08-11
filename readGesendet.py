from imap_tools import MailBox
from subprocess import Popen
from sys import stdout

with MailBox('imap.web.de').login('email_reader@web.de', '2ID2FFEVQCOC2QFFHJAL', 'Gesendet') as mb:
    print(mb.folder.get())
    for msg in mb.fetch():
        print(msg.subject, msg.text)
        p = Popen(["powershell.exe", "E:\Email-Reader\shutdown.ps1"], stdout=stdout)
        p.communicate()
        mb.delete([msg.uid])