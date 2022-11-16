Name:		texlive-texproposal
Version:	43151
Release:	1
Summary:	A proposal prototype for LaTeX promotion in Chinese universities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texproposal
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texproposal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texproposal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains the original source code and necessary
attachment of the document "Proposal for Offering TeX Courses
and Relevant Resources in Chongqing University". This proposal
could be helpful if one is considering to suggest his/her
university or company to use TeX (or LaTeX, or XeLaTeX) as a
typesetting system, especially for Chinese universities and
companies. The present proposal mainly explains the importance
and necessity of introducing TeX, a typesetting system often
used in academic writing, to students and teachers. This
proposal starts from a brief introduction of TeX, then steps
further into its fascinating application to academic writing
and dissertation formatting. Finally, a set of possible
implementation strategies with regard to the proper
introduction of TeX and relevant resources to our university,
is proposed.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/texproposal

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
