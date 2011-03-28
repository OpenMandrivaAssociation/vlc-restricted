%define name 		vlc
%define version 1.1.8
%define snapshot	0
%define pre		0
%define rel 2
%if %pre
%define release		%mkrel -c %pre %rel
%elsif %snapshot
%define release %mkrel -c %snapshot %rel
%else
%define release %mkrel %rel
%endif

%define	libmajor	5
%define coremajor	4
%if %snapshot
%define fname %name-snapshot-%snapshot
%elsif %pre
%define fname %name-%version-%pre
%else
%define fname %name-%version
%endif

%define with_plf 0

%define with_xulrunner 1
%define with_fribidi 1
%define with_xml 1
%define with_ncurses 1
%define with_lirc 1
%define	with_qt4 1
%define	with_svlc 1
%define with_udev 1
%define with_aa 1
%define with_sdl 1
%define with_sdl_image 1
%define with_ggi 1
%define with_svgalib 1
%define with_fb 1
%define with_xosd 1
%define with_xvideo 1
%define with_twolame 1
%define with_schroedinger 1
%define with_fluidsynth 1
%define with_gme 1
%define with_zvbi 1
%define with_kate 1
%define with_kde 1
%define with_goom 1
%define with_projectm 1
%define with_ass 1
%define with_lua 1
%define with_taglib 1
%define with_mtp 1
%define with_xcb_randr 1

%ifarch %{ix86}
%define with_loader 1
%else
%define with_loader 0
%endif

%define with_mad 1
%define with_ogg 1
%define with_theora 1
%define with_speex 1
%define with_flac 1
%define with_mkv 1
%define with_a52 1
%define with_vcd 1
%define with_cddb 1
%define with_dv 1
%define with_dvdnav 1
%define with_dvb 1
%define with_dvbpsi 1
%define with_satellite 0
%define	with_mpeg2dec 1
%define	with_mpc 1
%define	with_faad 0
%define	with_faac 0
%define	with_lame 0
%define	with_dts 0
%define	with_x264 0
%define with_live 1
%define with_libv4l 1
%define with_sysfs 1
%define with_shout 1

%define with_pulse 1
%define with_jack 1
%define with_alsa 1

%define with_bonjour 1
%define with_upnp 1
%define with_smb 1
%define with_tar 1
%define with_mod 1
%define with_gnutls 1

%define libname		%mklibname %name %libmajor
%define libnamecore	%mklibname vlccore %coremajor
%define develname %mklibname -d %name

# without
%{?_without_plf:	%{expand: %%global with_plf 0}}
%{?_without_xulrunner:	%{expand: %%global with_xulrunner 0}}
%{?_without_fribidi:	%{expand: %%global with_fribidi 0}}
%{?_without_udev:	%{expand: %%global with_udev 0}}
%{?_without_ncurses:	%{expand: %%global with_ncurses 0}}
%{?_without_lirc:	%{expand: %%global with_lirc 0}}
%{?_without_qt4:	%{expand: %%global with_qt4 0}}
%{?_without_svlc:	%{expand: %%global with_svlc 0}}

%{?_without_aa:   	%{expand: %%global with_aa 0}}
%{?_without_sdl:   	%{expand: %%global with_sdl 0}}
%{?_without_ggi:   	%{expand: %%global with_ggi 0}}
%{?_without_svgalib:	%{expand: %%global with_svgalib 0}}
%{?_without_fb:		%{expand: %%global with_fb 0}}
%{?_without_xosd:	%{expand: %%global with_xosd 0}}
%{?_without_xvideo:	%{expand: %%global with_xvideo 0}}
%{?_without_twolame:	%{expand: %%global with_twolame 0}}
%{?_without_schroedinger: %{expand: %%global with_schroedinger 0}}
%{?_without_fluidsynth:	%{expand: %%global with_fluidsynth 0}}
%{?_without_gme:	%{expand: %%global with_gme 0}}
%{?_without_lua:	%{expand: %%global with_lua 0}}
%{?_without_zvbi:	%{expand: %%global with_zvbi 0}}
%{?_without_kate:	%{expand: %%global with_kate 0}}

%{?_without_mad:	%{expand: %%global with_mad 0}}
%{?_without_ogg:	%{expand: %%global with_ogg 0}}
%{?_without_theora:	%{expand: %%global with_theora 0}}
%{?_without_speex:	%{expand: %%global with_speex 0}}
%{?_without_flac:	%{expand: %%global with_flac 0}}
%{?_without_mkv:	%{expand: %%global with_mkv 0}}
%{?_without_mpeg2dec:	%{expand: %%global with_mpeg2dec 0}}
%{?_without_mpc:	%{expand: %%global with_mpc 0}}
%{?_without_faad:	%{expand: %%global with_faad 0}}
%{?_without_faac:	%{expand: %%global with_faac 0}}
%{?_without_x264:	%{expand: %%global with_x264 0}}
%{?_without_lame:	%{expand: %%global with_lame 0}}
%{?_without_dts:	%{expand: %%global with_dts 0}}
%{?_without_live:	%{expand: %%global with_live 0}}
%{?_without_a52:	%{expand: %%global with_a52 0}}
%{?_without_dv:		%{expand: %%global with_dv 0}}
%{?_without_dvdnav:	%{expand: %%global with_dvdnav 0}}
%{?_without_dvb:	%{expand: %%global with_dvb 0}}
%{?_without_dvbpsi:	%{expand: %%global with_dvbpsi 0}}
%{?_without_libv4l:	%{expand: %%global with_libv4l 0}}
%{?_without_sysfs:	%{expand: %%global with_sysfs 0}}
%{?_without_satellite:	%{expand: %%global with_satellite 0}}
%{?_without_vcd:	%{expand: %%global with_vcd 0}}
%{?_without_cddb:	%{expand: %%global with_cddb 0}}
%{?_without_shout:	%{expand: %%global with_shout 0}}


%{?_without_pulse:	%{expand: %%global with_pulse 0}}
%{?_without_jack:	%{expand: %%global with_jack 0}}
%{?_without_alsa:	%{expand: %%global with_alsa 0}}

%{?_without_bonjour:	%{expand: %%global with_bonjour 0}}
%{?_without_upnp:	%{expand: %%global with_upnp 0}}
%{?_without_tar:	%{expand: %%global with_tar 0}}
%{?_without_mod:	%{expand: %%global with_mod 0}}
%{?_without_gnutls:	%{expand: %%global with_gnutls 0}}

# with
%{?_with_plf:    	%{expand: %%global with_plf 1}}
%{?_with_xulrunner:    	%{expand: %%global with_xulrunner 1}}
%{?_with_fribidi:    	%{expand: %%global with_fribidi 1}}
%{?_with_udev:		%{expand: %%global with_udev 1}}
%{?_with_ncurses:    	%{expand: %%global with_ncurses 1}}
%{?_with_lirc:       	%{expand: %%global with_lirc 1}}
%{?_with_qt4:		%{expand: %%global with_qt4 1}}
%{?_with_svlc:		%{expand: %%global with_svlc 1}}

%{?_with_aa:         	%{expand: %%global with_aa 1}}
%{?_with_sdl:        	%{expand: %%global with_sdl 1}}
%{?_with_ggi:        	%{expand: %%global with_ggi 1}}
%{?_with_svgalib:    	%{expand: %%global with_svgalib 1}}
%{?_with_fb:        	%{expand: %%global with_fb 1}}
%{?_with_xosd:       	%{expand: %%global with_xosd 1}}
%{?_with_xvideo:       	%{expand: %%global with_xvideo 1}}
%{?_with_twolame:      	%{expand: %%global with_twolame 1}}
%{?_with_schroedinger: 	%{expand: %%global with_schroedinger 1}}
%{?_with_fluidsynth:	%{expand: %%global with_fluidsynth 1}}
%{?_with_gme:		%{expand: %%global with_gme 1}}
%{?_with_lua:      	%{expand: %%global with_lua 1}}
%{?_with_zvbi:      	%{expand: %%global with_zvbi 1}}
%{?_with_kate:      	%{expand: %%global with_kate 1}}

