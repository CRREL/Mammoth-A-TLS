These are archived logs for the /var/mail/root and /var/mail/mammoth system logs.  They are generated
on the first day of each month to reduce the size of individual log files and make it easier to
navigate to specific dates/times within the system logs.

These system logs are generated after each automated script is performed via the crontab and
are located in the /Mammoth/Logs directory from the mammoth account or the /home/mammoth/Mammoth/Logs
directory from the root user account.

If you wish to extract an up to date log for the current month, please follow these steps:

        OPTION 1 (Not Recommended):
                sudo su -l root         # log in as super user to the root directory
                # copy root/mammoth mail files to the new directory
                # this will empty the file contents in the /var/mail directory
                /home/mammoth/Mammoth/Scripts/Logs/logs_split

        OPTION 2 (Recommended if you must extract file):
                sudo su -l root         # log in as super user to the root directory
                # copy without overwriting original /var/mail/ files.
                cp /var/mail/root /home/mammoth/Mammoth/Logs/YYYY_MM_root.log
                cp /var/mail/mammoth /home/mammoth/Mammoth/Logs/YYYY_MM_mammoth.log
                # keep in mind /var/mail/ files will be overwritten as normal in crontab.

        OPTION 3 (Recommended if you do not need to extract files):
                sudo su -l root         # log in as super user to the root directory
                nano /var/mail/root     # view current logs without copying
                nano /var/mail/mammoth
