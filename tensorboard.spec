Name     : tensorboard
Version  : 2.3.0
Release  : 27
URL      : https://github.com/tensorflow/tensorboard/archive/2.3.0/tensorboard-2.3.0.tar.gz
Source0  : https://github.com/tensorflow/tensorboard/archive/2.3.0/tensorboard-2.3.0.tar.gz
Summary  : TensorFlow's visualization toolkit
Group    : Development/Tools
License  : Apache-2.0
Requires : Markdown
Requires : Werkzeug
Requires : absl-py
Requires : google-auth
Requires : google-auth-oauthlib
Requires : grpcio
Requires : numpy
Requires : protobuf
Requires : requests
Requires : setuptools
Requires : six
#Requires : tensorboard-plugin-wit
Requires : wheel
BuildRequires : Markdown
BuildRequires : Werkzeug
BuildRequires : absl-py
BuildRequires : bazel
BuildRequires : curl
BuildRequires : google-auth
BuildRequires : google-auth-oauthlib
BuildRequires : grpcio
BuildRequires : numpy
BuildRequires : openjdk-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : protobuf
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : requests
BuildRequires : setuptools
#BuildRequires : tensorboard-plugin-wit
BuildRequires : six
BuildRequires : virtualenv
BuildRequires : wheel

# SOURCES BEGIN
Source10: http://mirror.tensorflow.org/cdnjs.cloudflare.com/ajax/libs/numeric/1.2.6/numeric.js
Source11: http://mirror.tensorflow.org/files.pythonhosted.org/packages/0b/02/ae6ceac1baeda530866a85075641cec12989bd8d31af6d5ab4a3e8c92f47/webencodings-0.5.1.tar.gz
Source12: http://mirror.tensorflow.org/files.pythonhosted.org/packages/59/2d/b24bab64b409e22f026fee6705b035cb0698399a7b69449c49442b30af47/Werkzeug-0.15.4.tar.gz
Source13: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/-L14Jk06m6pUHB-5mXQQnYX0hVgzZQUfRDuZrPvH3D8.woff2
Source14: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/0eC6fl06luXEYWpBSJvXCIX0hVgzZQUfRDuZrPvH3D8.woff2
Source15: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/1hZf02POANh32k2VkgEoUBkAz4rYn47Zy2rvigWQf6w.woff2
Source16: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/77FXFjRbGzN4aCrSFhlh3oX0hVgzZQUfRDuZrPvH3D8.woff2
Source17: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0at14sYYdJg5dU2qzJEVSuta0.woff2
Source18: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0at1BW26QxpSj-_ZKm_xT4hWw.woff2
Source19: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0at4gp9Q8gbYrhqGlRav_IXfk.woff2
Source20: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0at6E8kM4xWR1_1bYURRojRGc.woff2
Source21: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0at9DiNsR5a-9Oe_Ivpu8XWlY.woff2
Source22: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0at_ZraR2Tg8w2lzm7kLNL0-w.woff2
Source23: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/7m8l7TlFO-S3VkhHuR0atwt_Rm691LTebKfY2ZkKSmI.woff2
Source24: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/97uahxiqZRoncBaCEI3aW4X0hVgzZQUfRDuZrPvH3D8.woff2
Source25: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/Fl4y0QdOxyyTHEGMXX8kcYX0hVgzZQUfRDuZrPvH3D8.woff2
Source26: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/Hgo13k-tfSpn0qi1SFdUfZBw1xU1rKptJj_0jans920.woff2
Source27: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/I3S1wsgSg9YCurV6PUkTOYX0hVgzZQUfRDuZrPvH3D8.woff2
Source28: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/K23cxWVTrIFD6DJsEVi07RkAz4rYn47Zy2rvigWQf6w.woff2
Source29: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/Ks_cVxiCiwUWVsFWFA3Bjn-_kf6ByYO6CLYdB4HQE-Y.woff2
Source30: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/NJ4vxlgWwWbEsv18dAhqnn-_kf6ByYO6CLYdB4HQE-Y.woff2
Source31: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/NYDWBdD4gIq26G5XYbHsFIX0hVgzZQUfRDuZrPvH3D8.woff2
Source32: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0Qt_Rm691LTebKfY2ZkKSmI.woff2
Source33: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0V4sYYdJg5dU2qzJEVSuta0.woff2
Source34: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0VBW26QxpSj-_ZKm_xT4hWw.woff2
Source35: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0Ygp9Q8gbYrhqGlRav_IXfk.woff2
Source36: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0aE8kM4xWR1_1bYURRojRGc.woff2
Source37: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0dDiNsR5a-9Oe_Ivpu8XWlY.woff2
Source38: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OLffGBTaF0XFOW1gnuHF0fZraR2Tg8w2lzm7kLNL0-w.woff2
Source39: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/OpXUqTo0UgQQhGj_SFdLWBkAz4rYn47Zy2rvigWQf6w.woff2
Source40: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/Pru33qjShpZSmG3z6VYwnYX0hVgzZQUfRDuZrPvH3D8.woff2
Source41: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/PwZc-YbIL414wB9rB1IAPYX0hVgzZQUfRDuZrPvH3D8.woff2
Source42: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/RxZJdnzeo3R5zSexge8UUZBw1xU1rKptJj_0jans920.woff2
Source43: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/UX6i4JxQDm3fVTc1CPuwqoX0hVgzZQUfRDuZrPvH3D8.woff2
Source44: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/WxrXJa0C3KdtC7lMafG4dRkAz4rYn47Zy2rvigWQf6w.woff2
Source45: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/ZLqKeelYbATG60EpZBSDy4X0hVgzZQUfRDuZrPvH3D8.woff2
Source46: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/_VYFx-s824kXq_Ul2BHqYH-_kf6ByYO6CLYdB4HQE-Y.woff2
Source47: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/cDKhRaXnQTOVbaoxwdOr9xkAz4rYn47Zy2rvigWQf6w.woff2
Source48: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/d-6IYplOFocCacKzxwXSOJBw1xU1rKptJj_0jans920.woff2
Source49: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/isZ-wbCXNKAbnjo6_TwHToX0hVgzZQUfRDuZrPvH3D8.woff2
Source50: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/jSN2CGVDbcVyCnfJfjSdfIX0hVgzZQUfRDuZrPvH3D8.woff2
Source51: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/mbmhprMH69Zi6eEPBYVFhYX0hVgzZQUfRDuZrPvH3D8.woff2
Source52: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/mx9Uck6uB63VIKFYnEMXrYX0hVgzZQUfRDuZrPvH3D8.woff2
Source53: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/oHi30kwQWvpCWqAhzHcCSIX0hVgzZQUfRDuZrPvH3D8.woff2
Source54: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/oMMgfZMQthOryQo9n22dcuvvDin1pK8aKteLpeZ5c0A.woff2
Source55: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/oOeFwZNlrTefzLYmlVV1UIX0hVgzZQUfRDuZrPvH3D8.woff2
Source56: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/rGvHdJnr2l75qb0YND9NyIX0hVgzZQUfRDuZrPvH3D8.woff2
Source57: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/sTdaA6j0Psb920Vjv-mrzH-_kf6ByYO6CLYdB4HQE-Y.woff2
Source58: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcC14sYYdJg5dU2qzJEVSuta0.woff2
Source59: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcC1BW26QxpSj-_ZKm_xT4hWw.woff2
Source60: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcC4gp9Q8gbYrhqGlRav_IXfk.woff2
Source61: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcC6E8kM4xWR1_1bYURRojRGc.woff2
Source62: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcC9DiNsR5a-9Oe_Ivpu8XWlY.woff2
Source63: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcC_ZraR2Tg8w2lzm7kLNL0-w.woff2
Source64: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/t6Nd4cfPRhZP44Q5QAjcCwt_Rm691LTebKfY2ZkKSmI.woff2
Source65: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/tnj4SB6DNbdaQnsM8CFqBX-_kf6ByYO6CLYdB4HQE-Y.woff2
Source66: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/uYECMKoHcO9x1wdmbyHIm3-_kf6ByYO6CLYdB4HQE-Y.woff2
Source67: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/vPcynSL0qHq_6dX7lKVByXYhjbSpvc47ee6xR_80Hnw.woff2
Source68: http://mirror.tensorflow.org/fonts.gstatic.com/s/roboto/v18/vSzulfKSK0LLjjfeaxcREhkAz4rYn47Zy2rvigWQf6w.woff2
Source69: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59Fz1T7aJLK6nKpn36IMwTcMMc.woff2
Source70: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59Fz1x-M1I1w5OMiqnVF8xBLhU.woff2
Source71: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59Fz4gd9OEPUCN3AdYW0e8tat4.woff2
Source72: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59Fz8bIQSYZnWLaWC9QNCpTK_U.woff2
Source73: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59Fz_79_ZuUxCigM2DespTnFaw.woff2
Source74: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59FzwXaAXup5mZlfK6xRLrhsco.woff2
Source75: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/N4duVc9C58uwPiY8_59Fzwn6Wqxo-xwxilDXPU8chVU.woff2
Source76: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpY14sYYdJg5dU2qzJEVSuta0.woff2
Source77: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpY1BW26QxpSj-_ZKm_xT4hWw.woff2
Source78: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpY4gp9Q8gbYrhqGlRav_IXfk.woff2
Source79: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpY6E8kM4xWR1_1bYURRojRGc.woff2
Source80: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpY9DiNsR5a-9Oe_Ivpu8XWlY.woff2
Source81: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpY_ZraR2Tg8w2lzm7kLNL0-w.woff2
Source82: http://mirror.tensorflow.org/fonts.gstatic.com/s/robotomono/v5/hMqPNLsu_dywMa4C_DEpYwt_Rm691LTebKfY2ZkKSmI.woff2
Source83: http://mirror.tensorflow.org/github.com/angular/clutz/archive/7ef7cdb156cd5f0359eb3b22b259d780e3ad825d.tar.gz
Source84: http://mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/db4683a2a1836ac8e265804ca5fa31852395185b.tar.gz
Source85: http://mirror.tensorflow.org/github.com/bazelbuild/rules_nodejs/releases/download/1.6.0/rules_nodejs-1.6.0.tar.gz
Source86: http://mirror.tensorflow.org/github.com/bazelbuild/rules_webtesting/releases/download/0.3.1/rules_webtesting.tar.gz
Source87: http://mirror.tensorflow.org/nodejs.org/dist/v6.9.1/node-v6.9.1-linux-x64.tar.xz
Source88: http://mirror.tensorflow.org/pypi.python.org/packages/1d/25/3f6d2cb31ec42ca5bd3bfbea99b63892b735d76e26f20dd2dcc34ffe4f0d/Markdown-2.6.8.tar.gz
Source89: http://mirror.tensorflow.org/pypi.python.org/packages/source/s/six/six-1.13.0.tar.gz
Source90: http://mirror.tensorflow.org/raw.githubusercontent.com/Microsoft/TypeScript/v2.9.2/lib/lib.dom.d.ts
Source91: http://mirror.tensorflow.org/raw.githubusercontent.com/Microsoft/TypeScript/v2.9.2/lib/lib.es6.d.ts
Source92: http://mirror.tensorflow.org/raw.githubusercontent.com/Microsoft/TypeScript/v2.9.2/lib/tsc.js
Source93: http://mirror.tensorflow.org/raw.githubusercontent.com/cpettitt/dagre/v0.8.2/dist/dagre.core.js
Source94: http://mirror.tensorflow.org/raw.githubusercontent.com/cpettitt/graphlib/v2.1.5/dist/graphlib.core.js
Source95: http://mirror.tensorflow.org/raw.githubusercontent.com/google/material-design-icons/3.0.1/action/svg/production/ic_help_outline_24px.svg
Source96: http://mirror.tensorflow.org/raw.githubusercontent.com/google/material-design-icons/3.0.1/action/svg/production/ic_info_outline_24px.svg
Source97: http://mirror.tensorflow.org/raw.githubusercontent.com/google/material-design-icons/3.0.1/action/svg/production/ic_settings_24px.svg
Source98: http://mirror.tensorflow.org/raw.githubusercontent.com/google/material-design-icons/3.0.1/content/svg/production/ic_content_copy_24px.svg
Source99: http://mirror.tensorflow.org/raw.githubusercontent.com/google/material-design-icons/3.0.1/navigation/svg/production/ic_refresh_24px.svg
Source100: http://mirror.tensorflow.org/raw.githubusercontent.com/mrdoob/three.js/r108/build/three.js
Source101: http://mirror.tensorflow.org/raw.githubusercontent.com/mrdoob/three.js/r108/examples/js/controls/OrbitControls.js
Source102: http://mirror.tensorflow.org/raw.githubusercontent.com/tensorflow/graphics/fa0fc3496d86f0235d614a5f9a27257a1898cae2/tensorflow_graphics/tensorboard/mesh_visualizer/tf_mesh_dashboard/array-buffer-data-provider.js
Source103: http://mirror.tensorflow.org/raw.githubusercontent.com/tensorflow/graphics/fa0fc3496d86f0235d614a5f9a27257a1898cae2/tensorflow_graphics/tensorboard/mesh_visualizer/tf_mesh_dashboard/mesh-viewer.js
Source104: http://mirror.tensorflow.org/raw.githubusercontent.com/waylonflinn/weblas/v0.9.0/dist/weblas.js
Source105: http://mirror.tensorflow.org/registry.npmjs.org/plottable/-/plottable-3.7.0.tgz
Source106: http://mirror.tensorflow.org/repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.9/commons-lang3-3.9.jar
Source107: http://mirror.tensorflow.org/repo1.maven.org/maven2/org/apache/commons/commons-text/1.6/commons-text-1.6.jar
Source108: http://mirror.tensorflow.org/unpkg.com/umap-js@1.2.2/lib/umap-js.min.js
Source109: https://github.com/PolymerElements/iron-a11y-announcer/archive/v2.1.0/iron-a11y-announcer-2.1.0.tar.gz
Source110: https://github.com/PolymerElements/iron-a11y-keys-behavior/archive/v2.1.0/iron-a11y-keys-behavior-2.1.0.tar.gz
Source111: https://github.com/PolymerElements/iron-autogrow-textarea/archive/v2.2.0/iron-autogrow-textarea-2.2.0.tar.gz
Source112: https://github.com/PolymerElements/iron-behaviors/archive/v2.1.1/iron-behaviors-2.1.1.tar.gz
Source113: https://github.com/PolymerElements/iron-checked-element-behavior/archive/v2.1.0/iron-checked-element-behavior-2.1.0.tar.gz
Source114: https://github.com/PolymerElements/iron-collapse/archive/v2.2.1/iron-collapse-2.2.1.tar.gz
Source115: https://github.com/PolymerElements/iron-demo-helpers/archive/v2.1.0/iron-demo-helpers-2.1.0.tar.gz
Source116: https://github.com/PolymerElements/iron-dropdown/archive/v2.2.1/iron-dropdown-2.2.1.tar.gz
Source117: https://github.com/PolymerElements/iron-fit-behavior/archive/v2.2.1/iron-fit-behavior-2.2.1.tar.gz
Source118: https://github.com/PolymerElements/iron-flex-layout/archive/v2.0.3/iron-flex-layout-2.0.3.tar.gz
Source119: https://github.com/PolymerElements/iron-form-element-behavior/archive/v2.1.3/iron-form-element-behavior-2.1.3.tar.gz
Source120: https://github.com/PolymerElements/iron-icon/archive/v2.1.0/iron-icon-2.1.0.tar.gz
Source121: https://github.com/PolymerElements/iron-icons/archive/v2.1.1/iron-icons-2.1.1.tar.gz
Source122: https://github.com/PolymerElements/iron-iconset-svg/archive/v2.2.0/iron-iconset-svg-2.2.0.tar.gz
Source123: https://github.com/PolymerElements/iron-image/archive/v2.2.1/iron-image-2.2.1.tar.gz
Source124: https://github.com/PolymerElements/iron-input/archive/v2.1.3/iron-input-2.1.3.tar.gz
Source125: https://github.com/PolymerElements/iron-list/archive/v2.0.19/iron-list-2.0.19.tar.gz
Source126: https://github.com/PolymerElements/iron-menu-behavior/archive/v2.1.0/iron-menu-behavior-2.1.0.tar.gz
Source127: https://github.com/PolymerElements/iron-meta/archive/v2.1.0/iron-meta-2.1.0.tar.gz
Source128: https://github.com/PolymerElements/iron-overlay-behavior/archive/v2.3.3/iron-overlay-behavior-2.3.3.tar.gz
Source129: https://github.com/PolymerElements/iron-pages/archive/v2.1.0/iron-pages-2.1.0.tar.gz
Source130: https://github.com/PolymerElements/iron-range-behavior/archive/v2.1.0/iron-range-behavior-2.1.0.tar.gz
Source131: https://github.com/PolymerElements/iron-resizable-behavior/archive/v2.1.0/iron-resizable-behavior-2.1.0.tar.gz
Source132: https://github.com/PolymerElements/iron-scroll-target-behavior/archive/v2.1.0/iron-scroll-target-behavior-2.1.0.tar.gz
Source133: https://github.com/PolymerElements/iron-selector/archive/v2.1.0/iron-selector-2.1.0.tar.gz
Source134: https://github.com/PolymerElements/iron-validatable-behavior/archive/v2.1.0/iron-validatable-behavior-2.1.0.tar.gz
Source135: https://github.com/PolymerElements/iron-validator-behavior/archive/v2.1.0/iron-validator-behavior-2.1.0.tar.gz
Source136: https://github.com/PolymerElements/marked-element/archive/v2.4.0/marked-element-2.4.0.tar.gz
Source137: https://github.com/PolymerElements/neon-animation/archive/v2.2.1/neon-animation-2.2.1.tar.gz
Source138: https://github.com/PolymerElements/paper-behaviors/archive/v2.1.0/paper-behaviors-2.1.0.tar.gz
Source139: https://github.com/PolymerElements/paper-button/archive/v2.1.0/paper-button-2.1.0.tar.gz
Source140: https://github.com/PolymerElements/paper-card/archive/v2.1.0/paper-card-2.1.0.tar.gz
Source141: https://github.com/PolymerElements/paper-checkbox/archive/v2.0.3/paper-checkbox-2.0.3.tar.gz
Source142: https://github.com/PolymerElements/paper-dialog-behavior/archive/v2.2.2/paper-dialog-behavior-2.2.2.tar.gz
Source143: https://github.com/PolymerElements/paper-dialog-scrollable/archive/v2.2.0/paper-dialog-scrollable-2.2.0.tar.gz
Source144: https://github.com/PolymerElements/paper-dialog/archive/v2.1.1/paper-dialog-2.1.1.tar.gz
Source145: https://github.com/PolymerElements/paper-dropdown-menu/archive/v2.1.0/paper-dropdown-menu-2.1.0.tar.gz
Source146: https://github.com/PolymerElements/paper-header-panel/archive/v2.1.0/paper-header-panel-2.1.0.tar.gz
Source147: https://github.com/PolymerElements/paper-icon-button/archive/v2.2.0/paper-icon-button-2.2.0.tar.gz
Source148: https://github.com/PolymerElements/paper-input/archive/v2.2.3/paper-input-2.2.3.tar.gz
Source149: https://github.com/PolymerElements/paper-item/archive/v2.1.0/paper-item-2.1.0.tar.gz
Source150: https://github.com/PolymerElements/paper-listbox/archive/v2.1.0/paper-listbox-2.1.0.tar.gz
Source151: https://github.com/PolymerElements/paper-material/archive/v2.1.0/paper-material-2.1.0.tar.gz
Source152: https://github.com/PolymerElements/paper-menu-button/archive/v2.1.1/paper-menu-button-2.1.1.tar.gz
Source153: https://github.com/PolymerElements/paper-progress/archive/v2.1.0/paper-progress-2.1.0.tar.gz
Source154: https://github.com/PolymerElements/paper-radio-button/archive/v2.1.0/paper-radio-button-2.1.0.tar.gz
Source155: https://github.com/PolymerElements/paper-radio-group/archive/v2.2.0/paper-radio-group-2.2.0.tar.gz
Source156: https://github.com/PolymerElements/paper-ripple/archive/v2.1.0/paper-ripple-2.1.0.tar.gz
Source157: https://github.com/PolymerElements/paper-slider/archive/v2.0.6/paper-slider-2.0.6.tar.gz
Source158: https://github.com/PolymerElements/paper-spinner/archive/v2.1.0/paper-spinner-2.1.0.tar.gz
Source159: https://github.com/PolymerElements/paper-styles/archive/v2.1.0/paper-styles-2.1.0.tar.gz
Source160: https://github.com/PolymerElements/paper-tabs/archive/v2.1.0/paper-tabs-2.1.0.tar.gz
Source161: https://github.com/PolymerElements/paper-toast/archive/v2.1.0/paper-toast-2.1.0.tar.gz
Source162: https://github.com/PolymerElements/paper-toggle-button/archive/v2.1.1/paper-toggle-button-2.1.1.tar.gz
Source163: https://github.com/PolymerElements/paper-toolbar/archive/v2.1.0/paper-toolbar-2.1.0.tar.gz
Source164: https://github.com/PolymerElements/paper-tooltip/archive/v2.1.1/paper-tooltip-2.1.1.tar.gz
Source165: https://github.com/PolymerElements/prism-element/archive/v2.1.0/prism-element-2.1.0.tar.gz
Source166: https://github.com/bazelbuild/bazel-skylib/archive/0.7.0/bazel-skylib-0.7.0.tar.gz
Source167: https://github.com/bazelbuild/rules_sass/archive/1.26.3/rules_sass-1.26.3.zip
Source168: https://github.com/google/closure-compiler/archive/v20190513/closure-compiler-20190513.tar.gz
Source169: https://github.com/google/closure-library/archive/v20191027/closure-library-20191027.tar.gz
Source170: https://github.com/html5lib/html5lib-python/archive/1.0.1/html5lib-python-1.0.1.tar.gz
Source171: https://github.com/lodash/lodash/archive/4.17.5/lodash-4.17.5.tar.gz
Source172: https://github.com/mozilla/bleach/archive/v2.0/bleach-2.0.tar.gz
Source173: https://github.com/polymer/polymer/archive/v2.7.0/polymer-2.7.0.tar.gz
Source174: https://github.com/tensorflow/tensorflow/archive/v2.1.0/tensorflow-2.1.0.tar.gz
Source175: https://github.com/vaadin/vaadin-grid/archive/v3.0.2/vaadin-grid-3.0.2.tar.gz
Source176: https://github.com/vaadin/vaadin-split-layout/archive/v1.1.0/vaadin-split-layout-1.1.0.tar.gz
Source177: https://github.com/web-animations/web-animations-js/archive/2.2.1/web-animations-js-2.2.1.tar.gz
Source178: https://github.com/webcomponents/shadycss/archive/v1.9.1/shadycss-1.9.1.tar.gz
Source179: https://github.com/webcomponents/webcomponentsjs/archive/v1.3.3/webcomponentsjs-1.3.3.tar.gz
Source180: https://mirror.bazel.build/bazel_java_tools/releases/javac11/v10.0/java_tools_javac11_linux-v10.0.zip
Source181: https://mirror.bazel.build/github.com/bazelbuild/rules_cc/archive/b7fe9697c0c76ab2fd431a891dbb9a6a32ed7c3e.tar.gz
Source182: https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/981f06c3d2bd10225e85209904090eb7b5fb26bd.tar.gz
Source183: https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/97d8af4dc474595af3900dd85cb3a29ad28cc313.tar.gz
Source184: https://mirror.bazel.build/github.com/yarnpkg/yarn/releases/download/v1.19.1/yarn-v1.19.1.tar.gz
Source185: https://mirror.bazel.build/maven.ibiblio.org/maven2/com/google/jsinterop/jsinterop-annotations/1.0.1/jsinterop-annotations-1.0.1.jar
Source186: https://mirror.bazel.build/nodejs.org/dist/v12.13.0/node-v12.13.0-linux-x64.tar.xz
Source187: https://mirror.bazel.build/openjdk/azul-zulu11.37.17-ca-jdk11.0.6/zulu11.37.17-ca-jdk11.0.6-linux_x64.tar.gz
Source188: https://mirror.bazel.build/repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.jar
Source189: https://mirror.bazel.build/repo1.maven.org/maven2/args4j/args4j/2.0.26/args4j-2.0.26.jar
Source190: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/auto/value/auto-value-annotations/1.6/auto-value-annotations-1.6.jar
Source191: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/auto/value/auto-value/1.6/auto-value-1.6.jar
Source192: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/closure-stylesheets/closure-stylesheets/1.5.0/closure-stylesheets-1.5.0.jar
Source193: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/code/findbugs/jsr305/2.0.3/jsr305-2.0.3.jar
Source194: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/code/gson/gson/2.7/gson-2.7.jar
Source195: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/common/html/types/types/1.0.7/types-1.0.7.jar
Source196: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/dagger/dagger-compiler/2.14.1/dagger-compiler-2.14.1.jar
Source197: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/dagger/dagger-producers/2.14.1/dagger-producers-2.14.1.jar
Source198: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/dagger/dagger-spi/2.14.1/dagger-spi-2.14.1.jar
Source199: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/dagger/dagger/2.14.1/dagger-2.14.1.jar
Source200: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/errorprone/error_prone_annotations/2.1.3/error_prone_annotations-2.1.3.jar
Source201: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/errorprone/javac-shaded/9-dev-r4023-3/javac-shaded-9-dev-r4023-3.jar
Source202: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/googlejavaformat/google-java-format/1.5/google-java-format-1.5.jar
Source203: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/guava/guava/25.1-jre/guava-25.1-jre.jar
Source204: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/inject/extensions/guice-assistedinject/4.1.0/guice-assistedinject-4.1.0.jar
Source205: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/inject/extensions/guice-multibindings/4.1.0/guice-multibindings-4.1.0.jar
Source206: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/inject/guice/4.1.0/guice-4.1.0.jar
Source207: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/javascript/closure-compiler-unshaded/v20191027/closure-compiler-unshaded-v20191027.jar
Source208: https://mirror.bazel.build/repo1.maven.org/maven2/com/google/template/soy/2019-07-14/soy-2019-07-14.jar
Source209: https://mirror.bazel.build/repo1.maven.org/maven2/com/ibm/icu/icu4j/57.1/icu4j-57.1.jar
Source210: https://mirror.bazel.build/repo1.maven.org/maven2/com/squareup/javapoet/1.9.0/javapoet-1.9.0.jar
Source211: https://mirror.bazel.build/repo1.maven.org/maven2/javax/annotation/jsr250-api/1.0/jsr250-api-1.0.jar
Source212: https://mirror.bazel.build/repo1.maven.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar
Source213: https://mirror.bazel.build/repo1.maven.org/maven2/org/json/json/20160212/json-20160212.jar
Source214: https://mirror.bazel.build/repo1.maven.org/maven2/org/jsoup/jsoup/1.11.3/jsoup-1.11.3.jar
Source215: https://mirror.bazel.build/repo1.maven.org/maven2/org/ow2/asm/asm-analysis/6.0/asm-analysis-6.0.jar
Source216: https://mirror.bazel.build/repo1.maven.org/maven2/org/ow2/asm/asm-commons/6.0/asm-commons-6.0.jar
Source217: https://mirror.bazel.build/repo1.maven.org/maven2/org/ow2/asm/asm-tree/6.0/asm-tree-6.0.jar
Source218: https://mirror.bazel.build/repo1.maven.org/maven2/org/ow2/asm/asm-util/6.0/asm-util-6.0.jar
Source219: https://mirror.bazel.build/repo1.maven.org/maven2/org/ow2/asm/asm/6.0/asm-6.0.jar
Source220: https://storage.googleapis.com/mirror.tensorflow.org/github.com/grpc/grpc/archive/4566c2a29ebec0835643b972eb99f4306c4234a3.tar.gz
Source221: https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/protobuf/archive/310ba5ee72661c081129eb878c1bbcec936b20f0.tar.gz
Source222: https://storage.googleapis.com/mirror.tensorflow.org/zlib.net/zlib-1.2.11.tar.gz
# SOURCES END

