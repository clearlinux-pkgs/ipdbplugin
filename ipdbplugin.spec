#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipdbplugin
Version  : 1.5.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/cf/cb/510dcb9ae401e6876415412f0cc7bd2df8f7e9eb6667c23a2bd941309b88/ipdbplugin-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cf/cb/510dcb9ae401e6876415412f0cc7bd2df8f7e9eb6667c23a2bd941309b88/ipdbplugin-1.5.0.tar.gz
Summary  : Nose plugin to use iPdb instead of Pdb when tests fail
Group    : Development/Tools
License  : LGPL-2.1
Requires: ipdbplugin-python = %{version}-%{release}
Requires: ipdbplugin-python3 = %{version}-%{release}
Requires: ipython
Requires: nose
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : nose

%description
What about running nose with a smarter interactive debugger?

        Use this and *never* risk yourself forgetting `import ipdb; ipdb.set_trace()` in your code again!

        This plugin is 99.99% based on nose's builtin debug plugin.

        If you have any ideas about how to improve it, come and fork the code at http://github.com/flavioamieiro/nose-ipdb

%package python
Summary: python components for the ipdbplugin package.
Group: Default
Requires: ipdbplugin-python3 = %{version}-%{release}

%description python
python components for the ipdbplugin package.


%package python3
Summary: python3 components for the ipdbplugin package.
Group: Default
Requires: python3-core
Provides: pypi(ipdbplugin)

%description python3
python3 components for the ipdbplugin package.


%prep
%setup -q -n ipdbplugin-1.5.0
cd %{_builddir}/ipdbplugin-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583159077
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