%{?_with_mad:		%{expand: %%global with_mad 1}}
%{?_with_ogg:        	%{expand: %%global with_ogg 1}}
%{?_with_theora:       	%{expand: %%global with_theora 1}}
%{?_with_speex:        	%{expand: %%global with_speex 1}}
%{?_with_flac:        	%{expand: %%global with_flac 1}}
%{?_with_mkv:        	%{expand: %%global with_mkv 1}}
%{?_with_mpeg2dec:     	%{expand: %%global with_mpeg2dec 1}}
%{?_with_mpc:      	%{expand: %%global with_mpc 1}}
%{?_with_faad:      	%{expand: %%global with_faad 1}}
%{?_with_faac:      	%{expand: %%global with_faac 1}}
%{?_with_x264:      	%{expand: %%global with_x264 1}}
%{?_with_lame:      	%{expand: %%global with_lame 1}}
%{?_with_dts:      	%{expand: %%global with_dts 1}}
%{?_with_live:      	%{expand: %%global with_live 1}}
%{?_with_a52:        	%{expand: %%global with_a52 1}}
%{?_with_dv:         	%{expand: %%global with_dv 1}}
%{?_with_dvdnav:       	%{expand: %%global with_dvdnav 1}}
%{?_with_dvb:        	%{expand: %%global with_dvb 1}}
%{?_with_dvbpsi:       	%{expand: %%global with_dvbpsi 1}}
%{?_with_libv4l:       	%{expand: %%global with_libv4l 1}}
%{?_with_sysfs:       	%{expand: %%global with_sysfs 1}}
%{?_with_satellite:    	%{expand: %%global with_satellite 1}}
%{?_with_vcd:		%{expand: %%global with_vcd 1}}
%{?_with_cddb:		%{expand: %%global with_cddb 1}}
%{?_with_shout:		%{expand: %%global with_shout 1}}

%{?_with_pulse:       	%{expand: %%global with_pulse 1}}
%{?_with_jack:        	%{expand: %%global with_jack 1}}
%{?_with_alsa:       	%{expand: %%global with_alsa 1}}

%{?_with_bonjour:	%{expand: %%global with_bonjour 1}}
%{?_with_upnp:		%{expand: %%global with_upnp 1}}
%{?_with_tar:		%{expand: %%global with_tar 1}}
%{?_with_mod:		%{expand: %%global with_mod 1}}
%{?_with_gnutls:		%{expand: %%global with_gnutls 1}}

%if %mdvver < 201010
%define with_sdl_image 0
%endif

%if %mdvver < 201000
%define with_schroedinger 0
%define with_udev 0
%define with_dv 0
%define with_xcb_randr 0
%endif

%if %with_plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%define distsuffix plf
%global with_faac 1
%global with_faad 1
%global with_lame 1
%global with_dts 1
%global with_x264 1
%endif

%define git_url git://git.videolan.org/vlc.git

Summary:	MPEG, MPEG2, DVD and DivX player
Name:		%{name}
Version:	%{version}
Release:	%{release}%{?extrarelsuffix}
%if %snapshot
Source0:	http://nightlies.videolan.org/build/source/%fname.tar.bz2
%else
Source0:	http://download.videolan.org/pub/videolan/%name/%{version}/%{fname}.tar.bz2
%endif
#gw patches from Debian:
#use absolute paths for OSD menu config
Patch16: 200_osdmenu_paths.diff
Patch18: vlc-1.1-new-xulrunner.patch
# (cg) The version of PA on mdv 2010.1+updates is OK for VLC so it should be patched accordingly
Patch19: vlc-1.1.7-mdv2010.1-updated-pulse-version-is-ok.patch
License:	GPLv2+
Group:		Video
URL:		http://www.videolan.org/
# might be useful too:
Suggests:	vlc-plugin-theora
%if %with_pulse
# needed when using pulseaudio
Suggests:	vlc-plugin-pulse
%endif
Provides:	vlc-plugin-dvb vlc-plugin-mad vlc-plugin-alsa
Obsoletes:	vlc-plugin-dvb vlc-plugin-mad vlc-plugin-alsa
Requires:	fonts-ttf-vera

BuildRoot:	%_tmppath/%name-%version-%release-root
%if %with_sysfs
BuildRequires:  libsysfs-devel
%endif
%if %with_tar
BuildRequires:  libtar-devel
%endif
%if %with_mod
BuildRequires:  libmodplug-devel >= 1:0.7
%endif
%if %with_gnutls
BuildRequires:  libgnutls-devel >= 1.0.17
%endif
BuildRequires:  freetype2-devel
%if %with_fribidi
BuildRequires:  libfribidi-devel
%endif
%if %with_xulrunner
BuildRequires: xulrunner-devel
%endif
%if %with_libv4l
%if %mdvver >= 201010
BuildRequires: v4l-utils-devel
%else
BuildRequires: libv4l-devel
%endif
%endif
%if %with_udev
BuildRequires: udev-devel >= 142
%endif
Provides: gvlc
Obsoletes: gvlc
Provides: gnome-vlc
Obsoletes: gnome-vlc
Provides: kvlc
Obsoletes: kvlc
%if %with_qt4
Buildrequires:	qt4-devel
%endif
BuildRequires: libmesaglu-devel
%if %with_taglib
BuildRequires: taglib-devel > 1.5
%endif
%if %with_mtp
BuildRequires: libmtp-devel >= 1.0.0
%endif
%if %with_mad
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
%endif
%if %with_ogg
Buildrequires:	libvorbis-devel
Buildrequires:	libogg-devel
Provides: vlc-plugin-ogg
Obsoletes: vlc-plugin-ogg
%endif
BuildRequires: xpm-devel
BuildRequires: libxcb-util-devel
%if %with_xcb_randr
BuildRequires: libxcb-devel > 1.2
%endif
BuildRequires: libproxy-devel
%if %with_speex
Buildrequires:	libspeex-devel >= 1.1.6
%endif
%if %with_flac
Buildrequires:	libflac-devel
%endif
%if %with_mkv
Buildrequires:	libmatroska-devel >= 0.8.0
%endif
%if %with_dvdnav
Buildrequires:	libdvdnav-devel >= 0.1.9
Provides: vlc-plugin-dvdnav
Obsoletes: vlc-plugin-dvdnav
%endif
%if %with_a52
Buildrequires:	liba52dec-devel
Provides:	vlc-plugin-a52
Obsoletes: vlc-plugin-a52

%endif
%if %with_vcd
BuildRequires: libvcd-devel >= 0.7.21
%endif
BuildRequires: libcdio-devel >= 0.72
%if %with_cddb
BuildRequires: libcddb-devel >= 0.9.5
%else
BuildConflicts: libcddb-devel
%endif
%if %with_smb
BuildRequires: libsmbclient-devel >= 3.0.10
%endif
Buildrequires:	libffmpeg-devel
%if %with_lame
BuildRequires:  liblame-devel
%endif

%if %with_mpeg2dec
Buildrequires:	libmpeg2dec-devel >= 0.4.0
%endif
%if %with_mpc
BuildRequires: libmpcdec-devel
%endif
%if %with_faad
BuildRequires: libfaad2-devel >= 2.0
Provides: vlc-plugin-faad
Obsoletes: vlc-plugin-faad
%endif
%if %with_faac
BuildRequires: libfaac-devel
%endif
%if %with_alsa
BuildRequires:	libalsa-devel
%endif
%if %with_pulse
BuildRequires:	pulseaudio-devel >= 0.9.10
%endif
%if %with_jack
BuildRequires:	libjack-devel
BuildRequires:	libsamplerate-devel
%endif
Provides: vlc-plugin-slp
Obsoletes: vlc-plugin-slp

