import socket
from IPy import IP
from tqdm import tqdm

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ip_domain):
    port = 0
    with tqdm(total=1023) as prog_bar:
        while port < 1023:
            port += 1
            prog_bar.update(1)
            try:
                sock = socket.socket()
                sock.settimeout(0.5)
                sock.connect((ip_domain, port))
                if True:
                    l_open.append(port)
            except:
                pass

print(' Welcome!\n \n Press (q) and confirm (enter) to exit\n')
ipaddress = input(' Enter Target To Scan >>> ')

while True:
    if ipaddress == 'q':
        break
    ip_domain = check_ip(ipaddress)
    l_open = []

    scan_port(ip_domain)

    l_open = [str(i) for i in l_open]
    l_open = ", ".join(l_open)

    if l_open == '':
        print(f'No open ports in {ip_domain}')
        break
    else:   
        print(f'Open ports in {ip_domain}: {l_open}')
        break
