# Logs Scripts

## logs_split

1. Copies the mail files generated via cronjobs and then clears the original.
2. This splits mail log files by months.
3. Root user mail logs are copied to /home/mammoth/mammoth/logs/root/
4. Mammoth user mail logs are copied to /home/mammoth/mammoth/logs/mammoth/
5. The copied file has the YYYY_MM prefix appended to its name.

 **** NOTE:
    The root mail file requires sudo permissions or a root user to access.
