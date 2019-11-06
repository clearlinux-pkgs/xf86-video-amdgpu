#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5A81AF8E6ADBB200 (daenzer@debian.org)
#
Name     : xf86-video-amdgpu
Version  : 19.1.0
Release  : 29
URL      : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-19.1.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-19.1.0.tar.gz
Source1 : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-19.1.0.tar.gz.sig
Summary  : X.org amdgpu video driver
Group    : Development/Tools
License  : MIT
Requires: xf86-video-amdgpu-data = %{version}-%{release}
Requires: xf86-video-amdgpu-lib = %{version}-%{release}
Requires: xf86-video-amdgpu-license = %{version}-%{release}
Requires: xf86-video-amdgpu-man = %{version}-%{release}
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_amdgpu)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xf86driproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-amdgpu - Xorg driver for AMD Radeon GPUs using the amdgpu kernel driver
==================================================================================

%package data
Summary: data components for the xf86-video-amdgpu package.
Group: Data

%description data
data components for the xf86-video-amdgpu package.


%package lib
Summary: lib components for the xf86-video-amdgpu package.
Group: Libraries
Requires: xf86-video-amdgpu-data = %{version}-%{release}
Requires: xf86-video-amdgpu-license = %{version}-%{release}

%description lib
lib components for the xf86-video-amdgpu package.


%package license
Summary: license components for the xf86-video-amdgpu package.
Group: Default

%description license
license components for the xf86-video-amdgpu package.


%package man
Summary: man components for the xf86-video-amdgpu package.
Group: Default

%description man
man components for the xf86-video-amdgpu package.


%prep
%setup -q -n xf86-video-amdgpu-19.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570902114
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1570902114
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-amdgpu
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-video-amdgpu/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-amdgpu.conf

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/amdgpu_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-amdgpu/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/amdgpu.4
