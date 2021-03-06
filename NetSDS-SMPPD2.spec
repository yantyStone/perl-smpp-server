# This is spec file for common NetSDS frameworks

%define module NetSDS-SMPPD2
%define m_distro NetSDS-SMPPD2
%define m_name NetSDS::SMPPD2
%define _enable_test 1
%def_without test

Name: NetSDS-SMPPD2
Version: 2.101
Release: alt8

Summary: NetSDS-SMPPD2 - is an 

License: GPL

Group: Networking/Other
Url: http://www.netstyle.com.ua/

Packager: Dmitriy Kruglikov <dkr@netstyle.com.ua>

BuildArch: noarch
Source0: %module-%version.tar


# Automatically added by buildreq on Mon Mar 08 2010 (-bi)
BuildRequires: perl-NetSDS
BuildRequires: perl-JSON 
BuildRequires: perl-JSON-XS 
BuildRequires: perl-Module-Build
BuildRequires: perl-Net-SMPP
BuildRequires: perl-IPC-ShareLite
BuildRequires: perl-Data-Structure-Util 
BuildRequires: perl-Unix-Syslog
BuildRequires: perl-Data-UUID
BuildRequires: perl-DBI
BuildRequires: perl-DBD-Pg
BuildRequires: perl-DBD-mysql

Requires: NetSDS-common
Requires: perl-NetSDS
Requires: perl-JSON 
Requires: perl-JSON-XS 
Requires: perl-Net-SMPP
Requires: perl-IPC-ShareLite
Requires: perl-Data-Structure-Util 
Requires: perl-Unix-Syslog
Requires: perl-Data-UUID
Requires: perl-DBI
Requires: perl-DBD-Pg
Requires: perl-DBD-mysql


%description
NetSDS-SMPPD2 is an 

%package contrib
Summary: contrib files and scripts for NetSDS SMPP server
Group: Networking/Other
Requires: %name = %version-%release

%description contrib
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/{monitrc.d,NetSDS}
mkdir -p %buildroot%_datadir/NetSDS/smppserver2
install -m 755 smppserver %buildroot%_sbindir/smppserver2
install -m 755 smppserver_safe_start.sh %buildroot%_sbindir/smppserver2_safe_start.sh
install -m 755 smppserver.init %buildroot%_initdir/smppserver2
install -m 755 smppserver.monit %buildroot%_sysconfdir/monitrc.d/smppserver2
install -m 640 smppserver.conf %buildroot%_sysconfdir/NetSDS/smppserver2.conf
cp -r contrib %buildroot%_datadir/NetSDS/smppserver2
cp -r sql %buildroot%_datadir/NetSDS/smppserver2

%post
%post_service smppserver2

%preun
%preun_service smppserver2

%files
%perl_vendor_privlib/NetSDS*
%_sbindir/smppserver2
%_sbindir/smppserver2_safe_start.sh
%_bindir/*
%_datadir/NetSDS/smppserver2/sql
%config(noreplace) %_sysconfdir/NetSDS/smppserver2.conf
%config(noreplace) %_initdir/smppserver2
%config(noreplace) %_sysconfdir/monitrc.d/smppserver2
%doc doc/*

%files contrib
%_datadir/NetSDS/smppserver2/contrib

%changelog
* Thu Oct 27 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt8
- Used NetSDS-common instead /var/run/NetSDS creation.
- Tester smppsvrtst.pl used same DB and auth.

* Wed Oct 26 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt7
- Version Up for last tests.

* Wed Oct 26 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt6
- Fixed smppserver.conf and smppserver.init

* Tue Oct 25 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt5
- Add /var/run/NetSDS creation.

* Tue Oct 25 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt4
- Cleared Requirements 

* Tue Oct 25 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt3
- Added Requres for perl-IPC-ShareLite

* Tue Oct 25 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt3
- Added Requres for perl-Net-SMPP

* Tue Oct 25 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt3
- Files renamed for run v1 and v2 together.

* Mon Oct 24 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt2
- Added Requres for Nibelite-core

* Mon Oct 17 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 2.101-alt1
- Initial build
