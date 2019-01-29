set -ve

scons py --prefix=${PREFIX} -j${CPU_COUNT} --package=fp17

set +ve