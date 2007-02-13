Summary:	Enhanced Machine Controller
Summary(pl.UTF-8):	Enhanced Machine Controller - rozszerzone sterowanie maszynami
Name:		emc
Version:	2.0.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/emc/%{name}%{version}.tar.gz
# Source0-md5:	73810d60e7293e2f9dc8cef3925e1359
URL:		http://www.linuxcnc.org/
BuildRequires:	gtk+2-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EMC (the Enhanced Machine Control) is a software system for computer
control of machine tools such as milling machines. It provides:
- a user interface (actually several interfaces to chose from),
- an interpreter for "G-code" (the RS-274 machine tool programming
  language),
- and operates the actual electronic interfaces that control the motor
  drives on the machine tool.

It provides the "computer" functions needed to actually run the
machine's electronics. It does not provide drawing (CAD - Computer
Aided Design) or G-code generation from the drawing (CAM - Computer
Automated Manufacturing) functions. It can control up to 6 axes and
supports a variety of interfaces. The motion control can operate true
servos (usually analog) with the feedback loop closed by the EMC
software at the computer, or open loop with "step-servos" or stepper
motors. Motion planning includes cutter radius compensation, tool
length offsets, and constant velocity control. Support for
non-Cartesian motion systems is provided via kinematics. This includes
hexapods (Stewart platforms and similar concepts) and systems with
rotary joints to provide motion.

%description -l pl.UTF-8
EMC (Enhanced Machine Control - rozszerzone sterowanie maszynami) to
programowy system do komputerowego sterowania narzędziami takimi jak
frezarki. Udostępnia:
- interfejs użytkownika (właściwie kilka interfejsów do wyboru)
- interpreter "G-kodu" (języka programowania maszyn RS-274)
- współpracuje z właściwymi interfejsami elektronicznymi sterującymi
silnikami obrabiarki.

Udostępnia funkcje "komputerowe" niezbędne do właściwego działania
elektroniki maszyn. Nie udostępnia funkcji projektowania (CAD -
Computer Aided Design) ani generowania G-kodu z projektu (CAM -
Computer Aided Manufacturing). Potrafi sterować maksymalnie 6 osiami i
obsługuje różnorodne interfejsy. Sterowanie ruchem może operować na
prawdziwych serwomechanizmach (zwykle analogowych) z pętlą zwrotną
zamkniętą przez oprogramowanie EMC na komputerze lub z otwartą pętlą z
"serwomechanizmami krokowymi" lub silnikami krokowymi. Planowanie
ruchów obejmuje kompensację promienia freza, offsety długości
narzędzia i stałe sterowanie prędkością. Obsługa niekartezjańskich
układów sterowania jest zapewniona poprzez kinematykę. Obejmuje to
heksapody (platformy Stewarta i podobne idee) oraz systemy z
połączeniami obrotowymi.

%prep
%setup -q -n %{name}2

%build
cd src
%configure \
	--enable-simulator
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO docs/{*.pdf,NEWS,README} docs/help/*.*
%attr(755,root,root) %{_bindir}/*
