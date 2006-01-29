Summary:	KPopup - a program for sending and receiving Microsoft(tm) WinPopup messages
Summary(pl):	KPopup - program do wysy³ania i odbierania wiadomo¶ci WinPopup
Name:		kpopup
Version:	0.9.8.2
Release:	3
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.henschelsoft.de/kpopup/%{name}-%{version}.tar.gz
# Source0-md5:	f3cb22df62c4062dd172dd28aa92d4db
Patch0:		%{name}-desktop.patch
URL:		http://www.henschelsoft.de/kpopup_en.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.194
BuildRequires:	unsermake >= 040511
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPopup is a program for sending and receiving Microsoft(tm) WinPopup
messages.

%description -l pl
KPopup jest programem do wysy³ania i odbierania wiadomo¶ci WinPopup.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/kpopup

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<'EOF'
Locate the [global] section of your Samba configuration file (smb.conf)
and add the following line:

message command = sh -c '/usr/bin/receivepopup.sh "%s" "%f"' &
EOF
# 'vim
fi

%files -f kpopup.lang
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(755,root,root) %{_bindir}/kpopup
%attr(755,root,root) %{_bindir}/receivepopup.sh
%{_desktopdir}/kde/kpopup.desktop
%{_iconsdir}/hicolor/*/*/kpopup.png
%dir %attr(777,root,root) /var/lib/kpopup
