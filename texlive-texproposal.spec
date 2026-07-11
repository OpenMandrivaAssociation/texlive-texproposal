%global tl_name texproposal
%global tl_revision 43151

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	A proposal prototype for LaTeX promotion in Chinese universities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/texproposal
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texproposal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texproposal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains the original source code and necessary attachment
of the document "Proposal for Offering TeX Courses and Relevant
Resources in Chongqing University". This proposal could be helpful if
one is considering to suggest his/her university or company to use TeX
(or LaTeX, or XeLaTeX) as a typesetting system, especially for Chinese
universities and companies. The present proposal mainly explains the
importance and necessity of introducing TeX, a typesetting system often
used in academic writing, to students and teachers. This proposal starts
from a brief introduction of TeX, then steps further into its
fascinating application to academic writing and dissertation formatting.
Finally, a set of possible implementation strategies with regard to the
proper introduction of TeX and relevant resources to our university, is
proposed.

