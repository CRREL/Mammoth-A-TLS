The root user files/scripts necessary to perform automated terrestrial laser scanning.

interfaces:
  - describes the hardware network properties for eno1 (LAN6)
  - On startup, starts the eno1 interface so comms can be established with scanner.

crontab:
  - Conducts regular job operations such as frame scans at the top of each hour.
  - Conducts extended line scans if the frame scan shows it is snowing.
  - Conducts file compression, conversion, and sycning to the AWS S3 bucket.
