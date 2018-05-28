import numpy as np
import xarray as xr

"""
Read the 5k data from 5 y on...
"""

origin = 'Channel5k1000_vrough_01'

inname = '../../ForcedChannel5k/results/{}/input/'.format(origin)

with xr.open_dataset(inname+'spinup.nc') as ds:
    ds = ds.isel(record=-1)
    print(ds.time)
    ds.to_netcdf('Channel5k_{}_Spinup.nc'.format(origin), 'w')

with xr.open_dataset(inname+'spinup2d.nc') as ds:
    ds = ds.isel(record=-1)
    print(ds.time)
    ds.to_netcdf('Channel5k_{}_Spinup2d.nc'.format(origin), 'w')
