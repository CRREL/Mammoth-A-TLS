Decompressing and Compiling the Fintek GPIO SDK demo application from:
https://www.fintek.com.tw/index.php/mnu-swdevelopkitdl using a terminal.

1. mkdir /home/mammoth/Mammoth/Fintek
2. cd /home/mammoth/Mammoth/Fintek
3. cp <source location> /fintek_demo_release-4ee1af2d10-i686.tar.gz
4. tar xf fintek_demo_release-4ee1af2d10-i686.tar.gz
5. make

We do not use the demo application to control the Stealth LPC-835 GPIO, however
we do use Fintek's library through our own scripts to control the GPIO.
