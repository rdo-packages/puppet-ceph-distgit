%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xbba3b1e67a7303dd1769d34595bf2e4d09004514
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-ceph
Version:        3.1.1
Release:        1%{?dist}
Summary:        Community Developed Ceph Module
License:        ASL 2.0

URL:            https://launchpad.net/puppet-ceph

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Wed Apr 06 2022 RDO <dev@lists.rdoproject.org> 3.1.1-1
- Update to 3.1.1



