Summary:        Plasmoid for fancy representing your tasks and launchers	
Name:		plasma-applet-fancytasks
Version: 	0.8.1
Release: 	%mkrel 1
Source0: 	http://www.kde-look.org/CONTENT/content-files/99737-fancytasks-%{version}.tar.bz2
License: 	GPLv2
Group: 		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php/Fancy+Tasks?content=99737
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel
Requires:       kdebase4-runtime

%description 
Plasmoid for fancy representing your tasks and launchers. Inspired by Avant
Window Navigator and other MacOS X like docks.

Features:
- manages your tasks and launchers;
- tasks filtering, grouping (including manual) and sorting;
- launcher to task transition (icons of launchers with running tasks are
hidden);
- preview of windows with (live previews with KWin Taskbar Thumbnail effect
enabled) and without Composite (also for groups, you can click them to activate
window);
- dropping files on launchers runs command with parameters or gives option to
move, copy or link them (if this is directory);
- visual drop indicator that helps in manual tasks sorting and dropping
launchers;
- possibility to browse directories of directory launchers using context menu;
- menu with list of all icons shown after activating keyboard shortcut;
- configurable animations (zoom, jump, bounce, highlight, etc.) and appearance
(optional thumbnails, reflections and text label);
- fully animated icons (including animations of starting applications and tasks
needing attention).




%files -f %{name}.lang
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_fancytasks.so
%_kde_appsdir/desktoptheme/default/widgets/fancytasks.svg
%_kde_datadir/kde4/services/plasma-applet-fancytasks.desktop
%_kde_datadir/locale/*/LC_MESSAGES/*.mo

#--------------------------------------------------------------------

%prep
%setup -q -n fancytasks-%{version}


%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %{name}

%clean
rm -rf %{buildroot}


