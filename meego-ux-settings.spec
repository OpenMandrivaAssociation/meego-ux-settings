Name: meego-ux-settings
Version: 0.42
Release: %mkrel 1
Summary: Package to setup the environment and schemas
Group: Desktop/Interface
License: LGPLv2.1
URL: https://www.meego.com
Source0: README
Source1: %gconf-tree.xml
Source2: air-environment.sh
Source3: meego.path
BuildArch: noarch
BuildRequires: GConf2
BuildRequires: libxml2-utils
Obsoletes: moblin-ux-settings <= 0.19
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Package to install Netbook schemas and stuff.

%prep

%build

%install
cp %{SOURCE0} .
install -d %{buildroot}%{_sysconfdir}/gconf/gconf.xml.meego
xmllint %{SOURCE1} && install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gconf/gconf.xml.meego
install -d %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/gconf/2/meego.path

%files
%defattr(-,root,root,-)
%doc README
%{_sysconfdir}/gconf/2/meego.path
%{_sysconfdir}/gconf/gconf.xml.meego/%gconf-tree.xml
%{_sysconfdir}/profile.d/air-environment.sh
