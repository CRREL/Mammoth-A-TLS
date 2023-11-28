# General Purpose Input/Output (GPIO) Scripts

## scanner_poweroff

1. restores write to file variable files, if a user deleted them.
2. Uses scanner_shutdown to shut the scanner down through a telnet session.
3. Sets the GPIO pin to "off," using gpo_script to control the arduino mounted relays.

## scanner_poweron

1. restores write to file variable files, if a user deleted them.
2. Sets the GPIO pin to "on," using gpo_script to control the arduino mounted relays.
3. Makes you wait 5 minutes before you can talk to scanner to ensure it has come online.

## scanner_shutdown

1. Spawns a telnet session with the RIEGL VZ400i.
2. Asks the scanner to provide us with any available error information.
3. Issues a software shutdown command to the scanner.
4. Waits 1 minute before allowing further actions.

## scanner_status

1. Executes a read command of the GPIO pin connected to the Power Relay.
2. Reports the state of the GPIO pin in question.

## livox_poweroff

1. to be filled out.

## livox_poweron

1. to be filled out.

## livox_status

1. to be filled out.
