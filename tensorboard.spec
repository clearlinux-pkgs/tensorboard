Name     : tensorboard
Version  : 1.13.0
Release  : 12
URL      : https://github.com/tensorflow/tensorboard/archive/1.13.0.tar.gz
Source0  : https://github.com/tensorflow/tensorboard/archive/1.13.0.tar.gz
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

Source9 : http://localhost/tensorflow/buildcache-1.11.tar.gz


Source10 : https://github.com/tensorflow/tensorflow/archive/6ef428bd6e83b0930266bf922eaa2f4a60e8328a.tar.gz
Source11 : https://github.com/protocolbuffers/protobuf/archive/v3.6.1.2.tar.gz
Source12 : https://raw.githubusercontent.com/catapult-project/catapult/237aea8b58a37a2991318b6a0db60d84078e5f7e/trace_viewer_full.html
Source13 : https://files.pythonhosted.org/packages/fe/7f/6d70f765ce5484e07576313897793cb49333dd34e462488ee818d17244af/Werkzeug-0.11.15.tar.gz
Source14 : https://github.com/google/closure-compiler/archive/v20180402.tar.gz
Source15 : https://repo1.maven.org/maven2/com/google/template/soy/2018-03-14/soy-2018-03-14.jar
Source16 : https://raw.githubusercontent.com/Microsoft/TypeScript/v2.9.2/lib/tsc.js
Source17 : https://repo1.maven.org/maven2/com/google/guava/guava/24.1-jre/guava-24.1-jre.jar
Source18 : https://repo1.maven.org/maven2/com/google/dagger/dagger-compiler/2.9/dagger-compiler-2.9.jar
Source19 : https://repo1.maven.org/maven2/com/google/javascript/closure-compiler-unshaded/v20180402/closure-compiler-unshaded-v20180402.jar
Source20 : https://repo1.maven.org/maven2/com/google/auto/value/auto-value/1.6/auto-value-1.6.jar
Source21 : http://maven.ibiblio.org/maven2/com/ibm/icu/icu4j/57.1/icu4j-57.1.jar
Source22 : https://github.com/google/closure-library/archive/v20180405.tar.gz
Source23 : http://nodejs.org/dist/v6.9.1/node-v6.9.1-linux-x64.tar.xz
Source24 : https://github.com/PolymerElements/paper-card/archive/v1.1.6.tar.gz
Source25 : https://github.com/bazelbuild/rules_closure/archive/0.8.0.tar.gz
Source26 : https://repo1.maven.org/maven2/com/google/dagger/dagger/2.14.1/dagger-2.14.1.jar
Source27 : https://mirror.bazel.build/repo1.maven.org/maven2/com/google/dagger/dagger-compiler/2.14.1/dagger-compiler-2.14.1.jar
Source28 : https://mirror.bazel.build/repo1.maven.org/maven2/com/google/googlejavaformat/google-java-format/1.5/google-java-format-1.5.jar
Source29 : https://repo1.maven.org/maven2/com/squareup/javapoet/1.9.0/javapoet-1.9.0.jar
Source30 : https://repo1.maven.org/maven2/com/google/dagger/dagger-producers/2.14.1/dagger-producers-2.14.1.jar
Source31 : https://repo1.maven.org/maven2/com/google/dagger/dagger-spi/2.14.1/dagger-spi-2.14.1.jar
Source32 : https://repo1.maven.org/maven2/com/google/errorprone/javac-shaded/9-dev-r4023-3/javac-shaded-9-dev-r4023-3.jar
Source33 : https://raw.githubusercontent.com/cpettitt/graphlib/v2.1.5/dist/graphlib.core.js
Source34 : https://raw.githubusercontent.com/cpettitt/dagre/v0.8.2/dist/dagre.core.js
Source35 : https://github.com/d3/d3/releases/download/v5.7.0/d3.zip
Source36 : https://registry.npmjs.org/plottable/-/plottable-3.7.0.tgz
Source37 : https://github.com/lodash/lodash/archive/4.17.5.tar.gz
Source38 : https://github.com/pair-code/facets/archive/0.2.1.tar.gz
Source39 : https://github.com/bazelbuild/bazel-skylib/archive/e9fc4750d427196754bebb0e2e1e38d68893490a.tar.gz
Source40 :  https://github.com/bazelbuild/rules_go/releases/download/0.16.3/rules_go-0.16.3.tar.gz
Source41 : https://github.com/bazelbuild/bazel-gazelle/releases/download/0.15.0/bazel-gazelle-0.15.0.tar.gz
Source42 :  https://github.com/bazelbuild/rules_webtesting/archive/0.2.2.tar.gz
Source43 : https://dl.google.com/go/go1.11.2.linux-amd64.tar.gz
Source44 : https://mirror.bazel.build/openjdk/azul-zulu-9.0.7.1-jdk9.0.7/zulu9.0.7.1-jdk9.0.7-linux_x64-allmodules.tar.gz

%description
# TensorBoard ![Travis build status](https://travis-ci.org/tensorflow/tensorboard.svg?branch=master)

%prep
%setup -q -n tensorboard-1.13.0
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
InstallCache %{SOURCE26}
InstallCache %{SOURCE27}
InstallCache %{SOURCE28}
InstallCache %{SOURCE29}
InstallCache %{SOURCE30}
InstallCache %{SOURCE31}
InstallCache %{SOURCE32}
InstallCache %{SOURCE33}
InstallCache %{SOURCE34}
InstallCache %{SOURCE35}
InstallCache %{SOURCE36}
InstallCache %{SOURCE37}
InstallCache %{SOURCE38}
InstallCache %{SOURCE39}
InstallCache %{SOURCE40}
InstallCache %{SOURCE41}
InstallCache %{SOURCE42}
InstallCache %{SOURCE43}
InstallCache %{SOURCE44}




bazel clean
bazel build --repository_cache=/tmp/cache  tensorboard/pip_package:build_pip_package
bazel run //tensorboard/pip_package:build_pip_package



%install
export SOURCE_DATE_EPOCH=1503005760
rm -rf %{buildroot}
pip3 install --no-deps --force-reinstall  --root %{buildroot} /tmp/tensorboard/dist/tensorboard-1.13.0-py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/
/usr/bin/tensorboard


