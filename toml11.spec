%global user	ToruNiina

name:           toml11
Summary:		Toml11 is a C++11 header-only toml parser/encoder depending only on C++ standard library
License:        MIT
Group:          Development/Languages/C and C++
Release:        1%{?dist}
Version:        2.2.2
Requires:		gcc-c++
BuildRequires:	cmake make gcc-c++ boost-devel
BuildArch:		x86_64
Url:            https://github.com/%{user}/%{name}/
Source0:        https://github.com/%{user}/%{name}/archive/v%{version}.tar.gz

%package devel
Summary:        Toml11 is a C++11 header-only toml parser/encoder depending only on C++ standard library
Group:          Development/Languages/C and C++
Provides: %{name}-static = %{version}-%{release}

%description
Toml11 is a C++11 header-only toml parser/encoder depending only on C++ standard library. Compatible to the latest version of TOML v0.5.0 after version 2.0.0.

%description devel
Toml11 is a C++11 header-only toml parser/encoder depending only on C++ standard library. Compatible to the latest version of TOML v0.5.0 after version 2.0.0.

%global debug_package %{nil}

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/%{_includedir}/%{name}
cp -ar toml/ LICENSE README.md toml.hpp %{buildroot}/%{_includedir}/%{name}

%check
%cmake
make
make test

%files devel
%defattr(-, root, root)
%doc README.md
%license LICENSE
%{_includedir}/%{name}/

%changelog

