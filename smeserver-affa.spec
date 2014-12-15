Summary: A rsync-based backup program for linux, adapted to sme server 8
%define name smeserver-affa
Name: %{name}
%define version 3.2.2.2
%define release 0
Version: %{version}
Release: %{release}%{?dist}
Vendor: Michael Weinberger <mweinber AT users DOT sourceforge DOT net> //// adaptation to sme-server Arnaud Guillaume <smeserver-affa AT guedel DOT eu>
License: GNU General Public License
Group: Applications/Archiving
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
AutoReq: no
Requires: openssh-clients
Requires: perl-Config-IniFiles
Requires: perl-Filesys-DiskFree
Requires: perl-MailTools
Requires: perl-Proc-ProcessTable
Requires: perl-TimeDate 
Requires: rsync

%description
Affa is a rsync-based backup program
Documentation: http://affa.sf.net
with SMEServer + RPMCheck + Watchdog + rise

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
rm -f %{name}-%{version}-filelist
(cd root   ;find . -depth -print | cpio -dump $RPM_BUILD_ROOT)


# Set version String
cp -a $RPM_BUILD_ROOT/sbin/affa $RPM_BUILD_ROOT/sbin/affa.tmp
VERSIONSTRING=%{version}-`echo %{release}|sed -e 's/\..*$//'`
sed -e "s/my \$VERSION.*;/my \$VERSION='$VERSIONSTRING';/" < $RPM_BUILD_ROOT/sbin/affa.tmp > $RPM_BUILD_ROOT/sbin/affa
rm -f $RPM_BUILD_ROOT/sbin/affa.tmp

rm -f %{name}-%{version}-filelist

find $RPM_BUILD_ROOT -depth -type f -print |\
 sed -e "s@^$RPM_BUILD_ROOT@@g" \
 -e "s@^/sbin/@%attr(0750,root,root) &@"\
 -e "s@^/etc/profile.d/@%attr(0555,root,root) &@"\
 -e "s@^/etc/sudoers.d/@%attr(0440,root,root) &@"\
 -e "s@^/etc/cron.d/@%attr(0444,root,root)%config(noreplace) &@"\
 -e "s@^/usr/lib/affa/LICENSE@%attr(0444,root,root) &@"\
 -e "s@^/usr/lib/affa/WARRANTY@%attr(0444,root,root) &@"\
 -e "s@^/usr/man/man1/@%attr(0444,root,root) &@"\
 -e "s@^/etc/affa/scripts/@%attr(0750,root,root)%config(noreplace) &@"\
 -e "s@^/etc/affa/@%attr(0640,root,root)%config(noreplace) &@"\
 >> %{name}-%{version}-filelist


find $RPM_BUILD_ROOT -depth -type d -print |\
 sed -e "s@^$RPM_BUILD_ROOT@%dir @g" >> %{name}-%{version}-filelist

find $RPM_BUILD_ROOT -depth -type l -print |\
 sed "s@^$RPM_BUILD_ROOT@@g" >> %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre
exit 0

%post
exit 0

%preun
exit 0

%postun
exit 0

%changelog
* Sun Dec 07 2014 Arnaud Guillaume 3.2.2.2
- integration of the patch of Mats Schuh in order to enable check for external disk label before unmount
* Sat Aug 23 2014 Arnaud Guillaume 3.2.2.1
- adapted to the new release of rsync (bug by calculating the number and the size of the transfered files)
* Sat Apr 05 2014 Arnaud Guillaume 3.2.2.0
- first adaptation for sme server8
* Sun Mar 04 2012 Michael Weinberger 3.2.2
- Improved NRPE and sudoers config
- Fixed bug in DiskUsageRaw()
- Added NRPE command affa_diskusagenrpe
* Fri Mar 02 2012 Michael Weinberger 3.2.1
- Bugfix: command_prefix definiton was not added to /etc/nagios/affa-nrpe.cfg
* Thu Mar 01 2012 Michael Weinberger 3.2.0
- Bugfix: remoteRsyncBinary and localRsyncBinary was not used
* Sun Feb 26 2012 Michael Weinberger 3.1.7
- Bugfixes in showSchedule()
* Sun Feb 26 2012 Michael Weinberger 3.1.6
- added ICINGA/Nagios auto-configuration
* Fri Feb 24 2012 Michael Weinberger 3.1.4
- do not show Dedup interrupted in --status after the very first run
- improved --nrpe function
- added script yum_install_packages.sh
* Tue Oct 11 2011 Michael Weinberger 3.1.3
- MINOR IMPROVEMENTS
  --send-key: mkdir of RemoteAuthorizedKeysFile. Avoid errors if dir does not exist
  --log-tail: show last rotated if current log is empty or too short
  --check-conncetions: allow jobs as arguments 
* Sun Aug 29 2011 Michael Weinberger 3.1.2
- Bugfix: postJobCommand and postJobCommandRemote were not executed
* Sat Aug 13 2011 Michael Weinberger 3.1.1
- process state 'rsync interrupted' and 'dedup interrupted'
- --resume-interrupted
- resume interrupted jobs after server boot
* Sun Aug 07 2011 Michael Weinberger 3.1.0-1
- introduced status 'interrupted'(with --status)
* Fri Aug 05 2011 Michael Weinberger 3.1.0-0
- Release of 3.1.0
* Thu Aug 04 2011 Michael Weinberger 3.0.2-14
- de-duplicate, execPreJobCommand and execPostJobCommand only on scheduled run
- removed Command arg from sample scripts
- Fixed: Concatenated config in /tmp was world readable
- De-duplication info added to --show-schedule
* Tue Aug 02 2011 Michael Weinberger 3.0.2-6
- De-Duplication (freedup)
- De-Dup info in --status and --list-archives
- --status: only show enabled jobs. All with --all
- Fix: property globalStatus was not working
- Running state rsync or de-deduplicating display in --status
- Show de-deduplicating busy in --list-archives for scheduled.0
- new property dedupKill. When set no, --kill does not kill a job when de-duplicating
- new option --show-property

* Wed Jul 27 2011 Michael Weinberger 3.0.1-7
- Bug fixes: RemoteUser was not always used in ssh commands

* Sun Jul 24 2011 Michael Weinberger 3.0.1-6
- fixed bug in affa --status
- GlobalAffaConfig was mounted as Samba share
- call setupSamba() only in cronSetup()
- updated man

* Sat Jul 23 2011 Michael Weinberger 3.0.1-5
- new key NRPEtrigger
- full affa path required when starting re-run from cronjob
- improved deletion of shift out archives, --delete-job and --cleanup
- added --single-transaction to /etc/affa/scripts/mysql-dump-tables

* Wed Jul 20 2011 Michael Weinberger 3.0.0-0
- generic linux version made from Affa 2.0 (SME Version)

* Mon Apr 02 2007 Michael Weinberger
- bash version re-written in Perl

