# RPM Offliner
This is a simple tool to download RPM packages, make them offline and create an easy installer for them.

## When should I use this?
If you have an offline computer, e.g. a computer at your school, you can use this tool to download packages, then move them to the offline computer and install them without using the internet.

## How can I use this?
1.  Run `rpm-offliner` command (You have to become root user or use `sudo`).
2.  Write name off the package that you want to download and press enter.
3.  Accept the suggested directory or reject it and write directory address you prefer. (We recommend to create a folder and download all packages you want to that folder because this prevents downloading single dependencies several times.)
4.  Enter fedora version of the target computer.
5.  Wait for the download and other jobs to complete.
6.  Copy tar.xz archive to the target computer.
7.  Extract archive.
8.  Run the following command to make installer executable (You have to open the terminal in the extracted directory):

    `sudo chmod +x installer.sh`

9.  Run this command and wait for the installation to complete (You have to become root user or use `sudo`):
   
    `./installer.sh`

## Where to download and install this script?
To easily download and install this script, you can get it from [my copr repository](https://copr.fedorainfracloud.org/coprs/aerfanr/rpm-offliner/). Or you can download rpm package from release branch.