# webcomponents.js/webcomponents.js.d.ts
Source1000: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/46719185c564694c5583c4b7ad94dbb786ecad46.tar.gz
# types/d3-*/index.d.ts
Source1001: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/526dd2e57684fa586452445a181d37369533d02e.tar.gz
# google.analytics/ga.d.ts
Source1002: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/5d0f2126c8dac8fce0ff020218aea06607213b0d.tar.gz
# sinon/sinon.d.ts
Source1003: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/708609e0764daeb5eb64104af7aca50c520c4e6e.tar.gz
# threejs/three.d.ts
Source1004: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/8cb9ee3fdfe352cfef672bdfdb5f9c428f915e9f.tar.gz
# polymer/polymer.d.ts
Source1005: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/a872802c0c84ba98ff207d5e673a1fa867c67fd6.tar.gz
# types/sinon-chai/v2/index.d.ts
Source1006: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/b4715b48d6a64a288f4ca6d0d2efcbffb36dd1cf.tar.gz
# types/d3-array/index.d.ts
Source1007: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/b6746d73a2ddf103c6825449ee2b0953f716d994.tar.gz
# chai/chai.d.ts
# mocha/mocha.d.ts
Source1008: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/ebc69904eb78f94030d5d517b42db20867f679c0.tar.gz
# lodash/lodash.d.ts
Source1009: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/efd40e67ff323f7147651bdbef03c03ead7b1675.tar.gz
# types/d3-scale/index.d.ts
Source1010: https://github.com/DefinitelyTyped/DefinitelyTyped/archive/ff2359e74ce1c539097e47dc586d49d348a94587.tar.gz

