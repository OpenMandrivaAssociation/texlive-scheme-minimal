# revision 13822
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-minimal
Version:	20120307
Release:	8
Summary:	minimal scheme (plain only)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-minimal.tar.xz
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
%setup -c -a0

%build

%install


%changelog
* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120307-1
+ Revision: 783154
- Import texlive-scheme-minimal
- Import texlive-scheme-minimal

