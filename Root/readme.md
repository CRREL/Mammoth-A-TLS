Root user accout Files/Folder
- These binary executable files are accessed via the root user account.
- These files should be copied to the root account /usr/bin/ directory
- The root directory files cannot be executed via the mammoth user account.
- For now, all files executed by the root user account are seperated from the
    files executed by the mammoth user account.

User made tools (root user) : /usr/bin/ via sudo su -l root  
1. logs_split              # used to archive logs from previous month  
2. scanner_poweron         # just powers GPIO pin  
3. scanner_poweroff        # calls scanner_shutdown and removes power from GPIO pin  
4. scanner_shutdown        # spawns a telnet session, reports errors if any, shutdown, waits 1 minute.
