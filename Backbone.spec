%define cvs	20041115
Summary:	GNUstep backbone apps, including Preferences
Summary(pl):	Szkieletowe aplikacje GNUstepa, w tym Preferences
Name:		Backbone
Version:	1.2.99
Release:	0.%{cvs}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{cvs}.tar.gz
# Source0-md5:	303ba195aa04613b9792157e8aedaf5a
Patch0:		%{name}-buildinplace.patch
Patch1:		%{name}-installprefix.patch
Patch2:		%{name}-initializeWithArguments.patch
URL:		http://www.nongnu.org/backbone/
BuildRequires:	gnustep-gui-devel
Obsoletes:	Preferences
Obsoletes:	Terminal
Obsoletes:	TextEdit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
GNUstep Backbone applications, including Preferences.

%description -l pl
Szkieletowe aplikacje GNUstepa, w tym Preferences (edytor ustawieñ).

%package devel
Summary:	Header files for Backbone frameworks
Summary(pl):	Pliki nag³ówkowe dla bibliotek Backbone
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-gui-devel
Obsoletes:	Preferences-devel

%description devel
Header files for Backbone frameworks.

%description devel -l pl
Pliki nag³ówkowe dla bibliotek Backbone.

%prep
%setup -q -n System
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
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
%{_prefix}/System/Applications/*.app/Resources/*.txt
%{_prefix}/System/Applications/*.app/Resources/*.svcs
%{_prefix}/System/Applications/*.app/Resources/English.lproj
%lang(fr) %{_prefix}/System/Applications/*.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/*.app/Resources/German.lproj
%lang(hu) %{_prefix}/System/Applications/*.app/Resources/Hungarian.lproj
%lang(nb) %{_prefix}/System/Applications/*.app/Resources/Norwegian.lproj
%lang(ru) %{_prefix}/System/Applications/*.app/Resources/Russian.lproj
%lang(es) %{_prefix}/System/Applications/*.app/Resources/Spanish.lproj
%lang(se) %{_prefix}/System/Applications/*.app/Resources/Swedish.lproj
%lang(tr) %{_prefix}/System/Applications/*.app/Resources/Turkish.lproj
%dir %{_prefix}/System/Applications/*.app/%{gscpu}
%dir %{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Preferences.app/Preferences
%attr(755,root,root) %{_prefix}/System/Applications/Preferences.app/%{gscpu}/%{gsos}/%{libcombo}/Preferences
%attr(755,root,root) %{_prefix}/System/Applications/Terminal.app/Terminal
%attr(755,root,root) %{_prefix}/System/Applications/Terminal.app/%{gscpu}/%{gsos}/%{libcombo}/Terminal
%attr(755,root,root) %{_prefix}/System/Applications/TextEdit.app/TextEdit
%attr(755,root,root) %{_prefix}/System/Applications/TextEdit.app/%{gscpu}/%{gsos}/%{libcombo}/TextEdit
%{_prefix}/System/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
%attr(755,root,root) %{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/*

%dir %{_prefix}/System/Library/Frameworks/*.framework
%{_prefix}/System/Library/Frameworks/*.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/*
%{_prefix}/System/Library/Frameworks/*.framework/Versions/1.1.0/Resources
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/*.framework/Versions/1.1.0/%{gscpu}

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
