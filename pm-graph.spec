#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pm-graph
Version  : 5.5
Release  : 6
URL      : https://github.com/intel/pm-graph/archive/5.5.tar.gz
Source0  : https://github.com/intel/pm-graph/archive/5.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pm-graph-bin = %{version}-%{release}
Requires: pm-graph-license = %{version}-%{release}
Requires: pm-graph-man = %{version}-%{release}
BuildRequires : util-linux

%description
p m - g r a p h
pm-graph: suspend/resume/boot timing analysis tools
Version: 5.5
Author: Todd Brandt <todd.e.brandt@intel.com>
Home Page: https://01.org/pm-graph

%package bin
Summary: bin components for the pm-graph package.
Group: Binaries
Requires: pm-graph-license = %{version}-%{release}

%description bin
bin components for the pm-graph package.


%package license
Summary: license components for the pm-graph package.
Group: Default

%description license
license components for the pm-graph package.


%package man
Summary: man components for the pm-graph package.
Group: Default

%description man
man components for the pm-graph package.


%prep
%setup -q -n pm-graph-5.5
cd %{_builddir}/pm-graph-5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572380484
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1572380484
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pm-graph
cp %{_builddir}/pm-graph-5.5/COPYING %{buildroot}/usr/share/package-licenses/pm-graph/a7a897a4bde987e597c04f16a9c28f6d3f57916d
cp %{_builddir}/pm-graph-5.5/debian/copyright %{buildroot}/usr/share/package-licenses/pm-graph/c6968fc73b0c521cdaea80f5862460ea1fd7a317
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/pm-graph/bootgraph.py
/usr/lib/pm-graph/config/cgskip.txt
/usr/lib/pm-graph/config/freeze-callgraph.cfg
/usr/lib/pm-graph/config/freeze-dev.cfg
/usr/lib/pm-graph/config/freeze.cfg
/usr/lib/pm-graph/config/standby-callgraph.cfg
/usr/lib/pm-graph/config/standby-dev.cfg
/usr/lib/pm-graph/config/standby.cfg
/usr/lib/pm-graph/config/suspend-callgraph.cfg
/usr/lib/pm-graph/config/suspend-dev.cfg
/usr/lib/pm-graph/config/suspend-x2-proc.cfg
/usr/lib/pm-graph/config/suspend.cfg
/usr/lib/pm-graph/sleepgraph.py

%files bin
%defattr(-,root,root,-)
/usr/bin/bootgraph
/usr/bin/sleepgraph

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pm-graph/a7a897a4bde987e597c04f16a9c28f6d3f57916d
/usr/share/package-licenses/pm-graph/c6968fc73b0c521cdaea80f5862460ea1fd7a317

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/bootgraph.8
/usr/share/man/man8/sleepgraph.8