# From http://mirror.tensorflow.org/raw.githubusercontent.com/Microsoft/TypeScript/v2.7.2/LICENSE.txt
Source1020: TYPESCRIPT_LICENSE
# From http://mirror.tensorflow.org/raw.githubusercontent.com/google/roboto/ba03b84b90b50afd99f9688059447bc545e5c0e1/LICENSE
Source1021: ROBOTO_LICENSE
# From http://mirror.tensorflow.org/raw.githubusercontent.com/waylonflinn/weblas/v0.9.0/LICENSE
Source1022: WEBLAS_LICENSE
# From http://mirror.tensorflow.org/raw.githubusercontent.com/cpettitt/graphlib/v2.1.5/LICENSE
Source1023: GRAPHLIB_LICENSE
# From http://mirror.tensorflow.org/raw.githubusercontent.com/mrdoob/three.js/r108/LICENSE
Source1024: THREEJS_LICENSE
# From http://mirror.tensorflow.org/raw.githubusercontent.com/sloisel/numeric/v1.2.6/license.txt
Source1025: NUMERIC_LICENSE

Source1030: http://localhost/cgit/projects/tensorboard-yarn-cache/snapshot/tensorboard-yarn-cache-2.3.0.3.tar.xz

Patch1: 0001-Run-yarn-in-offline-mode.patch
Patch2: 0002-Remove-requirement-on-tensorboard-plugin-wit.patch

