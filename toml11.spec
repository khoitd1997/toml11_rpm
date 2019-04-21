%global user            ToruNiina
%global toml_ver        0.5.0
%global debug_package   %{nil}

Name:               toml11
Summary:            Toml parser/encoder C++11 headers library
License:            MIT
Group:              Development/Languages/C and C++
Release:            1%{?dist}
Version:            2.2.2

BuildRequires:      cmake
BuildRequires:      make
BuildRequires:      gcc-c++
BuildRequires:      boost-devel

ExclusiveArch:      x86_64 ARM-hfp AArch64
Url:                https://github.com/%{user}/%{name}/
Source0:            https://github.com/%{user}/%{name}/archive/v%{version}.tar.gz
Source1:            https://github.com/toml-lang/toml/archive/v%{toml_ver}.tar.gz

%description
Toml11 is a C++11 header-only toml parser/encoder. Compliant with %{toml_ver}

%package devel
Summary:            Toml parser/encoder C++11 headers library
Group:              Development/Languages/C and C++
Provides:           %{name}-static = %{version}-%{release}
Provides:           %{name} = %{version}-%{release}
Requires:           libstdc++-devel

%description devel
Toml11 is a C++11 header-only toml parser/encoder. Compliant with %{toml_ver}

%prep
%setup -q
%setup -q -T -D -a 1
mkdir build
cd build
gzip -dc %{SOURCE1} | tar -xvvf -
mv toml-%{toml_ver} toml

%build

%install
mkdir -p %{buildroot}/%{_includedir}/%{name}
cp -ar toml/ LICENSE README.md toml.hpp %{buildroot}/%{_includedir}/%{name}

%check
cd build
cmake ..
make
make test

%files devel
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_includedir}/%{name}

%changelog