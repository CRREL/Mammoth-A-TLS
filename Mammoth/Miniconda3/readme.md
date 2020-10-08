1. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. bash Miniconda3-latest-Linux-x86_64.sh
  - Follow Prompts
  - when asked provide /home/mammoth/Mammoth/Miniconda3 as the install directory.
3. rm Miniconda3-latest_Linux-x86_64.sh
4. close and reopen terminal window.
5. conda update conda
6. conda create --name pdal
  - Follow prompts
7. conda install --name pdal -c conda-forge pdal python-pdal gdal  
8. conda install boto3
9. conda config --add channels s3://conda.rsgiscx.net
10. conda install --name pdal readers_rxp readers_rdb
11. conda install --name pdal -c conda-forge jq
12. conda install --name pdal fgt cpd

**Note: when using 'pdal --drivers|grep rxp' command in the pdal environment we
just created.  You will find tiledb is not loading.  For the purposes of this
system, tiledb is not necessary so any error reporting triggered by this can be
safely ignored.
