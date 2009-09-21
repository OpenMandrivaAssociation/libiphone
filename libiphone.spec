%define name libiphone
%define version 0.9.3
%define major 0
%define libname %mklibname iphone %major
%define libnamedev %mklibname -d iphone

Name:           libiphone
Version:        0.9.3
Release:        %mkrel 2
Summary:        Library for connecting to Apple iPhone and iPod touch

Group:          System/Libraries
License:        LGPLv2+
URL:            http://matt.colyer.name/projects/iphone-linux/

Source0:        http://cloud.github.com/downloads/MattColyer/%{name}/%{name}-%{version}.tar.bz2
Patch0:         libiphone-wformat.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot


BuildRequires: libtasn1-devel
BuildRequires: libplist-devel
BuildRequires: usbmuxd-devel >= 0.1.4
BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: python-devel
BuildRequires: swig

%description
libiphone is a library for connecting to Apple's iPhone or iPod touch devices

%package -n %libname
Group: System/Libraries
Summary: Library for connecting to Apple iPhone and iPod touch
Requires: %name >= %version

%description -n %libname
libiphone is a library for connecting to Apple's iPhone or iPod touch devices

%package -n %libnamedev
Summary: Development package for libiphone
Group: Development/C
Provides: %name-devel = %version-%release
Requires: %libname = %{version}-%{release}

%description -n %libnamedev
Files for development with libiphone.

%package -n python-iphone
Summary: Python bindings for libiphone
Group: Development/Python
%py_requires -d


%description -n python-iphone
Python bindings for libiphone.

%prep
%setup -q
%patch0 -p1 -b .wformat

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER README
%{_datadir}/hal/fdi/information/20thirdparty/31-apple-mobile-device.fdi
%{_bindir}/iphone_id
%{_bindir}/iphoneinfo
%{_bindir}/iphonesyslog

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libiphone-1.0.pc
%{_libdir}/libiphone.so
%{_libdir}/libiphone*a
%{_includedir}/libiphone

%files -n python-iphone
%defattr(-,root,root,-)
%{python_sitearch}/libiphone/
