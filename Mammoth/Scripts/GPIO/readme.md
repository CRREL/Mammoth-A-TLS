General Purpose Input/Output (GPIO) Scripts

scanner_poweroff:
 - restores write to file variable files, if a user deleted them.
 - Uses scanner_shutdown to shut the scanner down through a telnet session.
 - Sets the GPIO pin to "off," using demo_gpio in the fintek demo code.

scanner_poweron:
 - restores write to file variable files, if a user deleted them.
 - Sets the GPIO pin to "on," using demo_gpio in the fintek demo code.
 - Makes you wait 4 minutes before you can talk to scanner to ensure it has come online.

scanner_shutdown:
 - Spawns a telnet session with the RIEGL VZ400i.
 - Asks the scanner to provide us with any available error information.
 - Issues a software shutdown command to the scanner.
 - Waits 1 minute before allowing further actions.

The GPIO of the linux box is connected to a power relay and acts as a switch to
provide power to the scanner from an external source.

**** NOTE:  
  Fintek GPIO tools use root/sys/class files to operate and thus these scripts
  are to be executed with sudo permissions or via the root crontab
