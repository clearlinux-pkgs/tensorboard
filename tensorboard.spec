Name     : tensorboard
Version  : 1.10.0
Release  : 8
URL      : https://github.com/tensorflow/tensorboard/archive/1.10.0.tar.gz
Source0  : https://github.com/tensorflow/tensorboard/archive/1.10.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0

Patch1: nonetwork.patch

BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : bazel
BuildRequires : openjdk-dev
BuildRequires : wheel
BuildRequires : six
BuildRequires : curl
BuildRequires : virtualenv
BuildRequires : python-core

Source9 : http://localhost/tensorflow/buildcache.tar.xz


Source10 : https://github.com/tensorflow/tensorflow/archive/9752b117ff63f204c4975cad52b5aab5c1f5e9a9.tar.gz
Source11 : https://github.com/google/protobuf/archive/v3.6.0.tar.gz
Source12 : https://raw.githubusercontent.com/catapult-project/catapult/237aea8b58a37a2991318b6a0db60d84078e5f7e/trace_viewer_full.html
Source13 : https://pypi.python.org/packages/b7/7f/44d3cfe5a12ba002b253f6985a4477edfa66da53787a2a838a40f6415263/Werkzeug-0.11.10.tar.gz
Source14 : https://github.com/google/closure-compiler/archive/v20180402.tar.gz
Source15 : https://repo1.maven.org/maven2/com/google/template/soy/2018-03-14/soy-2018-03-14.jar
Source16 : https://raw.githubusercontent.com/Microsoft/TypeScript/v2.7.2/lib/tsc.js
Source17 : https://repo1.maven.org/maven2/com/google/guava/guava/24.1-jre/guava-24.1-jre.jar
Source18 : https://repo1.maven.org/maven2/com/google/dagger/dagger-compiler/2.9/dagger-compiler-2.9.jar
Source19 : https://repo1.maven.org/maven2/com/google/javascript/closure-compiler-unshaded/v20180402/closure-compiler-unshaded-v20180402.jar
Source20 : https://repo1.maven.org/maven2/com/google/auto/value/auto-value/1.6/auto-value-1.6.jar
Source21 : http://maven.ibiblio.org/maven2/com/ibm/icu/icu4j/57.1/icu4j-57.1.jar
Source22 : https://github.com/google/closure-library/archive/v20180405.tar.gz
Source23 : http://nodejs.org/dist/v6.9.1/node-v6.9.1-linux-x64.tar.xz
Source24 : https://github.com/PolymerElements/paper-card/archive/v1.1.6.tar.gz
Source25 : https://github.com/bazelbuild/rules_closure/archive/0.7.0.tar.gz

%description
# TensorBoard ![Travis build status](https://travis-ci.org/tensorflow/tensorboard.svg?branch=master)

%prep
%setup -q -n tensorboard-1.10.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503005760

mkdir -p /tmp/cache
pushd /tmp/cache
tar -axf %{SOURCE9}
popd

InstallCache() {
	sha256=`sha256sum $1 | cut -f1 -d" "`
	mkdir -p /tmp/cache/content_addressable/sha256/$sha256/
	cp $1 /tmp/cache/content_addressable/sha256/$sha256/file
}


InstallCache %{SOURCE10}
InstallCache %{SOURCE11}
InstallCache %{SOURCE12}
InstallCache %{SOURCE13}
InstallCache %{SOURCE14}
InstallCache %{SOURCE15}
InstallCache %{SOURCE16}
InstallCache %{SOURCE17}
InstallCache %{SOURCE18}
InstallCache %{SOURCE19}
InstallCache %{SOURCE20}
InstallCache %{SOURCE21}
InstallCache %{SOURCE22}
InstallCache %{SOURCE23}
InstallCache %{SOURCE24}
InstallCache %{SOURCE25}


bazel clean
bazel build --repository_cache=/tmp/cache  tensorboard/pip_package:build_pip_package
bazel run //tensorboard/pip_package:build_pip_package



%install
export SOURCE_DATE_EPOCH=1503005760
rm -rf %{buildroot}
pip3 install --no-deps --force-reinstall  --root %{buildroot} /tmp/tensorboard/dist/tensorboard-1.10.0-py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/
/usr/bin/tensorboard


