These are archived logs for the /var/mail/root and /var/mail/mammoth system logs.  They are generated
on the first day of each month to reduce the size of individual log files and make it easier to
navigate to specific dates/times within the system logs.

These system logs are generated after each automated script is performed via the crontab and
are located in the /Mammoth/Logs directory from the mammoth account or the /home/mammoth/Mammoth/Logs
directory from the root user account.

If you wish to extract an up to date log for the current month, please follow these steps:

        OPTION 1:
                sudo su -l root         # log in as super user to the root directory
                logs_split script       # copy root/mammoth mail files to the new directory
                                        # this will empty the file contents in the /var/mail directory

        OPTION 2:
                sudo su -l root         # log in as super user to the root directory
                # copy without overwriting original /var/mail/ files.
                cp /var/mail/root /home/mammoth/Mammoth/logs/YYYY_MM_root.log
                cp /var/mail/mammoth /home/mammoth/Mammoth/logs/YYYY_MM_mammoth.log
                # keep in mind /var/mail/ files will be overwritten as normal in chrontab.

        OPTION 3:
                sudo su -l root         # log in as super user to the root directory
                nano /var/mail/root     # view current logs without copying
                nano /var/mail/mammoth
