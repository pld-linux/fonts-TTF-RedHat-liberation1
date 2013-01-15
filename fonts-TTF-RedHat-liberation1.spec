Summary:	Fonts to replace commonly used Microsoft Windows Fonts
Summary(pl.UTF-8):	Fonty zastępujące popularne fonty z Microsoft Windows
Name:		fonts-TTF-RedHat-liberation1
Version:	1.07.2
Release:	1
License:	GPL v2 + exceptions
Group:		Fonts
Source0:	https://fedorahosted.org/releases/l/i/liberation-fonts/liberation-fonts-%{version}.tar.gz
# Source0-md5:	293b364f3de019f0b19ddd54d36737e6
Source1:	liberation-fonts-mono.conf
Source2:	liberation-fonts-sans.conf
Source3:	liberation-fonts-serif.conf
Source4:	liberation-fonts-narrow.conf
Patch0:		liberation-fonts-bug-715309-714191-835182.patch
URL:		https://fedorahosted.org/liberation-fonts/
BuildRequires:	fontforge >= 20090923
BuildRequires:	fonttools
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Obsoletes:	liberation-fonts-ttf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems.

There are three sets: Sans (a substitute for Arial, Albany, Helvetica,
Nimbus Sans L, and Bitstream Vera Sans), Serif (a substitute for Times
New Roman, Thorndale, Nimbus Roman, and Bitstream Vera Serif) and Mono
(a substitute for Courier New, Cumberland, Courier, Nimbus Mono L, and
Bitstream Vera Sans Mono).

%description -l pl.UTF-8
Fonty Liberation mają być zamiennikami trzech najczęściej używanych
fontów z systemów Microsoftu.

Pakiet zawiera trzy zestawy: Sans (zamiennik dla Arial, Albany,
Helvetica, Nimbus Sans L i Bitstream Vera Sans), Serif (zamiennik dla
Times New Roman, Thorndale, Nimbus Roman i Bitstream Vera Serif) i
Mono (zamiennik dla Courier New, Cumberland, Courier, Nimbus Mono L i
Bitstream Vera Sans Mono).

%prep
%setup -q -n liberation-fonts-%{version}
%patch0 -p1

%build
%{__make}
mv liberation-fonts-ttf-%{version}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_sysconfdir}/fonts/conf.d,%{_datadir}/fontconfig/conf.avail}

cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/59-liberation-mono.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/59-liberation-sans.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/59-liberation-serif.conf
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/59-liberation-narrow.conf

ln -s %{_datadir}/fontconfig/conf.avail/59-liberation-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/59-liberation-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/59-liberation-serif.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/59-liberation-narrow.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog License.txt README TODO
%{_ttffontsdir}/LiberationMono-*.ttf
%{_ttffontsdir}/LiberationSans-*.ttf
%{_ttffontsdir}/LiberationSerif-*.ttf
%{_ttffontsdir}/LiberationSansNarrow-*.ttf
%{_datadir}/fontconfig/conf.avail/59-liberation-*.conf
%{_sysconfdir}/fonts/conf.d/59-liberation-*.conf
