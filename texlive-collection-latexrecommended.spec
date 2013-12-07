# revision 31071
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-latexrecommended
Epoch:		1
Version:	20131013
Release:	4
Summary:	LaTeX recommended packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-latexrecommended.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-anysize
Requires:	texlive-beamer
Requires:	texlive-booktabs
Requires:	texlive-caption
Requires:	texlive-cite
Requires:	texlive-cmap
Requires:	texlive-crop
Requires:	texlive-ctable
Requires:	texlive-ec
Requires:	texlive-eso-pic
Requires:	texlive-euler
Requires:	texlive-extsizes
Requires:	texlive-fancybox
Requires:	texlive-fancyref
Requires:	texlive-fancyvrb
Requires:	texlive-float
Requires:	texlive-fontspec
Requires:	texlive-fp
Requires:	texlive-index
Requires:	texlive-jknapltx
Requires:	texlive-koma-script
Requires:	texlive-l3kernel
Requires:	texlive-l3packages
Requires:	texlive-l3experimental
Requires:	texlive-listings
Requires:	texlive-mdwtools
Requires:	texlive-memoir
Requires:	texlive-metalogo
Requires:	texlive-mh
Requires:	texlive-microtype
Requires:	texlive-ms
Requires:	texlive-ntgclass
Requires:	texlive-parskip
Requires:	texlive-pdfpages
Requires:	texlive-powerdot
Requires:	texlive-psfrag
Requires:	texlive-rcs
Requires:	texlive-rotating
Requires:	texlive-sansmath
Requires:	texlive-section
Requires:	texlive-seminar
Requires:	texlive-sepnum
Requires:	texlive-setspace
Requires:	texlive-subfig
Requires:	texlive-textcase
Requires:	texlive-thumbpdf
Requires:	texlive-typehtml
Requires:	texlive-underscore
Requires:	texlive-url
Requires:	texlive-xcolor
Requires:	texlive-xkeyval

%description
A collection of recommended add-on packages for LaTeX which
have widespread use.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
