Summary:	Enhanced Machine Controller
Summary(pl):	Enhanced Machine Controller - rozszerzone sterowanie maszynami
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

%description -l pl
EMC (Enhanced Machine Control - rozszerzone sterowanie maszynami) to
programowy system do komputerowego sterowania narzêdziami takimi jak
frezarki. Udostêpnia:
- interfejs u¿ytkownika (w³a¶ciwie kilka interfejsów do wyboru)
- interpreter "G-kodu" (jêzyka programowania maszyn RS-274)
- wspó³pracuje z w³a¶ciwymi interfejsami elektronicznymi steruj±cymi
silnikami obrabiarki.

Udostêpnia funkcje "komputerowe" niezbêdne do w³a¶ciwego dzia³ania
elektroniki maszyn. Nie udostêpnia funkcji projektowania (CAD -
Computer Aided Design) ani generowania G-kodu z projektu (CAM -
Computer Aided Manufacturing). Potrafi sterowaæ maksymalnie 6 osiami i
obs³uguje ró¿norodne interfejsy. Sterowanie ruchem mo¿e operowaæ na
prawdziwych serwomechanizmach (zwykle analogowych) z pêtl± zwrotn±
zamkniêt± przez oprogramowanie EMC na komputerze lub z otwart± pêtl± z
"serwomechanizmami krokowymi" lub silnikami krokowymi. Planowanie
ruchów obejmuje kompensacjê promienia freza, offsety d³ugo¶ci
narzêdzia i sta³e sterowanie prêdko¶ci±. Obs³uga niekartezjañskich
uk³adów sterowania jest zapewniona poprzez kinematykê. Obejmuje to
heksapody (platformy Stewarta i podobne idee) oraz systemy z
po³±czeniami obrotowymi.

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
