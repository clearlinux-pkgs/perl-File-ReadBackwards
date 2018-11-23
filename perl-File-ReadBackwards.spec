#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-ReadBackwards
Version  : 1.05
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/U/UR/URI/File-ReadBackwards-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/U/UR/URI/File-ReadBackwards-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-readbackwards-perl/libfile-readbackwards-perl_1.05-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-ReadBackwards-license = %{version}-%{release}
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

%description dev
dev components for the perl-File-ReadBackwards package.


%package license
Summary: license components for the perl-File-ReadBackwards package.
Group: Default

%description license
license components for the perl-File-ReadBackwards package.


%prep
%setup -q -n File-ReadBackwards-1.05
cd ..
%setup -q -T -D -n File-ReadBackwards-1.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-ReadBackwards-1.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-ReadBackwards
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-ReadBackwards/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.0/File/ReadBackwards.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::ReadBackwards.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-ReadBackwards/deblicense_copyright
