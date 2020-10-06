This is the location of variables used for mammoth scripts

snowing:
  - 0 : It is not snowing.
  - 1 : It is snowing.

scanner_power
  - 0 : Scanner is off
  - 1 : Scanner is on

vars_init:
  - initializes write to file variable, files.
  - executed on power on and power off of scanner to ensure they are restored.

  **** NOTE:
    Read access for the fintek GPIO files is not necessarily available from
    the mammoth user account.  These variables are clones of information used
    elsewhere to help determine whether extended line frames need to be conducted
    and to determine whether the scanner is already on, or needs to be powered on.