%if %with_bonjour
BuildRequires: avahi-client-devel
%endif

%if %with_dvbpsi
BuildRequires: libdvbpsi-devel
%endif
BuildRequires: autoconf2.5
BuildRequires: gettext-devel
BuildRequires: automake >= 1.10
BuildRequires: libtool
%if %with_dts
BuildRequires:  libdca-devel
%endif
%if %with_x264
BuildRequires:  x264-devel > 0.65.2245
%endif
%if %with_xml
BuildRequires: libxml2-devel >= 2.6
%endif
%if %with_live
BuildRequires: live-devel > 2007.12.27
%endif
%if %with_xvideo
BuildRequires:	libxv-devel
%endif
BuildRequires: libnotify-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: portaudio-devel
BuildRequires: dirac-devel
BuildRequires: librsvg-devel
BuildRequires: libcaca-devel
%if %with_kde
BuildRequires: kdelibs4-core
%endif
%if %with_projectm
%endif
BuildRequires: desktop-file-utils
Provides: wxvlc
Obsoletes: wxvlc
BuildRequires:  libdvdread-devel
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
VideoLAN is an OpenSource streaming solution for every OS developed by
students from the Ecole Centrale Paris and developers from all over the
World.
VLC (VideoLAN Client) is a media player that can play MPEG1, MPEG2 and
MPEG4 (aka DivX) files, DVDs, VCDs, SVCDs, from a satellite card, from
a stream sent by VLS (VideoLAN Server), from another VLC, or from a Web
server.
This package contains no CSS unscrambling functionality for DVDs ;
you need the libdvdcss library available from 
http://www.videolan.org/libdvdcss/

%if %with_plf
This package is in PLF as it is violating software patents.
%endif

#general packages
%package -n %libname
Summary: Shared code for the VLC media player
Group: System/Libraries

%description -n %libname
Shared code for the VLC media player
This package contains code that is shared by different modules of the 
VLC media player.

%package -n %libnamecore
Summary: Shared core code for the VLC media player
Group: System/Libraries
#gw needed by the python bindings:
Provides: libvlccore = %version-%release

%description -n %libnamecore
Shared core code for the VLC media player
This package contains code that is shared by different modules of the
VLC media player.

%package -n %develname
Summary: Development files for the VLC media player
Group: Development/C
Requires: %libname = %version
Requires: %libnamecore = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Obsoletes: %mklibname -d %name 0

%description -n %develname
Development files for the VLC media player
This package contains headers and a static library required to build plugins
for the VLC media player, or standalone applications using features from VLC.

%package -n mozilla-plugin-vlc
Summary: Multimedia plugin for Mozilla, based on vlc
group: Video
Requires: %name = %version
%description -n mozilla-plugin-vlc
This plugin adds support for MPEG, MPEG2, DVD and DivX to your Mozilla
browser. The decoding process is done by vlc and the output window is
embedded in a webpage or directly in the browser window. There is also
support for fullscreen display.
%if %with_plf
This PLF build has additional support for MP3 encoding with lame,
which is covered by software patents.
%endif

%if %with_zvbi
%package plugin-zvbi
Summary: Add Teletext and Closed Caption support to VLC
Group: Video
Requires: %name = %version
BuildRequires: zvbi-devel

%description plugin-zvbi
This package adds support for Raw VBI, Teletext and Closed Caption based on
the ZVBI library to VLC.
%endif

%if %with_kate
%package plugin-kate
Summary: Add subtitle and Karaoke text support to VLC
Group: Video
Requires: %name = %version
BuildRequires: libtiger-devel

%description plugin-kate
This package adds support for subtitles and Karaoke text display based on
the libkate library to VLC.
%endif

%if %with_ass
%package plugin-libass
Summary: Add subtitle support to VLC using libass
Group: Video
Requires: %name = %version
BuildRequires: libass-devel

%description plugin-libass
This package adds support for subtitles based on the libass library to VLC.
%endif

%if %with_lua
%package plugin-lua
Summary: Add Lua scripting to vlc
Group: Video
Requires: %name = %version
BuildRequires: lua-devel >= 5.1


%description plugin-lua
This plugin adds lua scripting and provides a few example scripts as well.
%endif

%if %with_ncurses
%package plugin-ncurses
Summary: Ncurses console-based plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Buildrequires:	libncurses-devel

%description plugin-ncurses
This plugin adds a ncurses interface to the VLC media player. To
activate it, use the `--intf ncurses' flag.
%endif

%if %with_lirc
%package plugin-lirc
Summary: Lirc plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Obsoletes: vlc-lirc
Provides: vlc-lirc
Buildrequires:	liblirc-devel

%description plugin-lirc
This plugin is an infrared lirc interface for the VLC media player. To
activate it, use the `--extraintf lirc' flag.
%endif

%package -n svlc
Summary: Skinned GUI plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Provides: vlc-gui
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description -n svlc
This plugin adds a skinned GUI interface to the VLC media player. To
activate it, run the `svlc' program.

#
# video plugins
%if %with_aa
%package plugin-aa
Summary: ASCII art video plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Obsoletes: vlc-aa
Provides: vlc-aa
Buildrequires:	aalib-devel

%description plugin-aa
This is an ASCII art video output plugin for the VLC media playe. To
activate it, use the `--vout aa' flag or select the `aa' video output
plugin from the preferences menu.
%endif

%if %with_sdl
%package plugin-sdl
Summary: Simple DirectMedia Layer video plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Obsoletes: vlc-sdl
Provides: vlc-sdl
%if %with_sdl_image
Buildrequires:	SDL_image-devel >= 1.2.10
%endif
BuildRequires: libSDL-devel >= 1.2.10
Buildrequires:	nas-devel

%description plugin-sdl
This plugin adds support for the Simple DirectMedia Layer library to
the VLC media player. To activate it, use the `--vout sdl' or
`--aout sdl' flags or select the `sdl' video or audio output plugin
from the preferences menu.
%endif

%if %with_shout
%package plugin-shout
Summary: Shoutcast and Icecast connector
Group: Sound
Requires: %{name} = %{version}
Buildrequires:	libshout-devel >= 2.1

%description plugin-shout
This plugin adds support for Icecast and Shoutcast servers.
%endif

%package plugin-opengl
Summary: OpenGL video output plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
%description plugin-opengl
This plugin adds support for OpenGL video output to
the VLC media player. 

%if %with_ggi
%package plugin-ggi
Summary: GGI video plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Obsoletes: vlc-ggi
Provides: vlc-ggi
Buildrequires:	libggi-devel

%description plugin-ggi
This is a GGI plugin for the VLC media player. To activate it, use
the `--vout ggi' flag or select the `ggi' video output plugin from
the preferences menu.
%endif

%if %with_svgalib
%package plugin-svgalib
Summary: SVGAlib video plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Buildrequires:	svgalib-devel

%description plugin-svgalib
This plugin adds support for SVGAlib to the VLC media player. To
activate it, use the `--vout svgalib' flag or select the `svgalib' video
output plugin from the preferences menu. Note that you will need root
permissions to use SVGAlib.
%endif


#
# visualization plugins

%if %with_xosd
%package plugin-xosd
Summary: X On-Screen Display plugin for the VLC media player
Group: Video
Buildrequires:	libxosd-devel >= 2
Requires: %{name} = %{version}
%description plugin-xosd
This is an On-Screen Display plugin for the VLC media player. To activate
it, use the `--extraintf xosd' flag or select the `xosd' interface plugin
from the preferences menu.
%endif

%if %with_goom
%package plugin-goom
Summary: Visualization plugin for the VLC media player
Group: Video
BuildRequires: libgoom2-devel
Requires: %{name} = %{version}
%description plugin-goom
This is a visualization plugin for VLC media player based on the Goom library.
%endif

