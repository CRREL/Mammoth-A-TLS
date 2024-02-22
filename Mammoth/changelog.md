# System Change Log

## October 2020

- Taken down from Sesame on Oct 10, 2020
- Installed at CUES on Oct 19, 2020
- Reflector survey at CUES on Oct 19/20, 2020
- Fully functional 11/06/2020

## 11/9/2020

- Added 2nd compress and sync script calls into crontab.  Upload size was too
  large to complete before next scans would need to be conducted.  Now compressing
  and syncing to aws s3 bucket at 1:08 a.m./p.m. and 1:38 a.m./p.m., respectively.
- Ran sudo dpkg-reconfigure popularity-contest to get rid of cronjob emails to
  the root user mail account relating to being unable to open /etc/popularity-contest.conf

## 11/19/2020

- Changed first extended line scan to occur 6 minutes after the hour instead of 5.
This is due to a dropped extended line scan due to a spectralon panel scan not being
entirely finished with the scanner.
- Updated uploads to 10 min after the hour, instead of 9, to adjust for extended line
scans occuring 1 minute later at the top of the hour.

## 12/21/2020

- Added a spectralon-gondola line scan into the line scan script.
- bumped the extended line scan from 6 minutes after the hour to 7 minutes after the hour, to accommodate for the additional line scan.

## 02/\*2022

- System removed from Mammoth to use equipment for Fairbanks A-TLS project.

## 11/\*/2022

- System re-tooled and re-installed at Mammoth in a new position.
- Replaced LPC-835X with LPC-915, no longer has GPIO utilities
- Added custom Arduino power switch controlled via python serial commands
- Changed IP range of Riegl Scanner and Riegl Protective Housing to same range with livoxes
- Added support hardware + software for 3 Livox Mid-70 devices
- Added second power switching channel so Riegl and Livoxes can be powered independently
- Added Ethernet switch for Riegl + Livox devices
- Moved Fintek to 2021-2022 Archive as it is no longer utilized
- Updated readme.md files for software library installations
- Likely to rename all files to lowercase to follow internal nomenclature.

## Winter 2022-2023

- SOP not updated for 2022-2023 winter, uses old inaccurate SOP matrix from 2021-2022 season.
- Platform damage occurs at Mammoth causing the scanner to move around as the season progresses.
- Specific date of platform damage unknown.

## Summer/Fall 2023

- Platform repair takes place.
- Scanner is in yet another new position without an updated SOP.

## 11/\*/2023

- Updated SOP to adjust for removal/installation that took place 11/2022 and platform repair later in 2023.
- Updated Spectralon panel line scan and Spectralon gondola panel line scan.
- Detached compress and syncaws processes from scheduler after call, to help resolve sequential operations causing skipped processes.
- Adjusted GitHub respository to reflect the rebuilt A-TLS system, that no longer uses the same hardware/software.
