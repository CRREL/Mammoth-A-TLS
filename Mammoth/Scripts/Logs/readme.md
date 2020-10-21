Logs Scripts

logs_split:
 - Copies the mail files generated via cronjobs and then clears the original.
 - This splits mail log files by months.
 - Root user mail logs are copied to /home/mammoth/Mammoth/Logs/root/
 - Mammoth user mail logs are copied to /home/mammoth/Mammoth/Logs/mammoth/
 - The copied file has the YYYY_MM prefix appended to its name.

 **** NOTE:
    The root mail file requires sudo permissions or a root user to access.
