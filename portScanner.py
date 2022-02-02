import socket
from IPy import IP
from tqdm import tqdm

ipaddress = input('[+] Enter Target To Scan: ')
port = 0
l_open = []

with tqdm(total=1023) as prog_bar:

    while port < 1023:
        port += 1
        prog_bar.update(1)
        try:
            sock = socket.socket()
            sock.settimeout(0.02)
            sock.connect((ipaddress, port))
            if True:
                l_open.append(port)
        except:
            pass

l_open = [str(i) for i in l_open]
l_open = ", ".join(l_open)

print(f'Open ports: {l_open}')
