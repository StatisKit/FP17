set -ve

for filename in ${CONDA_PREFIX}/conda-bld/osx-64/*.tar.bz2
do
    anaconda upload ${filename} -u statiskit --label osx-x86_64_release
done

set +ve
