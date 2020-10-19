To make symlinks work from root user account, via sudo su -l root:
1. Edit ~/.bashrc file
  - nano ~/.bashrc
  - Add the following to the bottom of the file:
    # >>> Mammoth A-TLS initialize >>>
    export PATH=$PATH:~/home/mammoth/Mammoth/Symlinks/root
    # <<< Mammoth A-TLS initialize <<<
2. cd /home/mammoth/Mammoth/Symlinks/root
3. ./create_symlinks
4. exit and restart terminal, to add symlinks to pathing.
