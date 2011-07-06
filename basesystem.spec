Summary: The skeleton package which defines a simple Red Hat Enterprise Linux system
Name: basesystem
Version: 10.0
Release: 4%{?dist}
License: Public Domain
Group: System Environment/Base
Requires(Pre): setup filesystem
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Basesystem defines the components of a basic Red Hat Enterprise Linux
system (for example, the package installation order to use during
bootstrapping). Basesystem should be in every installation of a system,
and it should never be removed.

%prep

%build

%install

%clean

%files
%defattr(-,root,root,-)

%changelog
* Fri May 21 2010 Ondrej Vasik <ovasik@redhat.com> - 10.0-4
- remove reference to Fedora, add dist tag
Related: rhbz#566527

* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 10.0-3.2
- Rebuilt for RHEL 6
Related: rhbz#566527

* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 10.0-3.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 20 2008 Phil Knirsch <pknirsch@redhat.com> 10.0-1
- Bump version and rebuild for Fedora 10 (#451289)

* Fri Mar 02 2007 Phil Knirsch <pknirsch@redhat.com> - 8.1-1
- Cleanup per package review (#225608)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 8.0-5.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Sep 22 2004 Bill Nottingham <notting@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Aug 21 2002 Bill Nottingham <notting@redhat.com>
- bump rev

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Bill Nottingham <notting@redhat.com>
- rebuild. Wheee.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- don't require rpm (breaks dependency chain)

* Tue Mar 16 1999 Erik Troan <ewt@redhat.com>
- require rpm

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

