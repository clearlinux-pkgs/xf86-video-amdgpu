#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-video-amdgpu
Version  : 22.0.0
Release  : 178
URL      : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-22.0.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-22.0.0.tar.gz
Summary  : No detailed summary available
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
%setup -q -n xf86-video-amdgpu-22.0.0
cd %{_builddir}/xf86-video-amdgpu-22.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645829331
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1645829331
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-amdgpu
cp %{_builddir}/xf86-video-amdgpu-22.0.0/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-amdgpu/a297a2b3d9f367ccee795c8a4260d8c7f40ab78f
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
/usr/share/package-licenses/xf86-video-amdgpu/a297a2b3d9f367ccee795c8a4260d8c7f40ab78f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/amdgpu.4
