Installing aws-cli tools from a terminal onto the Linux computer.

1. cd ~/mammoth (if user, if root navigate to /home/mammoth/mammoth)
2. curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
3. unzip awscliv2.zip
4. rm awscliv2.zip
5. sudo ./aws/install
6. aws --verify
7. aws configure
  - enter your access key id
  - enter your secret access key
  - enter us-east-1
  - enter none
8. root su -l root
9. aws configure
  - enter your access key id
  - enter your secret access key
  - enter us-east-1
  - enter none
10. sudo apt install parallel
