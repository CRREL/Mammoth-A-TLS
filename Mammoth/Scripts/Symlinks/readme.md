Executing the create_symlinks script, with the modified .bashrc file in place,
will create symbolic links to scripts we wish to regularly use from anywhere.

1. Edit ~/.bashrc file
  - nano ~/.bashrc
  - Add the following to the bottom of the file:
    # >>> Mammoth A-TLS initialize >>>
    export PATH=$PATH:~/Mammoth/Scripts/Symlinks
    # <<< Mammoth A-TLS initialize <<<
2. cd /home/mammoth/Mammoth/Scripts/Symlinks
3. ./create_symlinks
4. exit and restart terminal, to add symlinks to pathing.
