#!/bin/sh
mkdir -p /tmp/yum-install
echo -n "yum install " > /tmp/yum-install/install_all.$$
yum list installed |grep -v "^ "|sed -e 's/ .*//' | grep "\."| sed -e 's/\..*//' | tr  '\n' ' ' >> /tmp/yum-install/install_all.$$
mv /tmp/yum-install/install_all.$$ /tmp/yum-install/install_all
