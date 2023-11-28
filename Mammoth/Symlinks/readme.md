# Creating symbolic links and updating environment

## General Information

- executing create_symlinks and updating the .bashrc files allows us to run commands without referencing the path to the script from any pathing.
- e.g. instead of /home/mammoth/mammoth/scripts/aws/syncaws, we can use: syncaws

## To make symlinks work, from mammoth user account

1. Edit ~/.bashrc file:
    - nano ~/.bashrc
    - Add the following to the bottom of the file:</br>
\# >>> Mammoth A-TLS initialize >>></br>
export PATH=$PATH:~/mammoth/symlinks</br>
\# <<< Mammoth A-TLS initialize <<<</br>
2. cd /home/mammoth/mammoth/symlinks
3. ./create_symlinks
4. exit and restart terminal, to add symlinks to pathing.

## To add sudo permissions to these files, modify the sudoers.tmp file

1. sudo su -l root
2. sudo visudo
3. Change:
    - FROM: Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/s"
    - TO: Defaults          secure_path="/home/mammoth/mammoth/symlinks:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/s"
4. At the bottom add:
    - mammoth ALL=NOPASSWD: /sbin/reboot

## To make symlinks work, from root user account

1. sudo su -l root
2. Edit ~/.bashrc file
    - nano ~/.bashrc
    - Add the following to the bottom of the file:</br>
\# >>> Mammoth A-TLS initialize >>></br>
export PATH=$PATH:~/../home/mammoth/mammoth/symlinks</br>
\# <<< Mammoth A-TLS initialize <<<</br>
