from subprocess import Popen
from sys import stdout

p = Popen(["powershell.exe", "E:\Email-Reader\shutdown.ps1"], stdout=stdout)
p.communicate()