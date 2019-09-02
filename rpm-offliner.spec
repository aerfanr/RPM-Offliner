# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/

Name:           rpm-archiver
Version:        1
Release:        0
Summary:        A tool for making offline rpm archives

Group:          PackageManagment
BuildArch:      noarch
License:        GPL
URL:            https://gitlab.com/aerfanr/rpm-offliner
Source0:        rpm-offliner-1.0.tar.gz

%description
A simple tool for making offline rpm archives and install them on fedora systems without internet access.

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/rpm-offliner
install -m 0755 installer.sh $RPM_BUILD_ROOT/etc/rpm-offliner/installer.sh
install -m 0755 rpm-offliner $RPM_BUILD_ROOT/etc/rpm-offliner/rpm-offliner.sh

%files
/etc/rpm-offliner
/etc/rpm-offliner/installer.sh
/etc/rpm-offliner/rpm-offliner.sh
