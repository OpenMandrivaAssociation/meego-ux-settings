Name: meego-ux-settings
Version: 0.42
Release: %mkrel 1
Summary: Package to set schemas for the MeeGo Shell
Group: Graphical desktop/Other
License: LGPLv2.1
URL: http://www.meego.com
Source0: README
Source1: %gconf-tree.xml
Source2: air-environment.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: gnome-vfs2
Requires: nautilus
Requires: fonts-ttf-droid
Requires: mutter-meego
Requires: mojito
Requires: meego-gtk-engine
Requires: meego-icon-theme
Requires: meego-sound-theme
Requires: meego-panel-applications
Requires: meego-panel-media
Requires: meego-panel-myzone
Requires: meego-panel-pasteboard
Requires: meego-panel-people
Requires: meego-panel-status
Requires: meego-web-browser-panel
BuildRequires: GConf2
Obsoletes: meego-ux-settings <= 0.19

%description
Package to install MeeGo schema file.

%prep
%setup -q -c -T
cp -a %{_sysconfdir}/gconf/2/path gconf.path

%build
sed -i -e 's@\(include /etc/gconf/2/local-defaults.path\)@\1\n\n# MeeGo settings.\nxml:readonly:/etc/gconf/gconf.xml.meego@' gconf.path

%install
cp %{SOURCE0} .
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.meego
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.meego
mkdir -p %{buildroot}%{_sysconfdir}/gconf/2
cp gconf.path %{buildroot}%{_sysconfdir}/gconf/2/meego.path
install -d $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

%files
%defattr(-,root,root,-)
%doc README
%{_sysconfdir}/gconf/gconf.xml.meego/%gconf-tree.xml
%{_sysconfdir}/profile.d/air-environment.sh
%{_sysconfdir}/gconf/2/meego.path
