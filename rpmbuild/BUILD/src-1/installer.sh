echo "--- preparing for install"

scriptDir=$(dirname "$0")
pname=$(head -n 1 $scriptDir/offline-meta)
version=$(tail -n 1 $scriptDir/offline-meta)

echo "[offline-$pname]
name=Fedora-$version - $pname
baseurl=file://$scriptDir
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Fedora-$version" > /etc/yum.repos.d/offline-$pname.repo

echo "--- installing packages"

dnf --disablerepo=\* --enablerepo=offline-$pname install $pname

echo "--- done"
