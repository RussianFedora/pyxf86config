Summary: Python wrappers for libxf86config
Name: pyxf86config
Version: 0.3.13
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
BuildRequires: python-devel
ExcludeArch: s390 s390x ppc64

%description
Python wrappers for the XFree86 library libxf86config.
It is used to read and write XFree86 configuration files.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --x-libraries=/usr/X11R6/%{_lib} --with-python-version=2.3
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
%{_libdir}/python?.?/site-packages/ixf86configmodule.so
%{_libdir}/python?.?/site-packages/xf86config.py

%changelog
* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 0.3.13-2
- rebuild for python 2.3
- don't build on ppc64 either since X is missing bits there as well

* Tue Jul 29 2003 Elliot Lee <sopwith@redhat.com> 0.3.13-1
- Rebuild

* Wed Jun  4 2003 Brent Fox <bfox@redhat.com> 0.3.12-1
- add a 'scrnum' attribute to the adjacency section

* Tue Jun  3 2003 Brent Fox <bfox@redhat.com> 0.3.11-1
- add a function to xf86config.py called getAllScreens()

* Tue Jun  3 2003 Brent Fox <bfox@redhat.com> 0.3.10-1
- add a BuildRequires for python-devel
- add an options attribute to the server layout section (for Xinerama)

* Tue Apr 29 2003 Alexander Larsson <alexl@redhat.com> 0.3.6-1
- Added laptop resolutions

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
