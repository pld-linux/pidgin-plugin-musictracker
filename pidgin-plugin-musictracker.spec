%define pidgin_ver %(pkg-config --modversion pidgin 2>/dev/null || echo ERROR)
Summary:	A plugin for Pidgin which displays the media currently playing in the status message
Summary(hu.UTF-8):	Egy plugin Pidginhez, amely az aktuálisan játszott dalt jeleníti meg az állapotüzenetben
Name:		pidgin-plugin-musictracker
Version:	0.4.21
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://pidgin-musictracker.googlecode.com/files/pidgin-musictracker-%{version}.tar.bz2
# Source0-md5:	38910d634b590e47f7766929c436f1a7
URL:		http://code.google.com/p/pidgin-musictracker/
BuildRequires:	pidgin-devel >= 2.2
BuildRequires:	pkgconfig
Requires:	pidgin >= %{pidgin_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pidgin-musictracker is a plugin for Pidgin which displays the media
currently playing in the status message for any protocol Pidgin
supports custom statuses on.

Currently supported players on Linux:
- Amarok
- Audacious
- Banshee
- Exaile
- Last.fm feed
- Listen
- MOC >= 2.5.0alpha
- MPD
- Quod Libet
- Rhythmbox
- Songbird + DBusBird addon
- SqueezeCenter
- Vagalume
- XMMS
- XMMS2 >= 0.6
- any player supporting the MPRIS DBus interface (Amarok2, BMPx,
  dragonplayer, Exaile >= 0.3, Goggles Music Manager, QMMP >=0.3,
  Rhythmbox, Songbird + MPRIS addon, VLC >0.9.0, etc.)

%description -l hu.UTF-8
pidgin-musictracker egy plugin Pidgin-hez, amely az aktuálisan
játszott dalt jeleníti meg a státuszüzenetben minden olyan protokoll
esetén, amelyhez a Pidgin támogatja az egyéni állapotokat.

Támogatott linuxos lejátszók:
- Amarok
- Audacious
- Banshee
- Exaile
- Last.fm feed
- Listen
- MOC >= 2.5.0alpha
- MPD
- Quod Libet
- Rhythmbox
- Songbird + DBusBird addon
- SqueezeCenter
- Vagalume
- XMMS
- XMMS2 >= 0.6
- minden lejátszó, amely támogatja az MPRIS DBus felületet (Amarok2,
  BMPx, dragonplayer, Exaile >= 0.3, Goggles Music Manager, QMMP >=0.3,
  Rhythmbox, Songbird + MPRIS addon, VLC >0.9.0, etc.)

%prep
%setup -q -n pidgin-musictracker-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/locale/en@*

%find_lang musictracker

%clean
rm -rf $RPM_BUILD_ROOT

%files -f musictracker.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS THANKS ChangeLog
%attr(755,root,root) %{_libdir}/pidgin/*.so