%if %with_projectm
%package plugin-projectm
Summary: Visualization plugin for the VLC media player
Group: Video
BuildRequires: libprojectm-devel
Requires: %{name} = %{version}
%description plugin-projectm
This is a visualization plugin for VLC media player based on projectm.
%endif

%if %with_theora
%package plugin-theora
Summary: Theora video codec for the VLC media player
Group: Video
Requires: %{name} = %{version}
Buildrequires:	libtheora-devel

%description plugin-theora
These plugin adds support for the Ogg Theora video format to the VLC
media player. They are autodetected.
%endif

%if %with_twolame
%package plugin-twolame
Summary: MP2 encoder plugin for VLC
Group: Sound
Requires: %{name} = %{version}
BuildRequires:  libtwolame-devel

%description plugin-twolame
These plugins add support for the Twolame MPEG Audio Layer 2 encoder
to the VLC media player. They are autodetected.
%endif

%if %with_fluidsynth
%package plugin-fluidsynth
Summary: Add MIDI playback support to VLC based on Fluidsynth
Group: Sound
Requires: %{name} = %{version}
BuildRequires: libfluidsynth-devel

%description plugin-fluidsynth
This plugin adds support for MIDI playback to VLC based on the Fluidsynth
library.
%endif

%if %with_gme
%package plugin-gme
Summary: Add game music playback support to VLC based on libgme
Group: Sound
Requires: %{name} = %{version}
BuildRequires: libgme-devel

%description plugin-gme
This plugin adds support for video game music playback to VLC based on the
GME library.
%endif

%if %with_schroedinger
%package plugin-schroedinger
Summary: Dirac plugin for VLC based on Schroedinger
Group: Video
Requires: %{name} = %{version}
BuildRequires: libschroedinger-devel >= 1.0.6

%description plugin-schroedinger
These plugins add support for the Dirac video format based on Schroedinger.
to the VLC media player.
%endif

%package plugin-speex
Summary: Ogg Speex codec plugin for the VLC media player
Group: Sound
Requires: %{name} = %{version}
%description plugin-speex
These plugins add support for the Ogg Speex codec to the VLC media
player. They are autodetected.


%package plugin-flac
Summary: Flac codec plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
%description plugin-flac
These plugins add support for the FLAC compressed audio format to the
VLC media player.

%if %with_dv
%package plugin-dv
Summary: DV codec plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Buildrequires:	libdv-devel
%if %mdvver >= 201000
BuildRequires:  libraw1394-devel >= 2.0.1
BuildRequires:  libdc1394-devel >= 2.1.0
%endif
BuildRequires:  libavc1394-devel >= 0.5.3

%description plugin-dv
This plugin adds support for the DV video format to the VLC media player.
The plugin is autodetected.
%endif

%package plugin-mod
Summary: MOD audio decoder plugin for the VLC media player
Group: Sound
Requires: %{name} = %{version}
%description plugin-mod
This plugin adds support for music module playback based on libmodplug
to the VLC media player.

%package plugin-mpc
Summary: MPC audio decoder plugin for the VLC media player
Group: Sound
Requires: %{name} = %{version}
%description plugin-mpc
This plugin adds support for Musepack audio playback based on libmpcdec
to the VLC media player.

#
# audio plugins
%if %with_pulse
%package plugin-pulse
Summary: PulseAudio plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Obsoletes: vlc-pulse
Provides: vlc-pulse
%description plugin-pulse
This plugin adds support for the PulseAudio Sound Daemon to the VLC
media player. To activate it, use the `--aout pulse' flag or select the
`pulse' audio output plugin from the preferences menu.
%endif

%package plugin-jack
Summary: Jack audio plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
Obsoletes: vlc-jack
Provides: vlc-jack
%description plugin-jack
This plugin adds support for the Jack Audio Connection Kit to the VLC
media player. To activate it, use the `--aout jack' flag or select the
`jack' audio output plugin from the preferences menu.

%package plugin-bonjour
Summary: Bonjour service discovery plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
%description plugin-bonjour
This plugin adds support for Bonjour service discovery to
the VLC media player.

%if %with_upnp
%package plugin-upnp
Summary: UPNP service discovery plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
BuildRequires: libupnp-devel
%description plugin-upnp
This plugin adds support for UPNP service discovery to
the VLC media player.
%endif

%package plugin-gnutls
Summary: Secure Socket Layer plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
%description plugin-gnutls
This plugin adds support for SSL/TLS to the VLC media player.

%package plugin-libnotify
Summary: Notification popup plugin for the VLC media player
Group: Video
Requires: %{name} = %{version}
%description plugin-libnotify
This plugin adds support for notification popup messages to
the VLC media player.


%prep
%if %snapshot
%setup -q -n %name
%else
%setup -q -n %fname
%endif
#gw if we want to regenerate libtool, we must remove the local versions of
# the libtool m4 files, aclocal will replace them
cd m4
rm -fv argz.m4 libtool.m4 ltdl.m4 ltoptions.m4 ltsugar.m4 ltversion.m4 lt~obsolete.m4
cd ..
perl -pi -e "s^/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf^/usr/share/fonts/TTF/VeraBd.ttf^" modules/misc/freetype.c
%patch16 -p1
%if %mdvver >= 200910
%patch18 -p1
%endif
%if %mdvver >= 201010
%patch19 -p1
%endif
%if %snapshot
./bootstrap
%endif
#gw we always need to call libtoolize to replace Debian's libtool
#we get this error on 2011.0 and 2010.0, but not on 2010.1
##libtool: Version mismatch error.  This is libtool 2.2.6b Debian-2.2.6b-2, but the
##libtool: definition of this LT_INIT comes from libtool 2.2.10.
##libtool: You should recreate aclocal.m4 with macros from libtool 2.2.6b Debian-2.2.6b-2
##libtool: and run autoconf again.
libtoolize --install --force
aclocal -I m4 
autoheader
autoconf 
automake

%build
# gw flags for the mozilla build 
export CPPFLAGS="$CPPFLAGS -DOJI -DMOZ_X11"
# add missing ebml include dir
export CPPFLAGS="$CPPFLAGS -I/usr/include/ebml"
#gw the speex headers have moved
export CPPFLAGS="$CPPFLAGS -I%_includedir/speex"
%configure2_5x --enable-pvr --disable-dependency-tracking \
  --disable-sse \
%if %with_bonjour
	--enable-bonjour \
%else
	--disable-bonjour \
%endif
%if %with_smb
	--enable-smb \
%else
	--disable-smb \
%endif
%if %with_xulrunner
	--enable-mozilla \
%else
	--disable-mozilla \
%endif
%if %with_ncurses
	--enable-ncurses \
%endif
%if %with_lirc
	--enable-lirc \
%endif
	--enable-xvideo \
%if %with_fb
	--enable-fb \
%else
	--disable-fb \
%endif
%if %with_aa
	--enable-aa \
%endif
%if %with_sdl
	--enable-sdl \
%endif
%if %with_ggi
	--enable-ggi \
%endif
%if %with_svgalib
        --enable-svgalib \
%endif
%if %with_xosd
	--enable-xosd \
%else
	--disable-xosd \
%endif
%if %with_mad
        --enable-mad \
%endif  
%if %with_ogg
	--enable-vorbis \
	--enable-ogg \
%else
	--disable-vorbis \
	--disable-ogg \
%endif
%if %with_theora
	--enable-theora \
%endif
%if %with_speex
	--enable-speex \
%else
	--disable-speex \
%endif
%if %with_flac
	--enable-flac \
%else
	--disable-flac \
%endif
%if %with_mkv
	--enable-mkv \
%else
	--disable-mkv \
%endif	
%if %with_dv
	--enable-dv \
%else
	--disable-dv \
%endif
%if %with_dvbpsi
	--enable-dvbpsi \
%else
	--disable-dvbpsi \
%endif
%if %with_shout
        --enable-shout \