%description
TensorBoard provides the visualization and tooling needed for machine learning
experimentation: tracking and visualizing metrics such as loss and accuracy;
visualizing the model graph (ops and layers); viewing histograms of weights,
biases, or other tensors as they change over time; projecting embeddings to a
lower dimensional space; displaying images, text, and audio data; profiling
TensorFlow programs; and much more.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

InstallCacheBazel() {
  sha256=$(sha256sum $1 | cut -f1 -d" ")
  mkdir -p /var/tmp/cache/content_addressable/sha256/$sha256
  cp $1 /var/tmp/cache/content_addressable/sha256/$sha256/file
}
export -f InstallCacheBazel

InstallCacheYarn() {
  mkdir -p $HOME/.cache/yarn
  cd $HOME/.cache/yarn
  tar --strip-components=1 -xf $1
  ls -a
  rm README
}

InstallDTS() {
  local tar="$1"
  shift
  local patterns="$@"
  tmp="$(mktemp -d -p .)"
  tar -C $tmp -xf "$tar"
  for pattern in $patterns; do
    find "$tmp" -path "*/$pattern" -print -exec bash -c 'InstallCacheBazel {}' \;
  done
  rm -rf $tmp
}

# CACHE BAZEL BEGIN
InstallCacheBazel %{SOURCE10}
InstallCacheBazel %{SOURCE11}
InstallCacheBazel %{SOURCE12}
InstallCacheBazel %{SOURCE13}
InstallCacheBazel %{SOURCE14}
InstallCacheBazel %{SOURCE15}
InstallCacheBazel %{SOURCE16}
InstallCacheBazel %{SOURCE17}
InstallCacheBazel %{SOURCE18}
InstallCacheBazel %{SOURCE19}
InstallCacheBazel %{SOURCE20}
InstallCacheBazel %{SOURCE21}
InstallCacheBazel %{SOURCE22}
InstallCacheBazel %{SOURCE23}
InstallCacheBazel %{SOURCE24}
InstallCacheBazel %{SOURCE25}
InstallCacheBazel %{SOURCE26}
InstallCacheBazel %{SOURCE27}
InstallCacheBazel %{SOURCE28}
InstallCacheBazel %{SOURCE29}
InstallCacheBazel %{SOURCE30}
InstallCacheBazel %{SOURCE31}
InstallCacheBazel %{SOURCE32}
InstallCacheBazel %{SOURCE33}
InstallCacheBazel %{SOURCE34}
InstallCacheBazel %{SOURCE35}
InstallCacheBazel %{SOURCE36}
InstallCacheBazel %{SOURCE37}
InstallCacheBazel %{SOURCE38}
InstallCacheBazel %{SOURCE39}
InstallCacheBazel %{SOURCE40}
InstallCacheBazel %{SOURCE41}
InstallCacheBazel %{SOURCE42}
InstallCacheBazel %{SOURCE43}
InstallCacheBazel %{SOURCE44}
InstallCacheBazel %{SOURCE45}
InstallCacheBazel %{SOURCE46}
InstallCacheBazel %{SOURCE47}
InstallCacheBazel %{SOURCE48}
InstallCacheBazel %{SOURCE49}
InstallCacheBazel %{SOURCE50}
InstallCacheBazel %{SOURCE51}
InstallCacheBazel %{SOURCE52}
InstallCacheBazel %{SOURCE53}
InstallCacheBazel %{SOURCE54}
InstallCacheBazel %{SOURCE55}
InstallCacheBazel %{SOURCE56}
InstallCacheBazel %{SOURCE57}
InstallCacheBazel %{SOURCE58}
InstallCacheBazel %{SOURCE59}
InstallCacheBazel %{SOURCE60}
InstallCacheBazel %{SOURCE61}
InstallCacheBazel %{SOURCE62}
InstallCacheBazel %{SOURCE63}
InstallCacheBazel %{SOURCE64}
InstallCacheBazel %{SOURCE65}
InstallCacheBazel %{SOURCE66}
InstallCacheBazel %{SOURCE67}
InstallCacheBazel %{SOURCE68}
InstallCacheBazel %{SOURCE69}
InstallCacheBazel %{SOURCE70}
InstallCacheBazel %{SOURCE71}
InstallCacheBazel %{SOURCE72}
InstallCacheBazel %{SOURCE73}
InstallCacheBazel %{SOURCE74}
InstallCacheBazel %{SOURCE75}
InstallCacheBazel %{SOURCE76}
InstallCacheBazel %{SOURCE77}
InstallCacheBazel %{SOURCE78}
InstallCacheBazel %{SOURCE79}
InstallCacheBazel %{SOURCE80}
InstallCacheBazel %{SOURCE81}
InstallCacheBazel %{SOURCE82}
InstallCacheBazel %{SOURCE83}
InstallCacheBazel %{SOURCE84}
InstallCacheBazel %{SOURCE85}
InstallCacheBazel %{SOURCE86}
InstallCacheBazel %{SOURCE87}
InstallCacheBazel %{SOURCE88}
InstallCacheBazel %{SOURCE89}
InstallCacheBazel %{SOURCE90}
InstallCacheBazel %{SOURCE91}
InstallCacheBazel %{SOURCE92}
InstallCacheBazel %{SOURCE93}
InstallCacheBazel %{SOURCE94}
InstallCacheBazel %{SOURCE95}
InstallCacheBazel %{SOURCE96}
InstallCacheBazel %{SOURCE97}
InstallCacheBazel %{SOURCE98}
InstallCacheBazel %{SOURCE99}
InstallCacheBazel %{SOURCE100}
InstallCacheBazel %{SOURCE101}
InstallCacheBazel %{SOURCE102}
InstallCacheBazel %{SOURCE103}
InstallCacheBazel %{SOURCE104}
InstallCacheBazel %{SOURCE105}
InstallCacheBazel %{SOURCE106}
InstallCacheBazel %{SOURCE107}
InstallCacheBazel %{SOURCE108}
InstallCacheBazel %{SOURCE109}
InstallCacheBazel %{SOURCE110}
InstallCacheBazel %{SOURCE111}
InstallCacheBazel %{SOURCE112}
InstallCacheBazel %{SOURCE113}
InstallCacheBazel %{SOURCE114}
InstallCacheBazel %{SOURCE115}
InstallCacheBazel %{SOURCE116}
InstallCacheBazel %{SOURCE117}
InstallCacheBazel %{SOURCE118}
InstallCacheBazel %{SOURCE119}
InstallCacheBazel %{SOURCE120}
InstallCacheBazel %{SOURCE121}
InstallCacheBazel %{SOURCE122}
InstallCacheBazel %{SOURCE123}
InstallCacheBazel %{SOURCE124}
InstallCacheBazel %{SOURCE125}
InstallCacheBazel %{SOURCE126}
InstallCacheBazel %{SOURCE127}
InstallCacheBazel %{SOURCE128}
InstallCacheBazel %{SOURCE129}
InstallCacheBazel %{SOURCE130}
InstallCacheBazel %{SOURCE131}
InstallCacheBazel %{SOURCE132}
InstallCacheBazel %{SOURCE133}
InstallCacheBazel %{SOURCE134}
InstallCacheBazel %{SOURCE135}
InstallCacheBazel %{SOURCE136}
InstallCacheBazel %{SOURCE137}
InstallCacheBazel %{SOURCE138}
InstallCacheBazel %{SOURCE139}
InstallCacheBazel %{SOURCE140}
InstallCacheBazel %{SOURCE141}
InstallCacheBazel %{SOURCE142}
InstallCacheBazel %{SOURCE143}
InstallCacheBazel %{SOURCE144}
InstallCacheBazel %{SOURCE145}
InstallCacheBazel %{SOURCE146}
InstallCacheBazel %{SOURCE147}
InstallCacheBazel %{SOURCE148}
InstallCacheBazel %{SOURCE149}
InstallCacheBazel %{SOURCE150}
InstallCacheBazel %{SOURCE151}
InstallCacheBazel %{SOURCE152}
InstallCacheBazel %{SOURCE153}
InstallCacheBazel %{SOURCE154}
InstallCacheBazel %{SOURCE155}
InstallCacheBazel %{SOURCE156}
InstallCacheBazel %{SOURCE157}
InstallCacheBazel %{SOURCE158}
InstallCacheBazel %{SOURCE159}
InstallCacheBazel %{SOURCE160}
InstallCacheBazel %{SOURCE161}
InstallCacheBazel %{SOURCE162}
InstallCacheBazel %{SOURCE163}
InstallCacheBazel %{SOURCE164}
InstallCacheBazel %{SOURCE165}
InstallCacheBazel %{SOURCE166}
InstallCacheBazel %{SOURCE167}
InstallCacheBazel %{SOURCE168}
InstallCacheBazel %{SOURCE169}
InstallCacheBazel %{SOURCE170}
InstallCacheBazel %{SOURCE171}
InstallCacheBazel %{SOURCE172}
InstallCacheBazel %{SOURCE173}
InstallCacheBazel %{SOURCE174}
InstallCacheBazel %{SOURCE175}
InstallCacheBazel %{SOURCE176}
InstallCacheBazel %{SOURCE177}
InstallCacheBazel %{SOURCE178}
InstallCacheBazel %{SOURCE179}
InstallCacheBazel %{SOURCE180}
InstallCacheBazel %{SOURCE181}
InstallCacheBazel %{SOURCE182}
InstallCacheBazel %{SOURCE183}
InstallCacheBazel %{SOURCE184}
InstallCacheBazel %{SOURCE185}
InstallCacheBazel %{SOURCE186}
InstallCacheBazel %{SOURCE187}
InstallCacheBazel %{SOURCE188}
InstallCacheBazel %{SOURCE189}
InstallCacheBazel %{SOURCE190}
InstallCacheBazel %{SOURCE191}
InstallCacheBazel %{SOURCE192}
InstallCacheBazel %{SOURCE193}
InstallCacheBazel %{SOURCE194}
InstallCacheBazel %{SOURCE195}
InstallCacheBazel %{SOURCE196}
InstallCacheBazel %{SOURCE197}
InstallCacheBazel %{SOURCE198}
InstallCacheBazel %{SOURCE199}
InstallCacheBazel %{SOURCE200}
InstallCacheBazel %{SOURCE201}
InstallCacheBazel %{SOURCE202}
InstallCacheBazel %{SOURCE203}
InstallCacheBazel %{SOURCE204}
InstallCacheBazel %{SOURCE205}
InstallCacheBazel %{SOURCE206}
InstallCacheBazel %{SOURCE207}
InstallCacheBazel %{SOURCE208}
InstallCacheBazel %{SOURCE209}
InstallCacheBazel %{SOURCE210}
InstallCacheBazel %{SOURCE211}
InstallCacheBazel %{SOURCE212}
InstallCacheBazel %{SOURCE213}
InstallCacheBazel %{SOURCE214}
InstallCacheBazel %{SOURCE215}
InstallCacheBazel %{SOURCE216}
InstallCacheBazel %{SOURCE217}
InstallCacheBazel %{SOURCE218}
InstallCacheBazel %{SOURCE219}
InstallCacheBazel %{SOURCE220}
InstallCacheBazel %{SOURCE221}
InstallCacheBazel %{SOURCE222}
# CACHE BAZEL END

