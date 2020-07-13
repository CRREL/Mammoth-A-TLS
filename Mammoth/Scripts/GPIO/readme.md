General Purpose Input/Output (GPIO) Scripts

scanner_poweroff:
  - Initializes the fintek GPIO library if it hasn't been initialized already.
  - Uses scanner_shutdown to shut the scanner down through a telnet session.
  - Sets the GPIO pin to "off."

scanner_poweron:
  - Initializes the fintek GPIO library if it hasn't been initialized already.
  - Sets the GPIO pin to "on."

scanner_shutdown:
  - Spawns a telnet session with the RIEGL VZ400i.
  - Asks the scanner to provide us with any available error information.
  - Issues a software shutdown command to the scanner.
  - Waits 1 minute before allowing further actions.

The GPIO of the linux box is connected to a power relay and acts as a switch to
provide power to the scanner from an external source.

Permissions required from root user in order to function properly:
  1. chmod -R a+rwx /usr/sbin/start_gpio
  2. chmod -R a+rwx /sys/class/gpio
