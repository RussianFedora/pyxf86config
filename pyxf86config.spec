Summary: Python wrappers for libxf86config
Name: pyxf86config
Version: 0.3.1
Release: 2
URL: http://www.redhat.com/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Requires: glib2
Requires: python2
BuildRequires: glib2
BuildRequires: XFree86-devel
BuildRequires: python2
ExcludeArch: alpha

%description
Python wrappers for the XFree86 library libxf86config.
It is used to read and write XFree86 configuration files.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -d %{_libdir}/python2.2/site-packages/xf86config.pyc ] ; then
  rm -f {_libdir}/python2.2/site-packages/xf86config.pyc
fi

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS COPYING ChangeLog
%{_libdir}/python2.2/site-packages/ixf86configmodule.so
%{_libdir}/python2.2/site-packages/xf86config.py

%changelog
* Mon Jul  8 2002 Alexander Larsson <alexl@redhat.com>
- Bump to 0.3.1

* Mon Jun 17 2002 Alexander Larsson <alexl@redhat.com>
- Bump to 0.3.0

* Fri May 24 2002 Alex Larsson <alexl@redhat.com> 0.2.0-3
- Excludearch alpha for now

* Fri May 24 2002 Alex Larsson <alexl@redhat.com> 0.2.0-2
- Add some doc files

* Fri May 24 2002 Alex Larsson <alexl@redhat.com> 0.2.0-1
- Update version number for new release

* Thu Apr 11 2002 Alex Larsson <alexl@redhat.com> 0.1.0-1
- Initial release

* Wed Apr 10 2002 Alex Larsson <alexl@redhat.com>
- Initial specfile
