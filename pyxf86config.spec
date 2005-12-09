%define pyver %(python -c 'import sys ; print sys.version[:3]')

Summary: Python wrappers for libxf86config
Name: pyxf86config
Version: 0.3.22
Release: 1.1
URL: http://www.redhat.com/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Requires: glib2
Requires: python-abi = %{pyver}
BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: python-devel
ExcludeArch: s390 s390x ppc64

%description
Python wrappers for the X server config file library libxf86config.
It is used to read and write X server configuration files.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --x-libraries=/usr/X11R6/%{_lib} --with-python-version=%{pyver}
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS COPYING ChangeLog
%{_libdir}/python?.?/site-packages/ixf86configmodule.so
%{_libdir}/python?.?/site-packages/xf86config.py*


%changelog
* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Nov 13 2005 Jeremy Katz <katzj@redhat.com> - 0.3.20-1
- the X server compiles in the path for rgb.txt, so don't explicitly list 
  (fixes for the path move with modular X)
- get rid of no longer needed %%preun
- modular X buildrequires changes

* Fri Jul 15 2005 Paul Nasrat <pnasrat@redhat.com> - 0.3.19-6
- ExcludeArch ppc64 again

* Fri Jul 15 2005 Paul Nasrat <pnasrat@redhat.com> - 0.3.19-5
- Drop ppc64 ExcludeArch
- pyc and pyo includes

* Tue Mar 29 2005 Warren Togami <wtogami@redhat.com> - 0.3.19-4
- #138263 broken preun #142419 auto pyver

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 0.3.19-2
- rebuild for python 2.4
- make the python requires be on the python-abi

* Wed Aug 11 2004 Jeremy Katz <katzj@redhat.com> - 0.3.19-1
- Change keyboard driver to kbd

* Thu Apr 15 2004 Mike A. Harris <mharris@redhat.com> - 0.3.18-1
- Do not write out XkbRules line to config file, as it is unnecessary hard
  coding the rules file, which has a built in default which should always
  work. (#120858)

* Thu Apr 15 2004 Jeremy Katz <katzj@redhat.com> - 0.3.17-1
- xorg for XkbRules

* Wed Apr 14 2004 Alex Larsson <alexl@redhat.com> 0.3.16
- Rebuild for the new libxf86config
- remove references to XFree86

* Thu Feb 19 2004 Brent Fox <bfox@redhat.com> 0.3.15-1
- remove the setupMice() function createTemplate() 
- because the 2.6 kernel puts both PS/2 and USB mice on the same device

* Mon Feb  9 2004 Alexander Larsson <alexl@redhat.com> 0.3.14-1
- fix range array bug

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