# Miscellaneous TypeScript files, many with naming collisions.
InstallDTS %{SOURCE1000} webcomponents.js/webcomponents.js.d.ts
InstallDTS %{SOURCE1001} "types/d3-*/index.d.ts"
InstallDTS %{SOURCE1002} google.analytics/ga.d.ts
InstallDTS %{SOURCE1003} sinon/sinon.d.ts
InstallDTS %{SOURCE1004} threejs/three.d.ts
InstallDTS %{SOURCE1005} polymer/polymer.d.ts
InstallDTS %{SOURCE1006} types/sinon-chai/v2/index.d.ts
InstallDTS %{SOURCE1007} types/d3-array/index.d.ts
InstallDTS %{SOURCE1008} chai/chai.d.ts mocha/mocha.d.ts
InstallDTS %{SOURCE1009} lodash/lodash.d.ts
InstallDTS %{SOURCE1010} types/d3-scale/index.d.ts

# Additional license files to be cached. These are committed to the repo to
# avoid current and future naming collisions.
InstallCacheBazel %{SOURCE1020}
InstallCacheBazel %{SOURCE1021}
InstallCacheBazel %{SOURCE1022}
InstallCacheBazel %{SOURCE1023}
InstallCacheBazel %{SOURCE1024}
InstallCacheBazel %{SOURCE1025}

# A pre-built archive including cache content (~/.cache/yarn/...) from two
# `yarn install`s, one for this release of tensorboard and one for the
# rules_sass release (or git snapshot) pulled in as a dependency.
InstallCacheYarn %{SOURCE1030}

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1503005760
export GCC_IGNORE_WERROR=1

# perform a full clean
bazel clean --expunge

bazel build \
  --repository_cache=/var/tmp/cache \
  --verbose_failures \
  //tensorboard/pip_package:build_pip_package

# a place to put build_pip_package result
mkdir -p /var/tmp/tensorboard/

bazel run \
  --repository_cache=/var/tmp/cache \
  --verbose_failures \
  //tensorboard/pip_package:build_pip_package -- /var/tmp/tensorboard

%install
export SOURCE_DATE_EPOCH=1503005760
rm -rf %{buildroot}
pip3 install \
  --no-deps \
  --force-reinstall \
  --ignore-installed \
  --root %{buildroot} \
  /var/tmp/tensorboard/tensorboard-%{version}-py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/bin/tensorboard
/usr/lib/python3*/site-packages/
