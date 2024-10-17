%define prj Kolab_Storage

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          kolab-storage
Version:       0.4.0
Release:       %mkrel 1
Summary:       A package for handling Kolab data stored on an IMAP server
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
PreReq:        %{_bindir}/pear
Requires:      php-pear
Requires:      php-pear-Net_IMAP
Requires:      php-pear-Mail_mimeDecode
Requires:      php-pear-HTTP_Request
Requires:      horde-framework
Requires:      horde-cache
Requires:      horde-group
Requires:      horde-history
Requires:      horde-ldap
Requires:      horde-perms
Requires:      horde-sessionobjects
Requires:      horde-mime
Requires:      horde-nls
Requires:      horde-notification
Requires:      horde-util
Requires:      kolab-server
Requires:      kolab-format
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:     %{_tmppath}/%{name}-%{version}

%description
Storing user data in an IMAP account belonging to the user is one
of the Kolab server core concepts. This package provides all the
necessary means to deal with this type of data storage effectively.

%prep
%setup -q -n %{prj}-%{version}
%__cp %{SOURCE0} %{prj}-%{version}.tgz

%build

%install
pear install --packagingroot %{buildroot} --nodeps --offline %{prj}-%{version}.tgz

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp %{_builddir}/package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Kolab
%dir %{peardir}/Horde/Kolab/Storage
%dir %{peardir}/Horde/Kolab/Test
%{peardir}/Horde/Kolab/Deprecated.php
%{peardir}/Horde/Kolab/Storage.php
%{peardir}/Horde/Kolab/Storage/Cache.php
%{peardir}/Horde/Kolab/Storage/Data.php
%{peardir}/Horde/Kolab/Storage/Folder.php
%{peardir}/Horde/Kolab/Storage/List.php
%{peardir}/Horde/Kolab/Storage/Perms.php
%{peardir}/Horde/Kolab/Test/Storage.php
%dir %{peardir}/docs
%dir %{peardir}/docs/Kolab_Storage
%dir %{peardir}/docs/Kolab_Storage/Horde
%dir %{peardir}/docs/Kolab_Storage/Horde/Kolab
%dir %{peardir}/docs/Kolab_Storage/Horde/Kolab/Storage
%{peardir}/docs/Kolab_Storage/Horde/Kolab/Storage/list.php
%{peardir}/docs/Kolab_Storage/Horde/Kolab/Storage/usage.txt
%dir %{peardir}/tests
%dir %{peardir}/tests/Kolab_Storage
%dir %{peardir}/tests/Kolab_Storage/Horde
%dir %{peardir}/tests/Kolab_Storage/Horde/Kolab
%dir %{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage
%{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage/AllTests.php
%{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage/CacheTest.php
%{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage/DataTest.php
%{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage/FolderTest.php
%{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage/ListTest.php
%{peardir}/tests/Kolab_Storage/Horde/Kolab/Storage/PermsTest.php

