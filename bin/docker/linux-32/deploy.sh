set -ve

for filename in ${CONDA_PREFIX}/conda-bld/linux-32/*.tar.bz2
do
    anaconda upload ${filename} -u statiskit --label linux-x86_release
done

set +ve
