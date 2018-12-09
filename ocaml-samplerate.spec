Name:     ocaml-samplerate
Version:  0.1.4
Release:  1%{?dist}
Summary:  OCaml bindings for the libsamplerate

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-samplerate
Source0:  https://github.com/savonet/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz


BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: libsamplerate-devel
Requires:      libsamplerate


%description
OCAML bindings for libsamplerate based on based on Madlld example.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=%{_prefix} \
   --disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
%doc README
%license COPYING
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.1.4-1
- Bump to 0.1.4
- Cleanup specfile and create -devel subpackage

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.1.3-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-samplerate.spec
