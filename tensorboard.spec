Name     : tensorboard
Version  : 1.15.0
Release  : 19
URL      : https://github.com/tensorflow/tensorboard/archive/1.15.0.tar.gz
Source0  : https://github.com/tensorflow/tensorboard/archive/1.15.0.tar.gz
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
BuildRequires : python3-core

Source9 : http://localhost/tensorflow/buildcache-1.15.0.tar.gz


Source10 : https://github.com/tensorflow/tensorflow/archive/2243bd6ba9b36d43dbd5c0ede313853f187f5dce.tar.gz
Source11 : https://github.com/protocolbuffers/protobuf/archive/310ba5ee72661c081129eb878c1bbcec936b20f0.tar.gz
Source12 : https://raw.githubusercontent.com/catapult-project/catapult/237aea8b58a37a2991318b6a0db60d84078e5f7e/trace_viewer_full.html
Source13 : https://files.pythonhosted.org/packages/fe/7f/6d70f765ce5484e07576313897793cb49333dd34e462488ee818d17244af/Werkzeug-0.11.15.tar.gz
Source14 : http://mirror.tensorflow.org/github.com/google/closure-compiler/archive/v20190513.tar.gz
Source15 : https://repo1.maven.org/maven2/com/google/template/soy/2019-03-11/soy-2019-03-11.jar
Source16 : https://raw.githubusercontent.com/Microsoft/TypeScript/v2.9.2/lib/tsc.js
Source17 : https://repo1.maven.org/maven2/com/google/guava/guava/24.1-jre/guava-24.1-jre.jar
Source18 : https://repo1.maven.org/maven2/com/google/dagger/dagger-compiler/2.9/dagger-compiler-2.9.jar
Source19 : http://repo1.maven.org/maven2/com/google/javascript/closure-compiler-unshaded/v20190528/closure-compiler-unshaded-v20190528.jar
Source20 : https://repo1.maven.org/maven2/com/google/auto/value/auto-value/1.6/auto-value-1.6.jar
Source21 : http://maven.ibiblio.org/maven2/com/ibm/icu/icu4j/57.1/icu4j-57.1.jar
Source22 : https://github.com/google/closure-library/archive/v20190415.tar.gz
Source23 : http://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz
Source24 : https://github.com/PolymerElements/paper-card/archive/v1.1.6.tar.gz
Source25 : https://github.com/bazelbuild/rules_closure/archive/7434c41542ca9e1b05166d897b90073d1b8b2cf8.tar.gz
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
Source39 : https://github.com/bazelbuild/bazel-skylib/archive/0.7.0.tar.gz
Source40 :  https://github.com/bazelbuild/rules_go/releases/download/0.16.3/rules_go-0.16.3.tar.gz
Source41 : https://github.com/bazelbuild/bazel-gazelle/releases/download/0.15.0/bazel-gazelle-0.15.0.tar.gz
Source42 : https://github.com/bazelbuild/rules_webtesting/releases/download/0.3.1/rules_webtesting.tar.gz
Source43 : https://dl.google.com/go/go1.11.2.linux-amd64.tar.gz
Source44 : https://mirror.bazel.build/openjdk/azul-zulu11.2.3-jdk11.0.1/zulu11.2.3-jdk11.0.1-linux_x64.tar.gz
Source45 : https://mirror.bazel.build/bazel_java_tools/releases/javac11/v4.0/java_tools_javac11_linux-v4.0.zip
Source46 : https://raw.githubusercontent.com/mrdoob/three.js/r104/LICENSE
Source47 : https://raw.githubusercontent.com/mrdoob/three.js/r104/build/three.js
Source48 : http://mirror.tensorflow.org/raw.githubusercontent.com/mrdoob/three.js/r104/examples/js/controls/OrbitControls.js
Source49 : https://github.com/angular/clutz/archive/6c8a2bd68dec3f2bbacae288e42d82ca4567b93f.tar.gz
Source50 : https://mirror.bazel.build/repo1.maven.org/maven2/org/jsoup/jsoup/1.11.3/jsoup-1.11.3.jar
Source51 : http://mirror.tensorflow.org/repo1.maven.org/maven2/org/apache/commons/commons-text/1.6/commons-text-1.6.jar
Source52 : http://mirror.tensorflow.org/repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.9/commons-lang3-3.9.jar
Source53 : https://github.com/vaadin/vaadin-split-layout/archive/v1.1.0.tar.gz
Source54 :  https://github.com/vaadin/vaadin-grid/archive/v3.0.2.tar.gz
Source55 : https://unpkg.com/umap-js@1.0.5/lib/umap-js.min.js
Source56 : https://raw.githubusercontent.com/tensorflow/graphics/cd8c42f9ca260f77c6acfecd42e66ef01d1a3766/tensorflow_graphics/tensorboard/mesh_visualizer/tf_mesh_dashboard/array-buffer-data-provider.js
Source57 :  https://raw.githubusercontent.com/tensorflow/graphics/cd8c42f9ca260f77c6acfecd42e66ef01d1a3766/tensorflow_graphics/tensorboard/mesh_visualizer/tf_mesh_dashboard/mesh-viewer.js
Source58 : https://github.com/bazelbuild/rules_nodejs/releases/download/0.34.0/rules_nodejs-0.34.0.tar.gz
Source59 : http://localhost/tensorflow/buildyarncache-1.15.0.tar.gz

