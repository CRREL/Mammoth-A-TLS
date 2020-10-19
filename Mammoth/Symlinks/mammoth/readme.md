To make symlinks work from mammoth user account:
1. Edit ~/.bashrc file
  - nano ~/.bashrc
  - Add the following to the bottom of the file:
    # >>> Mammoth A-TLS initialize >>>
    export PATH=$PATH:~/Mammoth/Symlinks/mammoth
    # <<< Mammoth A-TLS initialize <<<
2. cd /home/mammoth/Mammoth/Symlinks/mammoth
3. ./create_symlinks
4. exit and restart terminal, to add symlinks to pathing.

To add sudo permissions to these files, modify the sudoers.tmp file by:
1. sudo su -l root
2. sudo visudo
3. Change: Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/s
 - TO: Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/s:/home/mammoth/Mammoth/Symlinks/mammoth
