%global distro linux
%define __strip /bin/true
%define __jar_repack %{nil}

Name:		android-studio
Version:	135.1339820
Release:	1%{?dist}
Summary:	Android development environment based on IntelliJ IDEA
Group:		Development/Libraries
License:	FIXME
URL:		http://your.project.com
Source0:	%{name}-bundle-%{version}-%{distro}.tgz
Source1:	android-studio.xml
Source2:	android-studio.desktop
BuildRequires: chrpath
Requires:   java-devel
Requires:   glibc(%{__isa_name}-32)
Requires:   glibc(%{__isa_name}-32)
Requires:   libstdc++(%{__isa_name}-32)
Requires:   zlib-devel(%{__isa_name}-32)
Requires:   ncurses-devel(%{__isa_name}-32)
Requires:   libX11-devel(%{__isa_name}-32)
Requires:   libXrender(%{__isa_name}-32)
Requires:   libXrandr(%{__isa_name}-32)

AutoReqProv:    no


%description
Put some description here.
Can be multiline.

%prep
%setup -q -n %{name}

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps/%{name}
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,license,plugins,sdk,LICENSE.txt} %{buildroot}%{_javadir}/%{name}/
cp -af ./bin/idea.png %{buildroot}%{_datadir}/pixmaps/%{name}/idea.png
cp -af %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE2} %{buildroot}%{_datadir}/android-studio.desktop
ln -s %{_javadir}/%{name}/bin/studio.sh %{buildroot}%{_bindir}/studio
ls %{buildroot}%{_javadir}/%{name}/sdk/tools/lib/monitor-x86_64/
chrpath --delete %{buildroot}%{_javadir}/%{name}/sdk/tools/lib/monitor-x86_64/libcairo-swt.so
desktop-file-install				\
--add-category="Development"			\
--delete-original				\
--dir=%{buildroot}%{_datadir}/applications	\
%{buildroot}%{_datadir}/android-studio.desktop

%files
%defattr(-,root,root)
%doc LICENSE.txt
%doc license/
%{_javadir}/%{name}/*
%{_bindir}/studio
%{_datadir}/pixmaps/%{name}/idea.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/applications/android-studio.desktop

%changelog
* Mon Sep 29 2014 Petr Hracek <phracek@redhat.com> 135.1339820-1
- First version
