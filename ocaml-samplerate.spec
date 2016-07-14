Name:     ocaml-samplerate

Version:  0.1.3
Release:  1
Summary:  OCaml bindings for the libsamplerate
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-samplerate
Source0:  https://github.com/savonet/ocaml-samplerate/releases/download/0.1.3/ocaml-samplerate-0.1.3.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: libsamplerate-devel
Requires:      libsamplerate

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
/usr/lib64/ocaml/samplerate/META
/usr/lib64/ocaml/samplerate/dllsamplerate_stubs.so
/usr/lib64/ocaml/samplerate/libsamplerate_stubs.a
/usr/lib64/ocaml/samplerate/samplerate.a
/usr/lib64/ocaml/samplerate/samplerate.cma
/usr/lib64/ocaml/samplerate/samplerate.cmi
/usr/lib64/ocaml/samplerate/samplerate.cmx
/usr/lib64/ocaml/samplerate/samplerate.cmxa
/usr/lib64/ocaml/samplerate/samplerate.mli

%description
OCAML bindings for the libsamplerate based on based on Madlld example.


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-samplerate.spec
