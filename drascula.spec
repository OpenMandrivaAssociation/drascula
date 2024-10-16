%define scummvmdir %{_datadir}/scummvm/

Name:		drascula
Version:	1.0
Release:	4
Summary:	The Vampire Strikes Back - Adventure Game
Group:		Games/Adventure
License:	Freeware
URL:		https://wiki.scummvm.org/index.php/Drascula:_The_Vampire_Strikes_Back
Source0:	http://downloads.sourceforge.net/scummvm/%{name}-%{version}.zip
Source1:	http://downloads.sourceforge.net/scummvm/%{name}-int-1.1.zip
Source2:	http://downloads.sourceforge.net/scummvm/drascula-audio-2.0.zip
Source3:	http://github.com/scummvm/scummvm/raw/v1.4.0/dists/engine-data/drascula.dat
BuildRequires:	unzip
BuildArch:	noarch
Requires:	scummvm

%description
You play the role of John Hacker, a British estate agent, who travels to a
small village of Transylvania in order to negotiate the sale of some ground
of Gibraltar with the Count Drascula. 
But unfortunately Hacker is not aware of who is Drascula in reality: the most
terrible vampire with just one idea on his mind: DOMINATING the World
demonstrating that he is even more evil than his brother Vlad.

%prep
%setup -q -n %{name} -c %{name}
unzip -oqqj %{SOURCE1}
unzip -oqqj %{SOURCE2}

%install
%__install -d -m 755 %{buildroot}%{_gamesbindir}
# startscript
%__cat > %{buildroot}%{_gamesbindir}/%{name} <<'EOF'
#!/bin/bash
# Basic switch of language according to locale defined in Unix systems
case "$LC_MESSAGES" in
    de* )
        language="de"
	;;
    es* )
        language="es"
	;;
    fr* )
        language="fr"
	;;
    it* )
        language="it"
	;;
    * )
        language="en"
	;;
esac
scummvm -f -n -m 128 -p %{scummvmdir}/%{name} --language=$language %{name}
EOF

%__chmod 755 %{buildroot}%{_gamesbindir}/%{name}

%__mkdir_p %{buildroot}/%{scummvmdir}/%{name}
%__install -p -m 644 Packet.001 PACKET.00? *.ogg %{buildroot}/%{scummvmdir}/%{name}
%__install -p -m 644 %{SOURCE3} %{buildroot}/%{scummvmdir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Drascula: The Vampire Strikes Back
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;AdventureGame;
EOF

%clean

%files
%doc readme.txt drascula.doc
%{_gamesbindir}/%{name}
%{scummvmdir}/%{name}
%{_datadir}/applications/%{name}.desktop