%endif
%if %with_dvb
	--enable-dvb \
%if %with_satellite
--enable-satellite \
%endif
%else
	--disable-dvb --disable-satellite \
%endif
%if %with_pulse
	--enable-pulse \
%endif
%if %with_jack
	--enable-jack \
%endif
%if %with_alsa
	--enable-alsa \
%endif
%if %with_mpeg2dec
	--enable-libmpeg2 \
%else
	--disable-libmpeg2 \
%endif
%if %with_faad
	--enable-faad \
%endif
%if %with_dts
	--enable-dca \
%else
	--disable-dca \
%endif
%if ! %with_svlc
	--disable-skins2 \
%endif
%if ! %with_dvdnav
	--disable-dvdnav \
%endif
%if %with_live
	--enable-live555 --with-live555-tree=%_libdir/live \
%endif
        --enable-v4l \
%if %with_gnutls
	--enable-gnutls \
%endif
	--disable-rpath \
%if %with_vcd
	--enable-vcdx \
%endif
%if %with_cddb
	--enable-libcddb \
%else
	--disable-libcddb \
%endif
%if %with_x264
	--enable-x264 \
%else
	--disable-x264 \
%endif
%if %with_loader
	--enable-loader \
%endif
%if %with_twolame
	--enable-twolame \
%endif
%ifarch x86_64
        --with-pic
%endif

%make

%install
rm -rf %buildroot
mkdir -p %buildroot%_libdir
%makeinstall_std transform=""
find %buildroot%_libdir/vlc -name \*.la -exec rm -f {} \;
rm -f %buildroot%_libdir/mozilla/plugins/libvlcplugin.la
%find_lang %name
install -d %buildroot/%_mandir/man1
install doc/vlc.1 %buildroot/%_mandir/man1
install doc/vlc-config.1 %buildroot/%_mandir/man1
rm -rf installed-docs
mv %buildroot%_datadir/doc/vlc installed-docs
%if ! %with_svlc
rm -rf %buildroot%_datadir/vlc/skin*
%endif
# menu

desktop-file-install --vendor="" \
  --add-mime-type="x-content/video-dvd" \
  --add-mime-type="x-content/video-vcd" \
  --add-mime-type="x-content/video-svcd" \
  --add-mime-type="x-content/audio-cdda" \
  --add-category="Qt" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%if %with_svlc
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-svlc.desktop << EOF
[Desktop Entry]
Name=VLC skinned GUI media player
Comment=VLC is a free MPEG, MPEG2, DVD and DivX player
Exec=%{_bindir}/svlc %U
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;Audio;Video;Player;
EOF
fgrep MimeType= %buildroot%_datadir/applications/vlc.desktop >> %buildroot%{_datadir}/applications/mandriva-svlc.desktop
%endif

# icons
%define pngdir share/icons
mkdir -p %{buildroot}/{%{_miconsdir},%{_liconsdir}}
install -m 644 %pngdir/16x16/vlc.png %buildroot/%_miconsdir/vlc.png
install -m 644 %pngdir/32x32/vlc.png %buildroot/%_iconsdir/vlc.png
install -m 644 %pngdir/48x48/vlc.png %buildroot/%_liconsdir/vlc.png

