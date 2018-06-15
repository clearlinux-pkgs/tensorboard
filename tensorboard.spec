Name     : tensorboard
Version  : 1.7.0
Release  : 8
URL      : https://github.com/tensorflow/tensorboard/archive/1.7.0.tar.gz
Source0  : https://github.com/tensorflow/tensorboard/archive/1.7.0.tar.gz
Source1  : http://localhost/tensorflow/tensorboard-1.7.0-py3-none-any.whl
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
# TensorBoard ![Travis build status](https://travis-ci.org/tensorflow/tensorboard.svg?branch=master)

%prep
%setup -q -n tensorboard-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503005760


%install
export SOURCE_DATE_EPOCH=1503005760
rm -rf %{buildroot}
pip3 install --no-deps --force-reinstall  --root %{buildroot} %{SOURCE1}

%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages/
/usr/bin/tensorboard


%exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/api_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/field_mask_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/text_format.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/containers.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/containers.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/pyext/cpp_message.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/proto_builder.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/encoder.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/enum_type_wrapper.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/service.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/field_mask_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/empty_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/api_implementation.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/struct_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/json_format.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/service_reflection.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/compiler/__pycache__/plugin_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/pyext/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/struct_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/compiler/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/empty_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/compiler/plugin_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/text_encoding.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/wrappers_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/duration_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/python_message.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/text_format.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/proto_builder.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor_pool.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/json_format.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/descriptor_pool.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/api_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/type_checkers.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/message_listener.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/pyext/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/source_context_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/symbol_database.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/source_context_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor_database.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/enum_type_wrapper.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/timestamp_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/wire_format.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/python_message.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/testing_refleaks.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/well_known_types.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/service_reflection.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/encoder.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/compiler/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/_parameterized.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/service.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/descriptor_database.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/decoder.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/decoder.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/reflection.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/descriptor_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/message.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/message_factory.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/__pycache__/__init__.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/type_checkers.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/reflection.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/timestamp_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/type_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/any_pb2.py
  %exclude /usr/bin/tensorboard
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/duration_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/api_implementation.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/wrappers_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/message_factory.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/type_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/descriptor_pb2.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/descriptor.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/text_encoding.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/message_listener.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__init__.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/__pycache__/any_pb2.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/wire_format.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/message.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/symbol_database.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/__pycache__/_parameterized.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/pyext/__pycache__/cpp_message.cpython-36.pyc
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/well_known_types.py
  %exclude /usr/lib/python3.6/site-packages/external/protobuf/python/google/protobuf/internal/testing_refleaks.py
