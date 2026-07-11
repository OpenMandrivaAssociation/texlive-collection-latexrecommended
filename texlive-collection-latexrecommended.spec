%global tl_name collection-latexrecommended
%global tl_revision 78568

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX recommended packages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-latexrecommended
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-latexrecommended.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(anysize)
Requires:	texlive(attachfile2)
Requires:	texlive(beamer)
Requires:	texlive(booktabs)
Requires:	texlive(breqn)
Requires:	texlive(caption)
Requires:	texlive(cite)
Requires:	texlive(cmap)
Requires:	texlive(collection-latex)
Requires:	texlive(crop)
Requires:	texlive(ctable)
Requires:	texlive(eso-pic)
Requires:	texlive(euenc)
Requires:	texlive(euler)
Requires:	texlive(everysel)
Requires:	texlive(everyshi)
Requires:	texlive(extsizes)
Requires:	texlive(fancybox)
Requires:	texlive(fancyref)
Requires:	texlive(fancyvrb)
Requires:	texlive(filehook)
Requires:	texlive(float)
Requires:	texlive(fontspec)
Requires:	texlive(footnotehyper)
Requires:	texlive(fp)
Requires:	texlive(grffile)
Requires:	texlive(hologo)
Requires:	texlive(index)
Requires:	texlive(infwarerr)
Requires:	texlive(jknapltx)
Requires:	texlive(koma-script)
Requires:	texlive(l3experimental)
Requires:	texlive(latexbug)
Requires:	texlive(lineno)
Requires:	texlive(listings)
Requires:	texlive(ltx-talk)
Requires:	texlive(lua-unicode-math)
Requires:	texlive(lwarp)
Requires:	texlive(mathspec)
Requires:	texlive(mathtools)
Requires:	texlive(mdwtools)
Requires:	texlive(memoir)
Requires:	texlive(metalogo)
Requires:	texlive(microtype)
Requires:	texlive(newfloat)
Requires:	texlive(ntgclass)
Requires:	texlive(parskip)
Requires:	texlive(pdfcolfoot)
Requires:	texlive(pdflscape)
Requires:	texlive(pdfpages)
Requires:	texlive(polyglossia)
Requires:	texlive(psfrag)
Requires:	texlive(ragged2e)
Requires:	texlive(rcs)
Requires:	texlive(sansmath)
Requires:	texlive(section)
Requires:	texlive(seminar)
Requires:	texlive(sepnum)
Requires:	texlive(setspace)
Requires:	texlive(subfig)
Requires:	texlive(textcase)
Requires:	texlive(thumbpdf)
Requires:	texlive(translator)
Requires:	texlive(typehtml)
Requires:	texlive(ucharcat)
Requires:	texlive(underscore)
Requires:	texlive(unicode-math)
Requires:	texlive(xcolor)
Requires:	texlive(xfrac)
Requires:	texlive(xkeyval)
Requires:	texlive(xltxtra)
Requires:	texlive(xunicode)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of recommended add-on packages for LaTeX which have
widespread use.

