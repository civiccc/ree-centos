Summary: Ruby Enterprise Edition
Name: ruby-enterprise
Version: 1.8.7
Release: 2010.01
License: GPL
Group: Applications/System
Source: ruby-enterprise-%{version}-%{release}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)

Patch0: net_http_socket_close.patch

%description
Ruby Enterprise Edition is a copy-on-right friendly version of ruby that also
includes several performance patches.

%prep
%setup -q -n ruby-enterprise-%{version}-%{release}/source

%patch0 -p0

%build
./configure --prefix=/opt/ruby

%install
make
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
/opt/ruby

%changelog
* Thu May 06 2010 Brad Fults <brad at causes dot com>
- Update for use with 1.8.7

* Fri Dec 13 2008 Tim C. Harper <tim.harper@leadmediapartners.com>
- first build of REE package
