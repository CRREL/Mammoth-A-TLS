Installing aws-cli tools from a terminal onto the Linux computer.

1. curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
2. unzip awscli-bundle.zip
3. rm awscli-bundle.zip
4. sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
5. aws --verify
6. rm -rf awscli-bundle
7. aws configure
  - enter your access key id
  - enter your secret access key
  - enter us-east-1
  - enter none
