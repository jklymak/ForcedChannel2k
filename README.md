# Some Runs



## Runs:


## To setup

This uses the 5-km runs from `../ForcedChannel5k`
  - run `python get5kFile.py` for the proper run...
  - run `python gendataSpinup.py`
    - edit the envelope to make sure we use the correct bathy...

## Todo:

   - 2-D fft of `fastlevels.nc`

## Contents:

  - `MITgcm66h` is my version with `NF90io`.
  - `input` is where most model setup occurs.
  - `python` is where most processing occurs.

## Vagaries

   - Need `miniconda3` on the path!

## To compile on Conrad

  - `module load cray-netcdf-hdf5parallel`
  - `cd build/`
  - `../MITgcm66h/tools/genmake2 -optfile=../build_options/conrad -mods=../code/ -rootdir=../MITgcm66h -mpi`
  - `make depend`.  This will have some errors near the end about not being able to find source files for `module netcdf`.  This error is annoying but doesn't affect compile.
  - `make`

## To run

  - run `python gendata.py`
  - run `qsub -N jobname runModel.sh`
