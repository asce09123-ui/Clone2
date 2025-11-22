import os
from os import system

# Install dependencies untuk Termux
system('pkg install python -y')
system('pkg install chromium -y')
system('pip install selenium')
system('pip install requests')

print('Installation selesai untuk Termux')