%description
# TensorBoard ![Travis build status](https://travis-ci.org/tensorflow/tensorboard.svg?branch=master)

%prep
%setup -q -n tensorboard-1.15.0
# patch not needed on version 1.15.0
#%patch1 -p1

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

#need to copy all yarn cache as file hits on /tmp/cache
#are not recognized by yarn_install in rules_nodejs
#Provided to make as  buildyarncache-1.15.tar.gz

mkdir -p /builddir/.cache/yarn
pushd /builddir/.cache/yarn
tar -axf %{SOURCE59}
popd

# not using InstallCache for version 1.15.0
# as dependencies are growing large, instead a buildcache-1.15.0
# is populating all the possible hits for building

InstallCache() {
	sha256=`sha256sum $1 | cut -f1 -d" "`
	mkdir -p /tmp/cache/content_addressable/sha256/$sha256/
	cp $1 /tmp/cache/content_addressable/sha256/$sha256/file
}


#InstallCache %{SOURCE10}
#InstallCache %{SOURCE11}
#InstallCache %{SOURCE12}
#InstallCache %{SOURCE13}
#InstallCache %{SOURCE14}
#InstallCache %{SOURCE15}
#InstallCache %{SOURCE16}
#InstallCache %{SOURCE17}
#InstallCache %{SOURCE18}
#InstallCache %{SOURCE19}
#InstallCache %{SOURCE20}
#InstallCache %{SOURCE21}
#InstallCache %{SOURCE22}
InstallCache %{SOURCE23}
#InstallCache %{SOURCE24}
#InstallCache %{SOURCE25}
#InstallCache %{SOURCE26}
#InstallCache %{SOURCE27}
#InstallCache %{SOURCE28}
#InstallCache %{SOURCE29}
#InstallCache %{SOURCE30}
#InstallCache %{SOURCE31}
#InstallCache %{SOURCE32}
#InstallCache %{SOURCE33}
#InstallCache %{SOURCE34}
#InstallCache %{SOURCE35}
#InstallCache %{SOURCE36}
#InstallCache %{SOURCE37}
#InstallCache %{SOURCE38}
#InstallCache %{SOURCE39}
#InstallCache %{SOURCE40}
#InstallCache %{SOURCE41}
#InstallCache %{SOURCE42}
#InstallCache %{SOURCE43}
#InstallCache %{SOURCE44}
#InstallCache %{SOURCE45}
#InstallCache %{SOURCE46}
#InstallCache %{SOURCE47}
#InstallCache %{SOURCE48}
#InstallCache %{SOURCE49}
#InstallCache %{SOURCE50}
#InstallCache %{SOURCE51}
#InstallCache %{SOURCE52}
#InstallCache %{SOURCE53}
#InstallCache %{SOURCE54}
#InstallCache %{SOURCE55}
#InstallCache %{SOURCE56}
#InstallCache %{SOURCE57}


# perform a full clean
bazel clean --expunge
bazel build --repository_cache=/tmp/cache  --incompatible_disable_deprecated_attr_params=false --incompatible_new_actions_api=false --incompatible_depset_is_not_iterable=false  --incompatible_no_support_tools_in_action_inputs=false tensorboard/pip_package:build_pip_package

# a place to put build_pip_package result
mkdir -p /tmp/tensorboard/
bazel run --incompatible_disable_deprecated_attr_params=false  --incompatible_new_actions_api=false --incompatible_depset_is_not_iterable=false  --incompatible_no_support_tools_in_action_inputs=false //tensorboard/pip_package:build_pip_package -- /tmp/tensorboard

%install
export SOURCE_DATE_EPOCH=1503005760
rm -rf %{buildroot}
pip3 install --no-deps --force-reinstall  --root %{buildroot} /tmp/tensorboard/tensorboard-1.15.0-py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/
/usr/bin/tensorboard


