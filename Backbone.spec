%define cvs	20031026
Summary:	GNUstep backbone apps, including Preferences
Name:		Backbone
Version:	1.2.99
Release:	0.%{cvs}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-cvs-%{cvs}.tar.gz
# Source0-md5:	f94861488dd0c8a589af9186c97704b3
Patch0:	%{name}-instpath.patch
URL:		http://www.nongnu.org/backbone/
BuildRequires:	gnustep-gui-devel
Obsoletes: Preferences
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
GNUstep Backbone applications, including Preferences

%package devel
Summary:	Header files for Backbone frameforks
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gnustep-gui-devel
Obsoletes: Preferences-devel

%description devel
Header files for Backbone frameworks.

%prep
%setup -q -n System
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_prefix}/System/Applications/*.app
%dir %{_prefix}/System/Applications/*.app/Resources
%{_prefix}/System/Applications/*.app/Resources/*.desktop
%{_prefix}/System/Applications/*.app/Resources/*.plist
%{_prefix}/System/Applications/*.app/Resources/*.tiff
%{_prefix}/System/Applications/*.app/Resources/English.lproj
%dir %{_prefix}/System/Applications/*.app/%{gscpu}
%dir %{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Preferences.app/Preferences
%attr(755,root,root) %{_prefix}/System/Applications/Preferences.app/%{gscpu}/%{gsos}/%{libcombo}/Preferences
%{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/*

%dir %{_prefix}/System/Library/Frameworks/*.framework
%{_prefix}/System/Library/Frameworks/*.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/*
%{_prefix}/System/Library/Frameworks/*.framework/Versions/*/Resources
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/*.framework/Versions/*/%{gscpu}
%{_prefix}/System/Library/Frameworks/*.framework/Versions/Current

%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%dir %{_prefix}/System/Library/Preferences
%dir %{_prefix}/System/Library/Preferences/*.prefs
%{_prefix}/System/Library/Preferences/*.prefs/Resources
%attr(755,root,root) %{_prefix}/System/Library/Preferences/*.prefs/%{gscpu}
 
%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Frameworks/*.framework/Headers
%{_prefix}/System/Library/Frameworks/*.framework/Versions/1.1.0/Headers
%{_prefix}/System/Library/Headers/%{libcombo}/*

%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
