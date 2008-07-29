%define	major 1
%define libname	%mklibname %{name} %{major}

Summary:	Library for displaying messages
Name:		shhmsg
Version:	1.4.1
Release:	%mkrel 6
License:	Artistic
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://shh.thathost.com/pub-unix/
Source0:	http://shh.thathost.com/pub-unix/files/%{name}-%{version}.tar.bz2

%description
C-functions for error messages, verbose messages and `normal'
messages in terminalbased programs.

%package -n	%{libname}
Summary:	Library for displaying messages
Group:          System/Libraries

%description -n	%{libname}
C-functions for error messages, verbose messages and `normal'
messages in terminalbased programs.

%package -n	%{libname}-devel
Summary:	Library and header files for the %{name} library
Group:		Development/C
Provides:	lib%{name}-devel = %{version}
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
C-functions for error messages, verbose messages and `normal'
messages in terminalbased programs.

%prep

%setup -q -n %{name}-%{version}

%build

# make the shared library
make SHARED="1" OPTIM="%{optflags} -D_REENTRANT -fPIC"

# make the static library
make OPTIM="%{optflags} -D_REENTRANT -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

# install the shared library
make \
    SHARED="1" \
    INSTBASEDIR="%{buildroot}%{_prefix}" \
    INSTLIBDIR=%{buildroot}%{_libdir} \
    install


# install the static library
make \
    INSTBASEDIR="%{buildroot}%{_prefix}" \
    INSTLIBDIR=%{buildroot}%{_libdir} \
    install

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc CREDITS ChangeLog INSTALL README shhmsg.txt
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
