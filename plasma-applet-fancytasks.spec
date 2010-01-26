Summary:	Plasmoid for fancy representing your tasks and launchers
Name:		plasma-applet-fancytasks
Version:	0.9.9a
Release:	%mkrel 1
Source0:	http://www.kde-look.org/CONTENT/content-files/99737-fancytasks-%{version}.tar.bz2
#Patch0:		plasma-applet-fancytasks-fix-tooltips.patch
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php/Fancy+Tasks?content=99737
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel
BuildRequires:	kdebase4-devel
BuildRequires:	qimageblitz-devel
Requires:	kdebase4-runtime => 4.3
Provides:	plasma-applet

%description
Plasmoid for fancy representing your tasks and launchers. Inspired by
Avant Window Navigator and other MacOS X like docks.

Features:
- manages your tasks and launchers;
- tasks filtering, grouping (including manual) and sorting;
- launcher to task transition (icons of launchers with running tasks
are hidden);
- preview of windows with (live previews with KWin Taskbar Thumbnail
effect enabled) and without Composite (also for groups, you can click
them to activate window);
- dropping files on launchers runs command with parameters or gives
option to move, copy or link them (if this is directory);
- visual drop indicator that helps in manual tasks sorting and
dropping launchers;
- possibility to browse directories of directory launchers using
context menu;
- menu with list of all icons shown after activating keyboard
shortcut;
- configurable animations (zoom, jump, bounce, highlight, etc.) and
appearance (optional thumbnails, reflections and text label);
- fully animated icons (including animations of starting applications
and tasks needing attention).

%files -f plasma_applet_fancytasks.lang 
%defattr(-,root,root)
%doc INSTALL COPYING README TODO CHANGELOG
%_kde_libdir/kde4/plasma_applet_fancytasks.so
%_kde_appsdir/desktoptheme/default/widgets/fancytasks.svgz
%_kde_services/plasma-applet-fancytasks.desktop
%_kde_libdir/kde4/plasma_containment_fancypanel.so
%_kde_services/plasma-containment-fancypanel.desktop


#--------------------------------------------------------------------

%prep
%setup -q -n fancytasks-%{version}
#%patch0 -p 0
%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang plasma_applet_fancytasks 
# Containement fancy panel now have some localisations, since it's still experimental
# and upstream does not want to split the package i'm merging the language file list
%find_lang plasma_containment_fancypanel
cat plasma_containment_fancypanel.lang >> plasma_applet_fancytasks.lang

%clean
%__rm -rf %{buildroot}
