Summary: Python wrappers for libxf86config
Name: pyxf86config
Version: 0.3.5
Release: 1
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
ExcludeArch: s390 s390x

%description
Python wrappers for the XFree86 library libxf86config.
It is used to read and write XFree86 configuration files.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --x-libraries=/usr/X11R6/%{_lib}
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
* Mon Jan 27 2003 Alexander Larsson <alexl@redhat.com> 0.3.5-1
- Rebuild

* Wed Jan 15 2003 Michael Fulbright <msf@redhat.com> 0.3.4-1
- remove code in xf86config.py:createTemplate() that inserted a Display
  section.  We want user to supply this and it shouldnt be in template.

* Sat Jan 11 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add ExcludeArch: s390 s390x

* Thu Dec 12 2002 Mike A. Harris <mharris@redhat.com> 0.3.3-1
- Remove Excludearch alpha

* Tue Nov 12 2002 Michael Fulbright <msf@redhat.com> 0.3.2-1
- Added some convenience functions.

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
