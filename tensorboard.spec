Name     : tensorboard
Version  : 1.9.0
Release  : 8
URL      : https://github.com/tensorflow/tensorboard/archive/1.9.0.tar.gz
Source0  : https://github.com/tensorflow/tensorboard/archive/1.9.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
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


Source10 : https://github.com/tensorflow/tensorflow/archive/3128b43eb0bf37ac3c49cb22a6e1789d8ea346e8.tar.gz
Source11 : https://github.com/google/protobuf/archive/v3.5.1.tar.gz
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

%description
# TensorBoard ![Travis build status](https://travis-ci.org/tensorflow/tensorboard.svg?branch=master)

%prep
%setup -q -n tensorboard-1.9.0

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


bazel clean
bazel --output_base=/tmp/bazel   build --repository_cache=/tmp/cache  tensorboard/pip_package:build_pip_package
export RUNFILES=/tmp/bazel/execroot/
tensorboard/pip_package/build_pip_package.sh /tmp/whl


%install
export SOURCE_DATE_EPOCH=1503005760
rm -rf %{buildroot}
pip3 install --no-deps --force-reinstall  --root %{buildroot} /tmp/whl/*whl

%files
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/
/usr/bin/tensorboard


%exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/api_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/field_mask_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/text_format.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/containers.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/containers.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/pyext/cpp_message.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/proto_builder.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/encoder.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/enum_type_wrapper.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/service.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/field_mask_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/empty_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/api_implementation.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/struct_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/json_format.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/service_reflection.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/compiler/__pycache__/plugin_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/pyext/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/struct_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/compiler/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/empty_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/compiler/plugin_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/text_encoding.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/wrappers_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/duration_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/python_message.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/text_format.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/proto_builder.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor_pool.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/json_format.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/descriptor_pool.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/api_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/type_checkers.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/message_listener.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/pyext/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/source_context_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/symbol_database.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/source_context_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor_database.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/enum_type_wrapper.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/timestamp_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/wire_format.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/python_message.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/testing_refleaks.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/well_known_types.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/service_reflection.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/encoder.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/compiler/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/_parameterized.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/service.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/descriptor_database.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/decoder.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/decoder.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/reflection.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/message.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/message_factory.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/__pycache__/__init__.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/type_checkers.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/reflection.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/timestamp_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/type_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/any_pb2.py
  %exclude /usr/bin/tensorboard
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/duration_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/api_implementation.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/wrappers_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/message_factory.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/type_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/descriptor_pb2.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/descriptor.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/text_encoding.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/message_listener.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__init__.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/__pycache__/any_pb2.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/wire_format.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/message.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/symbol_database.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/_parameterized.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/pyext/__pycache__/cpp_message.cpython-37.pyc
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/well_known_types.py
  %exclude /usr/lib/python3.7/site-packages/external/protobuf/python/google/protobuf/internal/testing_refleaks.py
