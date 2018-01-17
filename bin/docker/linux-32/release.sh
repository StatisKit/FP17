set -ve

source activate
rm -rf ${CONDA_PREFIX}/conda-bld/linux-32

git clone --recursive http://github.com/StatisKit/FP17

cd FP17/bin/conda
conda build fp17

cd ../../..

set +ve