%clean
rm -fr %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README COPYING AUTHORS THANKS
%doc installed-docs/* doc/lirc/
%_bindir/cvlc
%_bindir/qvlc
%_bindir/vlc
%_bindir/vlc-wrapper
%dir %_datadir/vlc/
%_datadir/vlc/*.*
%_datadir/vlc/http
%_datadir/vlc/osdmenu/
%_datadir/vlc/utils
%dir %_libdir/vlc
%_libdir/vlc/vlc-cache-gen

%dir %_libdir/vlc/plugins

%dir %_libdir/vlc/plugins/3dnow
%_libdir/vlc/plugins/3dnow/libmemcpy3dn_plugin.so


%dir %_libdir/vlc/plugins/access
%_libdir/vlc/plugins/access/libaccess_alsa_plugin.so
%_libdir/vlc/plugins/access/libaccess_attachment_plugin.so
%_libdir/vlc/plugins/access/libaccess_avio_plugin.so
%_libdir/vlc/plugins/access/libaccess_bd_plugin.so
%if %with_dvdnav
%_libdir/vlc/plugins/access/libdvdnav_plugin.so*
%endif
%_libdir/vlc/plugins/access/libaccess_gnomevfs_plugin.so
%_libdir/vlc/plugins/access/libaccess_imem_plugin.so
%_libdir/vlc/plugins/access/libaccess_mmap_plugin.so
%if %with_mtp
%_libdir/vlc/plugins/access/libaccess_mtp_plugin.so
%_libdir/vlc/plugins/services_discovery/libmtp_plugin.so
%endif
%_libdir/vlc/plugins/access/libaccess_oss_plugin.so
#%_libdir/vlc/plugins/access/libaccess_rtmp_plugin.so
%_libdir/vlc/plugins/access/libcdda_plugin.so*
#%_libdir/vlc/plugins/access/libaccess_directory_plugin.so*
%_libdir/vlc/plugins/access/libaccess_fake_plugin.so*
#%_libdir/vlc/plugins/access/libaccess_file_plugin.so*
%_libdir/vlc/plugins/access/libaccess_ftp_plugin.so*
%_libdir/vlc/plugins/access/libaccess_http_plugin.so*
%_libdir/vlc/plugins/access/libaccess_mms_plugin.so*
%if %with_smb
%_libdir/vlc/plugins/access/libaccess_smb_plugin.so*
%endif
%_libdir/vlc/plugins/access/libaccess_tcp_plugin.so*
%_libdir/vlc/plugins/access/libaccess_udp_plugin.so*
%if %with_dvb
%_libdir/vlc/plugins/access/libdvb_plugin.so*
%endif
%_libdir/vlc/plugins/access/libfilesystem_plugin.so
%_libdir/vlc/plugins/access/librtp_plugin.so
%if %mdvver < 201100
%_libdir/vlc/plugins/access/libv4l_plugin.so*
%endif
%_libdir/vlc/plugins/access/libv4l2_plugin.so*
%_libdir/vlc/plugins/access/libdvdread_plugin.so*
%_libdir/vlc/plugins/access/libpvr_plugin.so
%if %with_vcd
%_libdir/vlc/plugins/access/libvcdx_plugin.so*
%endif
%_libdir/vlc/plugins/access/libvcd_plugin.so*
%_libdir/vlc/plugins/access/libxcb_screen_plugin.so
%_libdir/vlc/plugins/access/libzip_plugin.so


%dir %_libdir/vlc/plugins/access_output/
%_libdir/vlc/plugins/access_output/libaccess_output_dummy_plugin.so*
%_libdir/vlc/plugins/access_output/libaccess_output_file_plugin.so*
%_libdir/vlc/plugins/access_output/libaccess_output_http_plugin.so*
#%_libdir/vlc/plugins/access_output/libaccess_output_rtmp_plugin.so
%_libdir/vlc/plugins/access_output/libaccess_output_udp_plugin.so*

%dir %_libdir/vlc/plugins/audio_filter
%_libdir/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
%_libdir/vlc/plugins/audio_filter/libaudio_format_plugin.so*
%_libdir/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%_libdir/vlc/plugins/audio_filter/libconverter_fixed_plugin.so
#%_libdir/vlc/plugins/audio_filter/libconverter_float_plugin.so
%if %with_dts
%_libdir/vlc/plugins/audio_filter/libdtstofloat32_plugin.so*
%endif
%_libdir/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so*
%_libdir/vlc/plugins/audio_filter/libdtstospdif_plugin.so*
%_libdir/vlc/plugins/audio_filter/libequalizer_plugin.so*
%_libdir/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so*
#%_libdir/vlc/plugins/audio_filter/liblinear_resampler_plugin.so*
%_libdir/vlc/plugins/audio_filter/libmono_plugin.so
%if %with_mad
%_libdir/vlc/plugins/audio_filter/libmpgatofixed32_plugin.so*
%endif
%_libdir/vlc/plugins/audio_filter/libnormvol_plugin.so*
%_libdir/vlc/plugins/audio_filter/libparam_eq_plugin.so*
%_libdir/vlc/plugins/audio_filter/libscaletempo_plugin.so
%_libdir/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so*
%_libdir/vlc/plugins/audio_filter/libspatializer_plugin.so
%_libdir/vlc/plugins/audio_filter/libtrivial_channel_mixer_plugin.so*
#%_libdir/vlc/plugins/audio_filter/libtrivial_resampler_plugin.so*
%_libdir/vlc/plugins/audio_filter/libugly_resampler_plugin.so*

%dir %_libdir/vlc/plugins/audio_mixer
%_libdir/vlc/plugins/audio_mixer/libfloat32_mixer_plugin.so*
%_libdir/vlc/plugins/audio_mixer/libspdif_mixer_plugin.so*
%_libdir/vlc/plugins/audio_mixer/libtrivial_mixer_plugin.so*

%dir %_libdir/vlc/plugins/audio_output
%_libdir/vlc/plugins/audio_output/libaout_file_plugin.so*
%_libdir/vlc/plugins/audio_output/liboss_plugin.so*
%_libdir/vlc/plugins/audio_output/libportaudio_plugin.so*

%dir %_libdir/vlc/plugins/codec
%if %with_a52
%_libdir/vlc/plugins/codec/liba52_plugin.so*
%_libdir/vlc/plugins/audio_filter/liba52tofloat32_plugin.so*
%_libdir/vlc/plugins/audio_filter/liba52tospdif_plugin.so*
%endif
%_libdir/vlc/plugins/codec/libadpcm_plugin.so*
%_libdir/vlc/plugins/codec/libaes3_plugin.so
%_libdir/vlc/plugins/codec/libaraw_plugin.so*
%_libdir/vlc/plugins/codec/libavcodec_plugin.so
%_libdir/vlc/plugins/codec/libcc_plugin.so
%_libdir/vlc/plugins/codec/libcdg_plugin.so
#%_libdir/vlc/plugins/codec/libcmml_plugin.so*
%_libdir/vlc/plugins/codec/libcvdsub_plugin.so*
%_libdir/vlc/plugins/codec/libdirac_plugin.so
%_libdir/vlc/plugins/codec/libfake_plugin.so*
%_libdir/vlc/plugins/codec/libinvmem_plugin.so
%_libdir/vlc/plugins/codec/librawvideo_plugin.so*
%_libdir/vlc/plugins/codec/libsubsusf_plugin.so
%_libdir/vlc/plugins/codec/libsvcdsub_plugin.so*
%_libdir/vlc/plugins/codec/libt140_plugin.so
%_libdir/vlc/plugins/codec/libdts_plugin.so*
%_libdir/vlc/plugins/codec/liblpcm_plugin.so*
%_libdir/vlc/plugins/codec/liblibmpeg2_plugin.so*
%_libdir/vlc/plugins/codec/libmpeg_audio_plugin.so*
%_libdir/vlc/plugins/codec/libpng_plugin.so*
%_libdir/vlc/plugins/codec/libsubsdec_plugin.so*
%if %with_x264
%_libdir/vlc/plugins/codec/libx264_plugin.so*
%endif
%_libdir/vlc/plugins/codec/libspudec_plugin.so*
%_libdir/vlc/plugins/codec/libdvbsub_plugin.so*
%if %with_faad
%_libdir/vlc/plugins/codec/libfaad_plugin.so*
%endif
%if %with_loader
%_libdir/vlc/plugins/codec/libdmo_plugin.so*
%endif
%_libdir/vlc/plugins/codec/libtelx_plugin.so
%dir %_libdir/vlc/plugins/control
%_libdir/vlc/plugins/control/libdbus_plugin.so
%_libdir/vlc/plugins/control/libglobalhotkeys_plugin.so
%_libdir/vlc/plugins/control/libhotkeys_plugin.so*
%_libdir/vlc/plugins/control/liboldhttp_plugin.so*
%_libdir/vlc/plugins/control/libmotion_plugin.so
%_libdir/vlc/plugins/control/libnetsync_plugin.so
%_libdir/vlc/plugins/control/liboldrc_plugin.so*
#%_libdir/vlc/plugins/control/libshowintf_plugin.so*
%_libdir/vlc/plugins/control/libsignals_plugin.so
%_libdir/vlc/plugins/control/liboldtelnet_plugin.so*
%_libdir/vlc/plugins/control/libgestures_plugin.so*

%dir %_libdir/vlc/plugins/demux
%_libdir/vlc/plugins/demux/libaiff_plugin.so*
%_libdir/vlc/plugins/demux/libasf_plugin.so*
%_libdir/vlc/plugins/demux/libau_plugin.so*
%_libdir/vlc/plugins/demux/libavformat_plugin.so
%_libdir/vlc/plugins/demux/libavi_plugin.so*
%_libdir/vlc/plugins/demux/libdemux_cdg_plugin.so
%_libdir/vlc/plugins/demux/libdemuxdump_plugin.so*
%_libdir/vlc/plugins/demux/libdirac_plugin.so
%_libdir/vlc/plugins/demux/libes_plugin.so
%_libdir/vlc/plugins/demux/libh264_plugin.so*
%if %with_live
%_libdir/vlc/plugins/demux/liblive555_plugin.so
%endif
#%_libdir/vlc/plugins/demux/libm4v_plugin.so*
%_libdir/vlc/plugins/demux/libmjpeg_plugin.so*
%_libdir/vlc/plugins/demux/libmkv_plugin.so
%_libdir/vlc/plugins/demux/libmp4_plugin.so*
%_libdir/vlc/plugins/demux/libmpgv_plugin.so*
%_libdir/vlc/plugins/demux/libnsc_plugin.so*
%_libdir/vlc/plugins/demux/libnsv_plugin.so*
%_libdir/vlc/plugins/demux/libnuv_plugin.so*
%_libdir/vlc/plugins/demux/libplaylist_plugin.so*
%_libdir/vlc/plugins/demux/libps_plugin.so*
%_libdir/vlc/plugins/demux/libpva_plugin.so*
%_libdir/vlc/plugins/demux/librawaud_plugin.so
%_libdir/vlc/plugins/demux/librawdv_plugin.so*
%_libdir/vlc/plugins/demux/librawvid_plugin.so
%_libdir/vlc/plugins/demux/libreal_plugin.so*
%_libdir/vlc/plugins/demux/libsmf_plugin.so
%_libdir/vlc/plugins/demux/libsubtitle_plugin.so*
%_libdir/vlc/plugins/demux/libtta_plugin.so
%_libdir/vlc/plugins/demux/libty_plugin.so*
%_libdir/vlc/plugins/demux/libvobsub_plugin.so*
%_libdir/vlc/plugins/demux/libvc1_plugin.so
%_libdir/vlc/plugins/demux/libvoc_plugin.so*
%_libdir/vlc/plugins/demux/libwav_plugin.so*
%if %with_dvbpsi
%_libdir/vlc/plugins/demux/libts_plugin.so*
%endif
%_libdir/vlc/plugins/demux/libxa_plugin.so*
%if %with_ogg
%_libdir/vlc/plugins/demux/libogg_plugin.so*
%_libdir/vlc/plugins/codec/libvorbis_plugin.so*
%endif
%if %with_satellite
%_libdir/vlc/plugins/access/libsatellite_plugin.so*
%endif
%dir %_libdir/vlc/plugins/meta_engine
%_libdir/vlc/plugins/meta_engine/libfolder_plugin.so
%if %with_taglib
%_libdir/vlc/plugins/meta_engine/libtaglib_plugin.so
%endif
%dir %_libdir/vlc/plugins/misc
%_libdir/vlc/plugins/misc/libaudioscrobbler_plugin.so
%_libdir/vlc/plugins/misc/libdummy_plugin.so*
%_libdir/vlc/plugins/misc/libexport_plugin.so*
%_libdir/vlc/plugins/misc/libfreetype_plugin.so*
%_libdir/vlc/plugins/misc/libinhibit_plugin.so
%_libdir/vlc/plugins/misc/liblogger_plugin.so*
#%_libdir/vlc/plugins/misc/libmemcpy*_plugin.so*
%_libdir/vlc/plugins/misc/libosd_parser_plugin.so
#%_libdir/vlc/plugins/misc/libscreensaver_plugin.so*
%_libdir/vlc/plugins/misc/libstats_plugin.so
%_libdir/vlc/plugins/misc/libsqlite_plugin.so
%_libdir/vlc/plugins/misc/libsvg_plugin.so
%_libdir/vlc/plugins/misc/libtelepathy_plugin.so
%_libdir/vlc/plugins/misc/libvod_rtsp_plugin.so*
%_libdir/vlc/plugins/misc/libxdg_screensaver_plugin.so*
%if %with_xml
%_libdir/vlc/plugins/misc/libxml_plugin.so*
%endif
%_libdir/vlc/plugins/misc/libxscreensaver_plugin.so
%_libdir/vlc/plugins/misc/libxtag_plugin.so*

%dir %_libdir/vlc/plugins/mmx
%_libdir/vlc/plugins/mmx/libi420_rgb_mmx_plugin.so
%_libdir/vlc/plugins/mmx/libi420_yuy2_mmx_plugin.so
%_libdir/vlc/plugins/mmx/libi422_yuy2_mmx_plugin.so
%_libdir/vlc/plugins/mmx/libmemcpymmx_plugin.so

%dir %_libdir/vlc/plugins/mmxext
%_libdir/vlc/plugins/mmxext/libmemcpymmxext_plugin.so

%dir %_libdir/vlc/plugins/mux
%_libdir/vlc/plugins/mux/libmux_asf_plugin.so*
%_libdir/vlc/plugins/mux/libmux_avi_plugin.so*
%_libdir/vlc/plugins/mux/libmux_dummy_plugin.so*
%_libdir/vlc/plugins/mux/libmux_mp4_plugin.so*
%_libdir/vlc/plugins/mux/libmux_mpjpeg_plugin.so*
%if %with_ogg
%_libdir/vlc/plugins/mux/libmux_ogg_plugin.so*
%endif
%_libdir/vlc/plugins/mux/libmux_ps_plugin.so*
%_libdir/vlc/plugins/mux/libmux_ts_plugin.so
%_libdir/vlc/plugins/mux/libmux_wav_plugin.so*
%dir %_libdir/vlc/plugins/gui/
%_libdir/vlc/plugins/gui/libqt4_plugin.so
%dir %_libdir/vlc/plugins/packetizer
%_libdir/vlc/plugins/packetizer/libpacketizer_copy_plugin.so*
%_libdir/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
%_libdir/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%_libdir/vlc/plugins/packetizer/libpacketizer_h264_plugin.so*
%_libdir/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%_libdir/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so*
%_libdir/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so*
%_libdir/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so*
%_libdir/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so

%dir %_libdir/vlc/plugins/services_discovery/
%_libdir/vlc/plugins/services_discovery/libmediadirs_plugin.so
%_libdir/vlc/plugins/services_discovery/libpodcast_plugin.so*
%_libdir/vlc/plugins/services_discovery/libsap_plugin.so*
#%_libdir/vlc/plugins/services_discovery/libshout_plugin.so*
%if %with_udev
%_libdir/vlc/plugins/services_discovery/libudev_plugin.so*
%endif
%_libdir/vlc/plugins/services_discovery/libxcb_apps_plugin.so

#%dir %_libdir/vlc/plugins/sse2/
#%_libdir/vlc/plugins/sse2/libi420_rgb_sse2_plugin.so
#%_libdir/vlc/plugins/sse2/libi420_yuy2_sse2_plugin.so
#%_libdir/vlc/plugins/sse2/libi422_yuy2_sse2_plugin.so

%dir %_libdir/vlc/plugins/stream_filter/
%_libdir/vlc/plugins/stream_filter/libdecomp_plugin.so
%_libdir/vlc/plugins/stream_filter/libstream_filter_rar_plugin.so
%_libdir/vlc/plugins/stream_filter/libstream_filter_record_plugin.so

%dir %_libdir/vlc/plugins/stream_out
%_libdir/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%_libdir/vlc/plugins/stream_out/libstream_out_bridge_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_description_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_display_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_dummy_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_es_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_gather_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_raop_plugin.so
%_libdir/vlc/plugins/stream_out/libstream_out_record_plugin.so
%_libdir/vlc/plugins/stream_out/libstream_out_rtp_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_smem_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_standard_plugin.so*
%_libdir/vlc/plugins/stream_out/libstream_out_transcode_plugin.so*

%dir %_libdir/vlc/plugins/video_chroma
%_libdir/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%_libdir/vlc/plugins/video_chroma/libi420_rgb_*plugin.so*
#%_libdir/vlc/plugins/video_chroma/libi420_ymga_*plugin.so*
%_libdir/vlc/plugins/video_chroma/libi420_yuy2_*plugin.so*
%_libdir/vlc/plugins/video_chroma/libi422_i420_plugin.so
%_libdir/vlc/plugins/video_chroma/libi422_yuy2_*plugin.so*
%_libdir/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%_libdir/vlc/plugins/video_chroma/libyuy2_i422_plugin.so


%dir %_libdir/vlc/plugins/video_filter
%_libdir/vlc/plugins/video_filter/libadjust_plugin.so*
%_libdir/vlc/plugins/video_filter/libalphamask_plugin.so
%_libdir/vlc/plugins/video_filter/libaudiobargraph_v_plugin.so
%_libdir/vlc/plugins/video_filter/libatmo_plugin.so
%_libdir/vlc/plugins/video_filter/libball_plugin.so
%_libdir/vlc/plugins/video_filter/libblendbench_plugin.so
%_libdir/vlc/plugins/video_filter/libblend_plugin.so*
%_libdir/vlc/plugins/video_filter/libbluescreen_plugin.so
%_libdir/vlc/plugins/video_filter/libcanvas_plugin.so
%_libdir/vlc/plugins/video_filter/libchain_plugin.so
%_libdir/vlc/plugins/video_filter/libclone_plugin.so*
%_libdir/vlc/plugins/video_filter/libcolorthres_plugin.so
%_libdir/vlc/plugins/video_filter/libcroppadd_plugin.so
%_libdir/vlc/plugins/video_filter/libcrop_plugin.so*
%_libdir/vlc/plugins/video_filter/libdeinterlace_plugin.so*
%_libdir/vlc/plugins/video_filter/libdynamicoverlay_plugin.so
%_libdir/vlc/plugins/video_filter/liberase_plugin.so
%_libdir/vlc/plugins/video_filter/libextract_plugin.so
%_libdir/vlc/plugins/video_filter/libgaussianblur_plugin.so
%_libdir/vlc/plugins/video_filter/libgradient_plugin.so
%_libdir/vlc/plugins/video_filter/libgrain_plugin.so
%_libdir/vlc/plugins/video_filter/libinvert_plugin.so*
%_libdir/vlc/plugins/video_filter/liblogo_plugin.so*
%_libdir/vlc/plugins/video_filter/libmagnify_plugin.so*
%_libdir/vlc/plugins/video_filter/libmarq_plugin.so*
%_libdir/vlc/plugins/video_filter/libmirror_plugin.so
%_libdir/vlc/plugins/video_filter/libmosaic_plugin.so*
%_libdir/vlc/plugins/video_filter/libmotionblur_plugin.so*
%_libdir/vlc/plugins/video_filter/libmotiondetect_plugin.so*
%_libdir/vlc/plugins/video_filter/libnoise_plugin.so
%_libdir/vlc/plugins/video_filter/libosdmenu_plugin.so*
%if %with_xcb_randr
%_libdir/vlc/plugins/video_filter/libpanoramix_plugin.so
%endif
%_libdir/vlc/plugins/video_filter/libpostproc_plugin.so
%_libdir/vlc/plugins/video_filter/libpsychedelic_plugin.so
%_libdir/vlc/plugins/video_filter/libpuzzle_plugin.so
%_libdir/vlc/plugins/video_filter/libremoteosd_plugin.so
%_libdir/vlc/plugins/video_filter/libripple_plugin.so
%_libdir/vlc/plugins/video_filter/librotate_plugin.so
%_libdir/vlc/plugins/video_filter/librss_plugin.so*
%_libdir/vlc/plugins/video_filter/librv32_plugin.so*
%_libdir/vlc/plugins/video_filter/libscale_plugin.so*
%_libdir/vlc/plugins/video_filter/libscene_plugin.so
%_libdir/vlc/plugins/video_filter/libsharpen_plugin.so
%_libdir/vlc/plugins/video_filter/libswscale_plugin.so
%_libdir/vlc/plugins/video_filter/libtransform_plugin.so*
%_libdir/vlc/plugins/video_filter/libvideo_filter_wrapper_plugin.so
%_libdir/vlc/plugins/video_filter/libwall_plugin.so*
%_libdir/vlc/plugins/video_filter/libwave_plugin.so
%_libdir/vlc/plugins/video_filter/libyuvp_plugin.so

%dir %_libdir/vlc/plugins/video_output
%_libdir/vlc/plugins/video_output/libcaca_plugin.so
%if %with_fb
%_libdir/vlc/plugins/video_output/libfb_plugin.so*
%endif
%_libdir/vlc/plugins/video_output/libvmem_plugin.so
%_libdir/vlc/plugins/video_output/libyuv_plugin.so
%_libdir/vlc/plugins/video_output/libvout_wrapper_plugin.so
%_libdir/vlc/plugins/video_output/libxcb_x11_plugin.so*
%_libdir/vlc/plugins/video_output/libxcb_window_plugin.so*
%if %with_xvideo
%_libdir/vlc/plugins/video_output/libxcb_xv_plugin.so*
%endif

%dir %_libdir/vlc/plugins/visualization
%_libdir/vlc/plugins/visualization/libvisual_plugin.so*
%if %with_alsa
%_libdir/vlc/plugins/audio_output/libalsa_plugin.so*
%endif
%_mandir/man1/vlc.*
%_mandir/man1/vlc-wrapper.1*
%_datadir/applications/vlc.desktop
%_miconsdir/vlc.png
%_iconsdir/vlc.png
%_liconsdir/vlc.png
%_iconsdir/hicolor/*/apps/*
%if %with_kde
%_datadir/apps/solid/actions/*.desktop
%endif

%files -n %libname
%defattr(-,root,root)
%_libdir/libvlc.so.%{libmajor}*

%files -n %libnamecore
%defattr(-,root,root)
%_libdir/libvlccore.so.%{coremajor}*

%files -n %develname
%defattr(-,root,root)
%doc README doc/release-howto.txt doc/skins
%dir %_includedir/vlc
%_libdir/libvlc.so
%_libdir/libvlccore.so
%_includedir/vlc/*
%attr(644,root,root) %_libdir/*.la
%_mandir/man1/vlc-config*
%_libdir/pkgconfig/*

%if %with_shout
%files plugin-shout
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%endif

%if %with_xulrunner
%files -n mozilla-plugin-vlc
%defattr(-,root,root)
%doc README
%_datadir/vlc/mozilla
%_libdir/mozilla/plugins/libvlcplugin.so
%endif

# intf plugins
%if %with_svlc
%files -n svlc
%defattr(-,root,root)
%doc README
%_bindir/svlc
%_libdir/vlc/plugins/gui/libskins2_plugin.so*
%_datadir/applications/mandriva-svlc.desktop
%_datadir/vlc/skins2
%endif

%if %with_zvbi
%files plugin-zvbi
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libzvbi_plugin.so
%endif

%if %with_kate
%files plugin-kate
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libkate_plugin.so
%endif

%if %with_ass
%files plugin-libass
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/liblibass_plugin.so
%endif

%if %with_lua
%files plugin-lua
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/misc/liblua_plugin.so
%_libdir/vlc/lua
%_datadir/vlc/lua
%_bindir/rvlc
%endif

%if %with_ncurses
%files plugin-ncurses
%defattr(-,root,root)
%doc README
%_bindir/nvlc
%_libdir/vlc/plugins/gui/libncurses_plugin.so*
%endif

%if %with_lirc
%files plugin-lirc
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/control/liblirc_plugin.so*
%endif

# video plugins
%if %with_sdl
%files plugin-sdl
%defattr(-,root,root)
%doc README
%if %with_sdl_image
%_libdir/vlc/plugins/codec/libsdl_image_plugin.so*
%endif
%_libdir/vlc/plugins/audio_output/libaout_sdl_plugin.so*
%_libdir/vlc/plugins/video_output/libvout_sdl_plugin.so*
%endif

%files plugin-opengl
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/video_output/libxcb_glx_plugin.so*
#%_libdir/vlc/plugins/video_output/libopengl_plugin.so*

%if %with_ggi
%files plugin-ggi
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/video_output/libggi_plugin.so*
%endif

%if %with_aa
%files plugin-aa
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/video_output/libaa_plugin.so*
%endif

%if %with_svgalib
%files plugin-svgalib
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/video_output/libsvgalib_plugin.so*
%endif

# visualization plugin
%if %with_xosd
%files plugin-xosd
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/misc/libxosd_plugin.so*
%endif

%if %with_goom
%files plugin-goom
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/visualization/libgoom_plugin.so
%endif

%if %with_projectm
%files plugin-projectm
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/visualization/libprojectm_plugin.so
%endif

%if %with_theora
%files plugin-theora
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libtheora_plugin.so
%endif

%if %with_fluidsynth
%files plugin-fluidsynth
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libfluidsynth_plugin.so
%endif

%if %with_gme
%files plugin-gme
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/demux/libgme_plugin.so
%endif

%if %with_schroedinger
%files plugin-schroedinger
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libschroedinger_plugin.so
%endif

%if %with_twolame
%files plugin-twolame
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libtwolame_plugin.so*
%endif

%if %with_speex
%files plugin-speex
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/codec/libspeex_plugin.so*
%endif


%files plugin-flac
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/demux/libflacsys_plugin.so
%_libdir/vlc/plugins/codec/libflac_plugin.so*


%if %with_dv
%files plugin-dv
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/access/libaccess_dv_plugin.so
%_libdir/vlc/plugins/access/libdc1394_plugin.so
%endif

%if %with_mod
%files plugin-mod
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/demux/libmod_plugin.so*
%endif

%if %with_mpc
%files plugin-mpc
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/demux/libmpc_plugin.so*
%endif

#audio plugins
%if %with_pulse
%files plugin-pulse
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/audio_output/libpulse_plugin.so*
%endif


%if %with_jack
%files plugin-jack
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/access/libaccess_jack_plugin.so
%_libdir/vlc/plugins/audio_output/libjack_plugin.so*
%endif

%if %with_bonjour
%files plugin-bonjour
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/services_discovery/libbonjour_plugin.so*
%endif

%if %with_upnp
%files plugin-upnp
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/services_discovery/libupnp_intel_plugin.so*
%endif

%if %with_gnutls
%files plugin-gnutls
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/misc/libgnutls_plugin.so*
%endif

%files plugin-libnotify
%defattr(-,root,root)
%doc README
%_libdir/vlc/plugins/misc/libnotify_plugin.so*
