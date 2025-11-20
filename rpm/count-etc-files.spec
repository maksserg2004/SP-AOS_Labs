Name:           count-etc-files
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count files in /etc directory

License:        MIT
URL:            https://github.com/maksserg2004/SP-AOS_Labs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash

%description
A bash script that counts the number of regular files 
(excluding directories and links) in the /etc directory.
This script requires root or sudo privileges to run.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 script.sh %{buildroot}%{_bindir}/count-etc-files

%files
%{_bindir}/count-etc-files

%changelog
* Thu Nov 20 2025 Maksym Sergiyenko <maksymsergiyenko09@gmail.com> - 1.0-1
- Initial package release
