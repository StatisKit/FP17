set -ve

export PY2K=2.7
export PY3K=3.6

source activate
rm -rf ${CONDA_PREFIX}/conda-bld

cd ../../conda
conda build fp17 --python=${PY2K}
conda build fp17 --python=${PY3K}

cd ../script/unix

set +ve