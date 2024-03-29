#Importing libraries
from astropy.coordinates import Angle
from astropy import coordinates as coord
from astropy import units as u
from astropy.time import Time
import pandas as pd
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u

# Specify the observing location on Earth (for example, New York City)
observer_location = EarthLocation(
    lat=29.7128*u.deg, lon=77.0060*u.deg, height=0*u.m)


alti = []
Azi = []
for i in range(2000, 2151):
    # Specify the observing date and time (for example, January 12, 2024, at 20:00:00 UTC)
    observing_time = Time(f"{i}-01-01 20:00:00")

# Use SkyCoord.from_name to get the coordinates of Alcyone
    alcyone_coord = SkyCoord.from_name("Alcyone")

# Convert the coordinates to the Altitude-Azimuth frame for the specified observer location and time
    altaz_frame = AltAz(obstime=observing_time, location=observer_location)
    alcyone_altaz = alcyone_coord.transform_to(altaz_frame)
    alti.append(f'{alcyone_altaz.alt.degree:.2f}')
    Azi.append(f'{alcyone_altaz.az.degree:.2f}')

# Print the coordinates in the Altitude-Azimuth frame

c = pd.DataFrame(alti, columns=["Altitude"])
d = pd.DataFrame(Azi, columns=["Azimuth"])

# plt.plot(alti,label='Altitude')
plt.plot(Azi, label='Azimuth')
plt.legend()
plt.show()
