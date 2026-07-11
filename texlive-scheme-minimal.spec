%global tl_name scheme-minimal
%global tl_revision 54191

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	minimal scheme (plain only)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-minimal
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-minimal.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(collection-basic)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the minimal TeX Live scheme, with support for only plain TeX.
(No LaTeX macros.) LuaTeX is included because Lua scripts are used in
TeX Live infrastructure. This scheme corresponds exactly to collection-
basic.

