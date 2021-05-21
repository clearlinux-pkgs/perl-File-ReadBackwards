#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-ReadBackwards
Version  : 1.06
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-ReadBackwards-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-ReadBackwards-1.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-readbackwards-perl/libfile-readbackwards-perl_1.05-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-ReadBackwards-license = %{version}-%{release}
Requires: perl-File-ReadBackwards-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
File::ReadBackwards.pm
This module reads a file backwards line by line. It is simple to use,
memory efficient and fast. It supports both an object and a tied handle
interface.

%package dev
Summary: dev components for the perl-File-ReadBackwards package.
Group: Development
Provides: perl-File-ReadBackwards-devel = %{version}-%{release}
Requires: perl-File-ReadBackwards = %{version}-%{release}

%description dev
dev components for the perl-File-ReadBackwards package.


%package license
Summary: license components for the perl-File-ReadBackwards package.
Group: Default

%description license
license components for the perl-File-ReadBackwards package.


%package perl
Summary: perl components for the perl-File-ReadBackwards package.
Group: Default
Requires: perl-File-ReadBackwards = %{version}-%{release}

%description perl
perl components for the perl-File-ReadBackwards package.


%prep
%setup -q -n File-ReadBackwards-1.06
cd %{_builddir}
tar xf %{_sourcedir}/libfile-readbackwards-perl_1.05-2.debian.tar.xz
cd %{_builddir}/File-ReadBackwards-1.06
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-ReadBackwards-1.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-ReadBackwards
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-ReadBackwards/716ad9c812ed35d758cc7533266471a047f51423
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::ReadBackwards.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-ReadBackwards/716ad9c812ed35d758cc7533266471a047f51423

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/File/ReadBackwards.pm
