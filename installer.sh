#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This command has to be run as root"
    exit 1
fi

echo "--- preparing for install"

scriptDir="$(cat "$(dirname "$0")" ; pwd -P)"
pname=$(head -n 1 $scriptDir/offline-meta)
version=$(tail -n 1 $scriptDir/offline-meta)

echo "[offline-$pname]
name=Fedora-$version - $pname
baseurl=file://$scriptDir
enabled=0
gpgcheck=0" > /etc/yum.repos.d/offline-$pname.repo

echo "--- installing packages"

dnf --disablerepo=\* --enablerepo=offline-$pname install $pname

echo "--- done"
