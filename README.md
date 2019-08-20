# orbit-plot

Plot the trajectory of a NOAA satellite on a map.

You must specify:

- time duration of the signal (seconds)
- name of satellite (i.e 'noaa 15')
- date time (year, month, day, hour, min, sec) corresponding to the beginning ot the satellite pass


## Dependencies

- pyplot
- pyorbital
- basemap
- geopy

## Example

- duracion_s = 755
- satelite = 'noaa 15'
- year = 2019
- day = 4
- month = 3
- hour = 19
- minute = 30
- second = 49

Those parameters produces the following map:

![alt text](https://github.com/gobelc/orbit-plot/blob/master/img/example.png)

## Jupyter notebook
You can run this program online with a Jupyter Notebook (see jupyter_notebook folder).
