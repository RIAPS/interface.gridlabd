Installation Instructions
===========================

The steps below serve as a guide for installing the necessary packages to run the GridLAB-D interface. It assumes that the latest version of RIAPS is already installed. 
For instructions on how to install RIAPS please refer to https://riaps.isis.vanderbilt.edu/rdownloads.html.

The instructions below have been tested on a Ubuntu 18.04 installation. 

FNCS Installation
------------------
   
```
# download FNCS from the develop branch
git clone -b develop https://github.com/FNCS/fncs.git

# change to downloaded directory
cd FNCS

# build and install
./configure
make
sudo make install
```

GridLAB-D Instalation
----------------------
For fncs integration a specific branch of GridLAB-D needs to be instaled.

```
# download gridlabd fncs specific branch
git clone -b feature/1146 https://github.com/gridlab-d/gridlab-d.git

# change to downloaded directory
cd gridlab-d
autoreconf -isf

# install third party package Xerces C++
cd third_party
tar -xvzf xerces-c-3.2.0.tar.gz
cd xerces-c-3.2.0
./configure 'CXXFLAGS=-w' 'CFLAGS=-w'
make
sudo make install
cd ../..

# configure, build and install
./configure --with-fncs=/usr/local/ --enable-silent-rules 'CFLAGS=-w' 'CXXFLAGS=-w -std=c++14' 'LDFLAGS=-w'
make
sudo make install
```
Install tesp_support package
-----------------------------

`pip3 install tesp_support --upgrade`

Install InfluxDB
------------------

- Follow the instructions in the InfluxDB web page to download and install [InfluxDB](https://docs.influxdata.com/influxdb/v0.12/introduction/installation/).

- Install influxdb-python by following the instructions given in the [repository](https://github.com/influxdata/influxdb-python).



