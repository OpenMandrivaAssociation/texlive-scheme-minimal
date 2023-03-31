Name:		texlive-scheme-minimal
Version:	54191
Release:	2
Summary:	minimal scheme (plain only)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-minimal.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic

%description
This is the minimal TeX Live scheme, with support for only
plain TeX. (No LaTeX macros.)  LuaTeX is included because Lua
scripts are used in TeX Live infrastructure.  This scheme
corresponds exactly to collection-basic.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
