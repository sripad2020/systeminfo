import os
print('1.Windows ')
print('2.Linux ')
s=int(input('enter the choice '))
if s==1:
    print('1.get the information of mac address ')
    print('2.get the information of active connections ')
    print('3.get the information of the ip address connections and mac address ')
    print('4.get the information about the drivers of the system ')
    print('5.get the information about all the directories of the system ')
    print('6.play a simple game ')
    mac=int(input('enter the choice: '))
    if mac==1:
        print('------------------------executing-----------------------')
        print(os.system('getmac /v /fo list'))
    elif mac==2:
        print('*************************executing***********************')
        print(os.system('netstat'))
    elif mac==3:
        print('----------*-*-*-*-*-*-*-*-*-*-*---*-*-*-*-*-*-*-*-*-*')
        print(os.system('ipconfig /all'))
    elif mac==4:
        print('*/*/*/**/*-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/')
        print(os.system('driverquery'))
    elif mac==5:
        print('+-+-+-+-+-+-+-+-+-+-+-+--+-+-+--+-+--+-+-++-+-+-+-+-+-++-')
        print(os.system('tree'))
    elif mac==6:
        print('-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*--**--*-*-*--*-*-*')
        print(os.system('echo %random%random%random%random%random%random%random%random%random%random%random%'))
else:
    print('1.get  the memory information ')
    print('2.get information about the interface, ip address and mac address ')
    print('3.to disable the interface ')
    print('4.to changee the mac address ')
    print('5.to get the information about the services of the system ')
    print('6.to get the information about the process of the system ')
    print('7.to get the information about the usb services in linux')
    print('8.to get the information about the pci devices ')
    print('9.to get the boot log of the linux ')
    print('10.to get the uptime of the machine ')
    mac3=int(input('enter the choice: '))
    if mac3==1:
        print('--------------------------------------------')
        print(os.system('df -H'))
    elif mac3==2:
        print('-------------------------------------------')
        print(os.system('ifconfig'))
    elif mac3==3:
        print('s-s*-s-*s-*s-s-s*s-s*s-s*s-s*s-s*s-*s-s*-s*')
        print(os.system('sudo ifconfig eth0 down'))
    elif mac3==4:
        print('s+s+s+s+s+s+s+s+s+s+s+s++s+s+s+s+s+s+s+s+s++s')
        print(os.system('macchanger -r eth0'))
    elif mac3==5:
        print('i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-i-')
        print(os.system('systemctl'))
    elif mac3==6:
        print('q-q-q-q--q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-q-qq-')
        print(os.system('w'))
    elif mac3==7:
        print('o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-')
        print(os.system('lsusb'))
    elif mac3==8:
        print('a*a*a*a*a*a*a*a*a**a*a*a*a*a*a*a*aa*')
        print(os.system('lspci'))
    elif mac3==9:
        print('s/s*s/s*s*s/s*s/s*s/s*s/s*s/s*s/s*s*')
        print(os.system('cat var/log/boot.log'))
    elif mac3==10:
        print('x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x')
        print(os.system('uptime'))