# Mammoth A-TLS System Log Files

These are archived logs for the /var/mail/root and /var/mail/mammoth system logs.  They are generated
on the first day of each month to reduce the size of individual log files and make it easier to
navigate to specific dates/times within the system logs.

These system logs are generated after each automated script is performed via the crontab and
are located in the /Mammoth/Logs directory from the mammoth account or the /home/mammoth/Mammoth/Logs
directory from the root user account.

If you wish to extract an up to date log for the current month, please follow these steps:

        OPTION 1:
                sudo logs_split         # copies mail logs to archive.
                                        # appends if the file already exists.
                                        # empties active log file after copying.

        OPTION 2:
                sudo su -l root         # log in as super user to the root directory
                cd /var/mail            # view files via nano or vim.

Mammoth user: Log files are located in ~/mammoth/logs/root and ~/mammoth/logs/mammoth.</br>
Root user: Log files are located in ~/../home/mammoth/mammoth/logs/root and ~/../home/mammoth/mammoth/logs/mammoth
