%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-ceph
%global commit 896a22275b5a73c45c2f9aca877b1a09bc68b517
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%if 0%{?dlrn}
%define upstream_name openstack-ceph
%else
%define upstream_name puppet-ceph
%endif

Name:           puppet-ceph
Version:        3.0.0
Release:        1%{dist}
Summary:        Community Developed Ceph Module
License:        ASL 2.0

URL:            https://launchpad.net/puppet-ceph

Source0:        https://github.com/openstack/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-apache
Requires:       puppet-concat
Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet-keystone
Requires:       puppet >= 2.7.0

%description
Community Developed Ceph Module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
* Mon Apr 29 2019 RDO <dev@lists.rdoproject.org> 3.0.0-1
- Update to release 3.0.0


