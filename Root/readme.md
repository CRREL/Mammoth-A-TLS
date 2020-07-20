The root user files/scripts necessary to perform automated terrestrial lidar scanning.

interfaces:
  - describes the hardware network properties for eno1 (LAN6)
  - On startup, starts the eno1 interface so comms can be established with scanner.

  User made tools (root user) : /usr/bin/ via sudo su -l root  
  1. logs_split:  used to archive logs from previous month  
  2. scanner_poweron:  just powers GPIO pin  
  3. scanner_poweroff:  calls scanner_shutdown and removes power from GPIO pin  
  4. scanner_shutdown:  spawns a telnet session, reports errors, shuts down, waits 1 minute.
