Name:           rpm-offliner
Version:        1.1
Release:        1%{?dist}
Summary:        A tool for making offline rpm archives

Group:          PackageManagment
BuildArch:      noarch
Requires:       tar, dnf, createrepo, bash
License:        GPLv3+
URL:            https://gitlab.com/aerfanr/rpm-offliner
Source0:        rpm-offliner-1.1.tar.gz

%description
A simple tool for making offline rpm archives and install them on fedora systems without internet access.

%prep
%setup -q
%build
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/rpm-offliner
install installer.sh %{buildroot}/%{_sysconfdir}/rpm-offliner/installer.sh
install rpm-offliner %{buildroot}/%{_bindir}/rpm-offliner
chmod 755 %{buildroot}/%{_bindir}/rpm-offliner
echo "boz"

%files
%{_sysconfdir}/rpm-offliner/installer.sh
%{_bindir}/rpm-offliner

%changelog
* Sat Sep 21 2019 Amirerfan Rafati <erfan.rafati@outlook.com> - 1.1-1
- Bug fix, rpm-offliner file changed, rpm-offliner.sh file removed
* Wed Sep 4 2019 Amirerfan Rafati <erfan.rafati@outlook.com> - 1.0-4
- Bug fix, installer.sh file channged
* Wed Sep 4 2019 Amirerfan Rafati <erfan.rafati@outlook.com> - 1.0-3
- Bug fix, rpm-offliner file channged
* Wed Sep 4 2019 Amirerfan Rafati <erfan.rafati@outlook.com> - 1.0-2
- Bug fix, rpm-offliner file channged
* Tue Sep 3 2019 Amirerfan Rafati <erfan.rafati@outlook.com> - 1.0-1
- First package
