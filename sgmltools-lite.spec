%include	/usr/lib/rpm/macros.perl
Summary:	A text formatting package based on SGML
Summary(de):	Textformatierungssystem, das vom Linux Documentation Project benutzt wird
Summary(fr):	Système de formattage de texte utilisé par le Linux Documentation Project
Summary(nl):	Tekstformateringssysteem welke door het Linux Documentatie Project wordt gebruikt
Summary(pl):	Narzêdzia konweruj±ce do linuxdoc-dtd
Summary(tr):	GNU belge biçimlendirme sistemi
Name:		sgmltools-lite
Version:	3.0.2
Release:	0.1
License:	GPL
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/sgmltools-lite/%{name}-%{version}.tar.gz
# Source0-md5:	9f88d015eacf4c1be33711723b53ac43
Source1:	sgml2info.1.pl
Source2:	sgml2txt.1.pl
Patch0:		%{name}-Makefile.in.patch
Patch1:		%{name}-configure.patch

URL:		http://sgmltools-lite.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	groff
BuildRequires:	openjade
Requires:	/usr/bin/nsgmls
Requires:	sgmls
Requires:	sgml-common
Obsoletes:	linuxdoc-sgml
Obsoletes:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGMLtools is a text formatting package based on SGML (Standard
Generalized Markup Language). SGMLtools allows you to produce LaTeX,
HTML, GNU info, LyX, RTF, plain text (via groff), and other format
outputs from a single SGML source. SGMLtools is intended for writing
technical software documentation.

%description -l de
SGMLtools ist ein Textformatierer auf SGML-Basis, der eine Vielzahl
von Ausgabeformaten erzeugen kann. Sie können aus einer einzigen
SGML-Quelldatei PostScript-, dvi- (mit LaTeX), Nur-Text- (mit groff),
HTML- und texinfo-Dateien erstellen.

%description -l fr
SGMLtools est un formatteur de texte basé sur SGML qui vous permet de
produire de nombreux formats de fichiers de sortie. vous pouvez créer
du PostScript et du dvi (avec LaTeX), du texte simple (avec groff), du
HTML, et des fichiers texinfo depuis un simple fichier SGML.

%description -l pl
SGMLtools jest bazuj±cym na SGML (a dok³adniej na LinuxDoc) pakietem
s³u¿±cym do formatowania tekstu. Wchodz±ce w sk³ad pakietu narzêdzia
pozwalaj± na wygenerowanie ze ¼ród³a w SGML dokumentów w formatach
LaTeX, HTML, GNU info, LyX, RTF, tekstowym (przy u¿yciu groff-a).
SGMLtools przeznaczone s± do pisania dokumentacji technicznej
oprogramowania.

%description -l tr
SGMLtools, SGML tabanlý deðiþik biçimlerde çýktýlar üretmenizi
saðlayan bir metin biçimleyicisidir. PostScript, dvi (LaTeX ile), düz
metin (groff ile), HTML dosyalarýný tek bir SGML kaynak dosyasýndan
yaratabilirsiniz.

%description -l nl
SGMLtools is een op SGML gebaseerd tekstverwerkingssyteem waarmee een
aantal verschillende andere bestanden kan worden gemaakt. Uitvoer is
mogelijk in: ASCII, DVI, HTML, LaTeX, PostScript en RTF (Windows help)

%package dtd
Summary:	linuxdoc DTD
Summary(pl):	linuxdoc DTD
Group:		Applications/Publishing/SGML

%description dtd
LinuxDoc DTD.

%description dtd -l pl
LinuxDoc DTD.

%package -n sgmls
Summary:	sgmls
Summary(pl):	sgmls
Version:	1.1
Group:		Applications/Publishing/SGML

%description -n sgmls
sgmls - a validating SGML parser.

%description -n sgmls -l pl
sgmls - parser sprawdzaj±cy poprawno¶æ SGML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 
rm config.cache
rm config.status

%build
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
%configure2_13
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

%makeinstall \
	libdir=$RPM_BUILD_ROOT%{_datadir}/sgml-tools \
	perl5libdir=$RPM_BUILD_ROOT%{perl_vendorlib} \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -L %{_libdir}/sgml-tools/dtd/sgml-tools ]; then
	rm -f %{_libdir}/sgml-tools/dtd/sgml-tools
fi
if [ -L %{_datadir}/sgml-tools/dtd/sgml-tools ]; then
	rm -f %{_datadir}/sgml-tools/dtd/sgml-tools
fi

%files
%defattr(644,root,root,755)
%doc doc/{html,guide*,example*,Makedoc.sh,README}
%{_datadir}/sgml-tools
%{perl_vendorlib}/Text/EntityMap.pm
%attr(755,root,root) %{_bindir}/rtf2rtf
%attr(755,root,root) %{_bindir}/sgmlpre
%attr(755,root,root) %{_bindir}/sgml2*
%attr(755,root,root) %{_bindir}/sgmltools.v1
%attr(755,root,root) %{_bindir}/sgmlcheck

%{_mandir}/man1/sgml2*.1*
%{_mandir}/man1/sgmlcheck.1*
%{_mandir}/man1/sgmltools.1*
%lang(pl) %{_mandir}/pl/man1/sgml2*.1*

%files -n sgmls
%defattr(644,root,root,755)
%doc sgmls-1.1/LICENSE sgmls-1.1/NEWS
%attr(755,root,root) %{_bindir}/rast
%attr(755,root,root) %{_bindir}/sgmls
%attr(755,root,root) %{_bindir}/sgmlsasp
%attr(755,root,root) %{_bindir}/sgmls.pl

%{_mandir}/man1/rast.1*
%{_mandir}/man1/sgmls.1*
%{_mandir}/man1/sgmlsasp.1*

%files dtd
%defattr(644,root,root,755)
%{_datadir}/sgml/sgml-tools
%{_datadir}/entity-map
