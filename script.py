import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Menu Tambahan ')
print(a+'\t  UP,Down,right,Left,CTRL, etc ')
print(b+'\t  Creator :   CyberZiC')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] L04D1N6 6UYS..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Done!!!..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] sambil menunggu, jangan lupa subscribenya!!!')
sleep(1)
print(b+'\n[!] ')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] done !! ')
