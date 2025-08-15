#!/usr/bin/env bash
set -e

# نصب ابزارها لازم
apt-get update && apt-get install -y build-essential wget tar

# دانلود و نصب کتابخانه C-ta-lib
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xvzf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
make install
cd ..
