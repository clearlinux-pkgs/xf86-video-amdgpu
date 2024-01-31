#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x4B25B5180522B8D9 (contactshashanksharma@gmail.com)
#
Name     : xf86-video-amdgpu
Version  : 23.0.0
Release  : 685
URL      : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-23.0.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-23.0.0.tar.gz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-amdgpu-23.0.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-amdgpu-data = %{version}-%{release}
Requires: xf86-video-amdgpu-lib = %{version}-%{release}
Requires: xf86-video-amdgpu-license = %{version}-%{release}
Requires: xf86-video-amdgpu-man = %{version}-%{release}
BuildRequires : buildreq-configure
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: symbol.patch

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
%setup -q -n xf86-video-amdgpu-23.0.0
cd %{_builddir}/xf86-video-amdgpu-23.0.0
%patch1 -p1
pushd ..
cp -a xf86-video-amdgpu-23.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685480067
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --disable-glamor
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --disable-glamor
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685480067
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-amdgpu
cp %{_builddir}/xf86-video-amdgpu-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-amdgpu/a297a2b3d9f367ccee795c8a4260d8c7f40ab78f || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-amdgpu.conf

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/xorg/modules/drivers/amdgpu_drv.so
/usr/lib64/xorg/modules/drivers/amdgpu_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-amdgpu/a297a2b3d9f367ccee795c8a4260d8c7f40ab78f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/amdgpu.4
