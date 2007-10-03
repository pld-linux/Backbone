%define cvs	20070830
Summary:	GNUstep backbone apps, including Preferences
Summary(pl.UTF-8):	Szkieletowe aplikacje GNUstepa, w tym Preferences
Name:		Backbone
Version:	1.2.99
Release:	0.%{cvs}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{cvs}.tar.gz
# Source0-md5:	e27413e9e105cfa3bb2eaf953fa3661f
Patch0:		%{name}-buildinplace.patch
Patch1:		%{name}-installprefix.patch
Patch2:		%{name}-pass-arguments.patch
Patch3:		%{name}-install.patch
URL:		http://www.nongnu.org/backbone/
BuildRequires:	gnustep-gui-devel
Obsoletes:	Preferences
Obsoletes:	Terminal
Obsoletes:	TextEdit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUstep Backbone applications, including Preferences.

%description -l pl.UTF-8
Szkieletowe aplikacje GNUstepa, w tym Preferences (edytor ustawień).

%package devel
Summary:	Header files for Backbone frameworks
Summary(pl.UTF-8):	Pliki nagłówkowe dla bibliotek Backbone
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-gui-devel
Obsoletes:	Preferences-devel

%description devel
Header files for Backbone frameworks.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla bibliotek Backbone.

%prep
%setup -q -n System
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} -j1 \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} -j1 install \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT 

for f in Calculator CurrencyConverter GSTest Ink NSBrowserTest NSImageTest NSPanelTest NSScreenTest md5Digest ; do
	ln -sf %{_libdir}/GNUstep/Applications/$f.app/$f $RPM_BUILD_ROOT/%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/GNUstep/Applications/*.app
%dir %{_libdir}/GNUstep/Applications/*.app/Resources
%{_libdir}/GNUstep/Applications/*.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/*.app/Resources/*.plist
%{_libdir}/GNUstep/Applications/*.app/Resources/*.tiff
%{_libdir}/GNUstep/Applications/*.app/Resources/*.txt
%{_libdir}/GNUstep/Applications/*.app/Resources/*.svcs
%{_libdir}/GNUstep/Applications/*.app/Resources/English.lproj
%lang(fr) %{_libdir}/GNUstep/Applications/*.app/Resources/French.lproj
%lang(de) %{_libdir}/GNUstep/Applications/*.app/Resources/German.lproj
%lang(hu) %{_libdir}/GNUstep/Applications/*.app/Resources/Hungarian.lproj
%lang(nb) %{_libdir}/GNUstep/Applications/*.app/Resources/Norwegian.lproj
%lang(ru) %{_libdir}/GNUstep/Applications/*.app/Resources/Russian.lproj
%lang(es) %{_libdir}/GNUstep/Applications/*.app/Resources/Spanish.lproj
%lang(se) %{_libdir}/GNUstep/Applications/*.app/Resources/Swedish.lproj
%lang(tr) %{_libdir}/GNUstep/Applications/*.app/Resources/Turkish.lproj
%dir %{_libdir}/GNUstep/Applications/*.app/%{gscpu}
%dir %{_libdir}/GNUstep/Applications/*.app/%{gscpu}/%{gsos}
%dir %{_libdir}/GNUstep/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Preferences.app/Preferences
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Preferences.app/%{gscpu}/%{gsos}/%{libcombo}/Preferences
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Terminal.app/Terminal
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Terminal.app/%{gscpu}/%{gsos}/%{libcombo}/Terminal
%attr(755,root,root) %{_libdir}/GNUstep/Applications/TextEdit.app/TextEdit
%attr(755,root,root) %{_libdir}/GNUstep/Applications/TextEdit.app/%{gscpu}/%{gsos}/%{libcombo}/TextEdit
%{_libdir}/GNUstep/Applications/*.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
%attr(755,root,root) %{_libdir}/GNUstep/Tools/%{gscpu}/%{gsos}/%{libcombo}/*

%dir %{_libdir}/GNUstep/Library/Frameworks/*.framework
%{_libdir}/GNUstep/Library/Frameworks/*.framework/Resources
%dir %{_libdir}/GNUstep/Library/Frameworks/*.framework/Versions
%dir %{_libdir}/GNUstep/Library/Frameworks/*.framework/Versions/*
%{_libdir}/GNUstep/Library/Frameworks/*.framework/Versions/1.1.0/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Library/Frameworks/*.framework/Versions/1.1.0/%{gscpu}

%attr(755,root,root) %{_libdir}/GNUstep/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%dir %{_libdir}/GNUstep/Library/Preferences
%dir %{_libdir}/GNUstep/Library/Preferences/*.prefs
%{_libdir}/GNUstep/Library/Preferences/*.prefs/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Library/Preferences/*.prefs/%{gscpu}
 
%files devel
%defattr(644,root,root,755)
%{_libdir}/GNUstep/Library/Frameworks/*.framework/Headers
%{_libdir}/GNUstep/Library/Frameworks/*.framework/Versions/1.1.0/Headers
%{_libdir}/GNUstep/Library/Headers/%{libcombo}/*

%attr(755,root,root) %{_libdir}/GNUstep/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
