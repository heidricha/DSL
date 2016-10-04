from telnetlib import Telnet

try:
    tn = Telnet('127.0.0.1', port=25, timeout=5)
except Exception as ex:
    print(ex)
assert tn

print(tn.read_very_eager())
tn.write('ehlo localhost\n')
print(tn.read_very_eager())
tn.write('quit\n')
print(tn.read_all())
tn.close