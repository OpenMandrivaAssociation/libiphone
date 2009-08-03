# Tarfile created using git
# git clone http://git.matt.colyer.name/2008/libiphone/
# git-archive --format=tar --prefix=libiphone-0.1.0/ %{git_version} | bzip2 > libiphone-0.1.0-20081201.tar.bz2

%define gitdate 20090103
%define git_version 5cde554
%define tarfile %{name}-%{version}-%{gitdate}.tar.bz2
%define snapshot %{gitdate}git%{git_version}

%define major 0
%define libname %mklibname iphone %major
%define develname %mklibname -d iphone

Name:           libiphone
Version:        0.1.0
Release:        %{snapshot}.%mkrel 2
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
BuildRequires: gnutls-devel <= 2.7.0

# Require these until a formal release
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf

%description
libiphone is a library for connecting to Apple's iPhone or iPod touch devices

%package -n %libname
Group: System/Libraries
Summary: Library for connecting to Apple iPhone and iPod touch
Requires: %name >= %version-%release

%description -n %libname
libiphone is a library for connecting to Apple's iPhone or iPod touch devices

%package -n %develname
Summary: Development package for libiphone
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %develname
Files for development with libiphone.

%prep
%setup -q
%patch0 -p0 -b .fixgnutlsver
./autogen.sh

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README
%{_bindir}/libiphone-initconf
%{_datadir}/hal/fdi/information/20thirdparty/31-apple-mobile-device.fdi

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libiphone.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libiphone-1.0.pc
%{_libdir}/libiphone.so
%{_includedir}/libiphone
