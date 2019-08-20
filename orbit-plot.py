#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019
#   Gonzalo Belcredi
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.from mpl_toolkits.basemap import Basemap

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pytz
from pyorbital.orbital import Orbital
from datetime import datetime
from datetime import timedelta  
from mpl_toolkits.basemap import Basemap
import geopy.distance

duracion_s = 755
satelite = 'noaa 15'
year = 2019
day = 4
month = 3
hour = 19
minute = 30
second = 49

"""## Cálculo de trayectoria"""

orb = Orbital(satelite)

#now = datetime.utcnow()
local_tz = pytz.timezone("America/Montevideo")
UTC_dif = 3
dtobj = datetime(year,month,day,hour+UTC_dif,minute,second)
dtobj2= dtobj + timedelta(seconds=duracion_s)  

lon, lat, alt = orb.get_lonlatalt(dtobj)
lon2, lat2, alt2 = orb.get_lonlatalt(dtobj2)


coords_1 = (lat, lon)
coords_2 = (lat2, lon2)

distancia = geopy.distance.vincenty(coords_1, coords_2).km

print("Posición inicio:",  orb.get_position(dtobj))
print("Longitud:", lon)
print("Latitud:", lat)
print("Altura (km):", alt)

print("\nPosición final:",  orb.get_position(dtobj2))
print("Longitud:", lon2)
print("Latitud:", lat2)
print("Altura (km):", alt2)

print("\nDistancia recorrida (km): ", distancia)

"""# Visualización"""

# create new figure, axes instances.
fig=plt.figure(figsize=(8, 6), dpi=150)
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(width=12000000,height=9000000, projection='lcc',
            resolution=None,lat_1=20,lat_2=-50,lat_0=-30,lon_0=-60.)
# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
#m.drawmapboundary(fill_color='aqua')
# fill continents, set lake color same as ocean color.
#m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
# label parallels on right and top
# meridians on bottom and left
parallels = np.arange(0.,81,10.)
# labels = [left,right,top,bottom]
#m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(10.,351.,20.)
m.drawmeridians(meridians,labels=[True,False,False,True])
# plot blue dot on Boulder, colorado and label it as such.
#lon, lat = -104.237, 40.125 # Location of Boulder
# convert to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
xpt,ypt = m(lon,lat)
xpt2,ypt2 = m(lon2,lat2)

# convert back to lat/lon
lonpt, latpt = m(xpt,ypt,inverse=True)
lonpt2, latpt2 = m(xpt2,ypt2,inverse=True)

#m.drawcountries()
m.drawgreatcircle(lonpt, latpt, lonpt2, latpt2, 
                  linewidth=2, color='r', alpha=1)
m.plot(xpt,ypt,'bo', markersize=2)  # plot a blue dot there
m.plot(xpt2,ypt2,'bo', markersize=2)  # plot a blue dot there
m.bluemarble()
# put some text next to the dot, offset a little bit
# (the offset is in map projection coordinates)
plt.text(xpt+100000,ypt+100000,'  Inicio (%5.2fW,%3.2fN)' % (lonpt,latpt), fontsize=8,color='w')
plt.text(xpt2+100000,ypt2+100000,'  Fin (%5.2fW,%3.2fN)' % (lonpt2,latpt2), fontsize=8, color='w')
plt.suptitle('%s | %d/%d/%d %d:%d' %(satelite,day,month,year,hour,minute))
plt.title('Distancia recorrida: %d km' %distancia)
plt.show()
