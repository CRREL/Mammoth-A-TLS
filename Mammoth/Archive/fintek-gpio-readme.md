Decompressing and Compiling the Fintek GPIO SDK demo application from:
https://www.fintek.com.tw/index.php/mnu-swdevelopkitdl using a terminal.

1. mkdir /home/mammoth/Mammoth/Fintek
2. cd /home/mammoth/Mammoth/Fintek
3. cp source_location /fintek_demo_release-900360fe71-x86_64.tar.gz
4. tar xf fintek_demo_release-900360fe71-x86_64.tar.gz
5. nano (or vim) demo_gpio.c
6. change line 625 (change to your eSIO Type):
  - from: if (nRet = init_fintek_sio(eSIO_TYPE_F75111_I2C, 0, &sio_data)) {
  - to: if (nRet = init_fintek_sio(eSIO_TYPE_F81866, 0, &sio_data)) {
  - save & exit
7. make
8. rm fintek_demo_release-900360fe71-x86_64.tar.gz

**Note: eSIO_TYPE for the Stealth LPC-835 is F81866.  If your eSIO_TYPE is for a
different SIO chipset you will need to input the correct eSIO_TYPE for your system.


**Note 2: Replaced Stealth LPC-835X with a Stealth LPC-915 which does not include
GPIO functionality.  To achieve power switching for Riegl scanner, a custom Arduino relay shield
commanded via python serial rs232 commands is utilized.  Thus, the fintek software
is no longer needed.  Updates to come with those changes.
