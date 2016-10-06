from telnetlib import Telnet
from decorator import decorator

class telnetSNMP:
    @classmethod
    def _init_(host, port = 23, timeout = 5):
        HOST = host
        PORT = port
        TIMEOUT = timeout
        TELNET = Telnet(HOST, PORT, TIMEOUT)
    @classmethod
    def do_conversation(expect_send = []):
        if expect_send:
            wait_for = l[0]
            del l[0]
            if l[0] == "":
                print(TELNET.read_very_eager())
            else:
                print(TELNET.read_until(wait_for))
            if l:
                send_this = l[0]
                del l[0]
                TELNET.write(send_this)
        telnet.read_all()
        TELNET.close()
    
if __name__ == "__main__":
    print("Hello")
    try:
        tn = telnetSNMP('127.0.0.1', port=50000)
    except Exception as ex:
        pass
    assert tn
    tn.do_conversation(['', 'ehlo localhost\n', '', 'quit\n'])
