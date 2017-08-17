#!/usr/bin/bash

if [ ! -e 0.1.4.tar.gz ]; then
	curl -O -L https://github.com/tensorflow/tensorboard/archive/0.1.4.tar.gz
fi	
rm -rf tensorboard-0.1.4
rm -rf tmp
mkdir tmp

tar -axf 0.1.4.tar.gz

pushd tensorboard-0.1.4
	bazel clean
	bazel build  tensorboard/pip_package:build_pip_package
	tensorboard/pip_package/build_pip_package.sh /tmp/whl
popd


