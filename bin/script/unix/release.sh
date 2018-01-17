set -ve

source activate
rm -rf ${CONDA_PREFIX}/conda-bld

cd ../../conda
conda build fp17

cd ../script/unix

set +ve