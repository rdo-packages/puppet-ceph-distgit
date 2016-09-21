%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-ceph
Version:        2.1.0
Release:        1%{?dist}
Summary:        Community Developed Ceph Module
License:        Apache-2.0

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
%setup -q -n openstack-ceph-%{version}

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
* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.1.0-1
- Update to 2.1.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.0.0-1
- Update to 2.0.0


