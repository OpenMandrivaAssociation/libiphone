# Tarfile created using git
# git clone http://git.matt.colyer.name/2008/libiphone/
# git-archive --format=tar --prefix=libiphone-0.1.0/ %{git_version} | bzip2 > libiphone-0.1.0-20081201.tar.bz2

%define gitdate 20090103
%define git_version 5cde554
%define tarfile %{name}-%{version}-%{gitdate}.tar.bz2
%define snapshot %{gitdate}git%{git_version}

Name:           libiphone
Version:        0.1.0
Release:        %{snapshot}.%mkrel 1
Summary:        Library for connecting to Apple iPhone and iPod touch

Group:          System/Libraries
License:        LGPLv2+
URL:            http://matt.colyer.name/projects/iphone-linux/

Source0:        %{tarfile}
Patch0:         libiphone-fixgnutlsver.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libxml2-devel
BuildRequires: libusb-devel
BuildRequires: libtasn1-devel
BuildRequires: glib2-devel
BuildRequires: gnutls-devel

# Require these until a formal release
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf

%description
libiphone is a library for connecting to Apple's iPhone or iPod touch devices

%package devel
Summary: Development package for libiphone
Group: System/Libraries
Requires: libiphone = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with libiphone.

%prep
%setup -q
%patch0 -p0 -b .fixgnutlsver

%build
./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libiphone.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER README
%{_bindir}/libiphone-initconf
%{_libdir}/libiphone.so.0
%{_libdir}/libiphone.so.0.0.0
%{_datadir}/hal/fdi/information/20thirdparty/31-apple-mobile-device.fdi

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libiphone-1.0.pc
%{_libdir}/libiphone.so
%{_includedir}/libiphone
