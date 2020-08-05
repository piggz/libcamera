Name:       libcamera
Summary:    open source camera stack and framework for Linux
Version:    0.0.0
Release:    1
Group:      Multimedia
License:    LGPLv2.1
URL:        https://libcamera.org
Source:     %{name}-%{version}.tar.bz2

BuildRequires: meson
BuildRequires: ninja
BuildRequires: openssl
BuildRequires: boost-devel
BuildRequires: python-yaml
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)

%description
A complex camera support library for Linux, Android, and ChromeOS

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%meson -Dgstreamer=enabled \
	-Dv4l2=true \
	-Dqcam=enabled

%meson_build

%install
%meson_install

%files
%defattr(-,root,root,-)
%{_libdir}/libcamera.so.*

