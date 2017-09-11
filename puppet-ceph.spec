%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-ceph
Version:        2.4.1
Release:        1%{?dist}
Summary:        Community Developed Ceph Module
License:        ASL 2.0

URL:            https://launchpad.net/puppet-ceph

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-apache
Requires:       puppet-concat
Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Community Developed Ceph Module

%prep
%setup -q -n openstack-ceph-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/ceph/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/ceph/



%files
%{_datadir}/openstack-puppet/modules/ceph/


%changelog
* Mon Sep 11 2017 Haikel Guemar <hguemar@fedoraproject.org> 2.4.1-1
- Update to 2.4.1

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 2.4.0-1
- Update to 2.4.0



