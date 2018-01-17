set -ve

for filename in $(find ${CONDA_PREFIX}/conda-bld/ -name '*.tar.bz2')
do
    anaconda upload ${filename} -u statiskit --label linux-release
done

set +ve
